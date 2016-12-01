import itertools
import re
import sys
import numpy as np
import tensorflow as tf
from build_network import build_network, ALPHABET, TARGET_CLASSES

MAX_LEN = 200
ALPHABET_DICT = {char: index for index, char in enumerate(ALPHABET)}
TARGET_DICT = {clazz: index for index, clazz in enumerate(TARGET_CLASSES)}


def data_to_tensor(texts, dictionary):
    text_indices = []
    lengths = []
    for text in texts:
        text = text.rstrip()
        indices = [dictionary.get(c, 0) for c in text]
        lengths.append(min(MAX_LEN, len(text)))
        if len(indices) > MAX_LEN:
            text_indices.append(indices[:MAX_LEN])
        else:
            text_indices.append(indices +
                                [0 for _ in range(MAX_LEN - len(indices))])
    return np.array(text_indices), np.array(lengths)


def evaluation(logits, targets, lengths):
    predicted_classes = np.argmax(logits, axis=2)

    correct = 0.
    correct_punct = 0.
    in_prediction = 0.
    in_annotation = 0.

    for predicted, target, length in zip(predicted_classes, targets, lengths):
        correct += np.sum(predicted[:length] == target[:length])
        correct_punct += np.sum((predicted[:length] > 0)
                                & (predicted[:length] == target[:length]))
        in_prediction += np.sum(predicted[:length] > 0)
        in_annotation += np.sum(target[:length] > 0)

    accuracy = correct / np.sum(lengths)
    precision = correct_punct / in_prediction if in_prediction else 0.
    recall = correct_punct / in_annotation if in_annotation else 0.
    if precision and recall:
        f_score = 2 * precision * recall / (precision + recall)
    else:
        f_score = 0.

    return (accuracy, precision, recall, f_score)


def main():
    seq_input, lengths, targets, predictions_tf, cross_entropy_tf, dropout_plc = build_network(
        max_lenght=MAX_LEN)
    f_text = open(sys.argv[1])
    f_punct = open(sys.argv[2])

    val_text, val_lengths = data_to_tensor(
        itertools.islice(f_text, 1000), ALPHABET_DICT)
    val_punct, _ = data_to_tensor(itertools.islice(f_punct, 1000), TARGET_DICT)

    bias_regex = re.compile(r'[Bb]ias')
    regularizable = [tf.reduce_sum(
        v ** 2) for v in tf.trainable_variables()
        if bias_regex.findall(v.name)]

    l2_value = sum(v * v for v in regularizable)
    l2_cost = 1e-6 * l2_value

    cost = cross_entropy_tf + l2_cost
    optimizer = tf.train.AdamOptimizer(1e-4)
    train_op = optimizer.minimize(cost)

    session = tf.Session(config=tf.ConfigProto(
        intra_op_parallelism_threads=8))
    session.run(tf.initialize_all_variables())
    saver = tf.train.Saver()

    batch_n = 0
    max_f_score = 0.

    while True:
        batch_n += 1
        text_batch, batch_lengths = data_to_tensor(
            itertools.islice(f_text, 64), ALPHABET_DICT)
        punct_batch, _ = data_to_tensor(
            itertools.islice(f_punct, 64), TARGET_DICT)

        if text_batch.shape == (0,):
            break

        _, predictions, cross_entropy = session.run(
            [train_op, predictions_tf, cross_entropy_tf],
            feed_dict={seq_input: text_batch,
                       targets: punct_batch,
                       lengths: batch_lengths,
                       dropout_plc: 0.5})
        accuracy, precision, recall, f_score = evaluation(
            predictions, punct_batch, batch_lengths)
        print("batch {}:\tacc: {:.4f}\tprec: {:.4f}\trecall: {:.4f}\tF1: {:.4f}\txent: {:.4f}".format(
            batch_n, accuracy, precision, recall, f_score, cross_entropy))

        if batch_n % 20 == 0:
            predictions, cross_entropy = session.run(
                [predictions_tf, cross_entropy_tf],
                feed_dict={seq_input: val_text,
                           targets: val_punct,
                           lengths: val_lengths,
                           dropout_plc: 1.0})
            accuracy, precision, recall, f_score = evaluation(
                predictions, punct_batch, batch_lengths)

            print("")
            print("Valdidation after batch {}".format(batch_n))
            print("  accuracy:       {:.5f}".format(accuracy))
            print("  precision:      {:.5f}".format(precision))
            print("  recall:         {:.5f}".format(recall))
            print(
                "  F1-score:       {:.5f} (previous max: {:.5f})".format(f_score, max_f_score))
            print("  cross-entropy:  {:.5f}".format(cross_entropy))

            print("")

            if f_score > max_f_score:
                max_f_score = f_score
                saver.save(session, "model.variables")

    f_text.close()
    f_punct.close()

if __name__ == "__main__":
    main()
