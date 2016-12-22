"""Training script for the spelling task."""
# -*- coding: utf-8 -*-

import itertools
import re
import sys
import numpy as np
import tensorflow as tf
from build_network import build_network, ALPHABET, TARGET_CLASSES

ALPHABET_DICT = {char: index for index, char in enumerate(ALPHABET)}
TARGET_DICT = {clazz: index for index, clazz in enumerate(TARGET_CLASSES)}

MAX_LEN = 200

def data_to_tensor(texts, dictionary):
    text_indices = [[dictionary.get(c, 0) for c in text.rstrip()[:MAX_LEN]]
                    for text in texts]
    lengths = [len(i) for i in text_indices]
    max_len = max(lengths)
    matrix = []
    for indices in text_indices:
        matrix.append(indices +
                      [0 for _ in range(max_len - len(indices))])
    return np.array(matrix), np.array(lengths)


def evaluation(logits, targets, lengths):
    predicted_classes = np.argmax(logits, axis=2)

    correct = 0.
    count = 0.

    for predicted, target, length in zip(predicted_classes, targets, lengths):
        count += np.sum(target[:length] > 0)
        correct += np.sum((predicted[:length] == target[:length]) * (target[:length] > 0))

    accuracy = correct / count

    return accuracy

def get_train_op(model):
    bias_regex = re.compile(r'[Bb]ias')
    regularizable = [tf.reduce_sum(
        v ** 2) for v in tf.trainable_variables()
                     if bias_regex.findall(v.name)]

    l2_value = sum(v * v for v in regularizable)
    l2_cost = 1e-6 * l2_value

    cost = model.cost + l2_cost
    optimizer = tf.train.AdamOptimizer(1e-4)
    train_op = optimizer.minimize(cost)
    return train_op


def main():
    model = build_network()
    print("The graph has been built.")
    f_text = open(sys.argv[1], encoding="utf-8")
    f_cap = open(sys.argv[2])

    val_text, val_lengths = data_to_tensor(
        itertools.islice(f_text, 400), ALPHABET_DICT)
    val_cap, _ = data_to_tensor(itertools.islice(f_cap, 400), TARGET_DICT)
    print("Validation data are ready.")

    train_op = get_train_op(model)
    print("Optimizer has been built.")

    session = tf.Session(config=tf.ConfigProto(
        intra_op_parallelism_threads=8))
    session.run(tf.initialize_all_variables())
    saver = tf.train.Saver()
    print("Session initialized.")

    batch_n = 0
    max_acc = 0.

    while True:
        batch_n += 1
        text_batch, batch_lengths = data_to_tensor(
            itertools.islice(f_text, 50), ALPHABET_DICT)
        cap_batch, _ = data_to_tensor(
            itertools.islice(f_cap, 50), TARGET_DICT)

        if text_batch.shape == (0,):
            break

        _, predictions, cross_entropy = session.run(
            [train_op, model.predictions, model.cost],
            feed_dict={model.input: text_batch,
                       model.targets: cap_batch,
                       model.lengths: batch_lengths})
        accuracy = evaluation(
            predictions, cap_batch, batch_lengths)
        print("batch {}:\tacc: {:.4f}\txent: {:.4f}".format(
            batch_n, accuracy, cross_entropy))

        if batch_n % 10 == 0:
            predictions, cross_entropy = session.run(
                [model.predictions, model.cost],
                feed_dict={model.input: val_text,
                           model.targets: val_cap,
                           model.lengths: val_lengths})
            accuracy = evaluation(
                predictions, val_cap, batch_lengths)

            print("")
            print("Valdidation after batch {}".format(batch_n))
            print("  accuracy:       {:.5f}".format(accuracy))
            print("  cross-entropy:  {:.5f}".format(cross_entropy))

            print("")

            if accuracy > max_acc:
                max_acc = accuracy
                saver.save(session, "model.variables")

    f_text.close()
    f_cap.close()

if __name__ == "__main__":
    main()
