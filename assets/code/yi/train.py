# -*- coding: utf-8 -*- 

import itertools
import re
import sys
import numpy as np
import tensorflow as tf
from build_network import build_network, ALPHABET, TARGET_CLASSES
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

ALPHABET_DICT = {char: index for index, char in enumerate(ALPHABET)}
TARGET_DICT = {clazz: index for index, clazz in enumerate(TARGET_CLASSES)}

MAX_LEN=200

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


def main():
    seq_input, lengths, targets, predictions_tf, cross_entropy_tf, dropout_plc, embeddings = build_network()
    print("The graph has been built.")
    f_text = open(sys.argv[1], encoding="utf-8")
    f_cap = open(sys.argv[2])

    val_text, val_lengths = data_to_tensor(
        itertools.islice(f_text, 400), ALPHABET_DICT)
    val_cap, _ = data_to_tensor(itertools.islice(f_cap, 400), TARGET_DICT)
    print("Validation data are ready.")

    bias_regex = re.compile(r'[Bb]ias')
    regularizable = [tf.reduce_sum(
        v ** 2) for v in tf.trainable_variables()
                     if bias_regex.findall(v.name)]

    l2_value = sum(v * v for v in regularizable)
    l2_cost = 1e-6 * l2_value

    cost = cross_entropy_tf + l2_cost
    optimizer = tf.train.AdamOptimizer(1e-4)
    train_op = optimizer.minimize(cost)
    print("Optimizer has been built.")

    session = tf.Session(config=tf.ConfigProto(
        intra_op_parallelism_threads=8))
    session.run(tf.initialize_all_variables())
    saver = tf.train.Saver()
    print("Session initialized.")

    embedding_plot_n = 0
    def plot_embeddings():
        nonlocal embedding_plot_n
        if embedding_plot_n < 500:
            plt.clf()
            embeddings_values = session.run(embeddings)
            tsne = TSNE(n_components=2, random_state=0)
            np.set_printoptions(suppress=True)
            tsne = TSNE(n_components=2, random_state=0)
            Y = tsne.fit_transform(embeddings_values)
            plt.scatter(Y[:, 0], Y[:, 1], s=0)
            for label, x, y in zip(ALPHABET, Y[:, 0], Y[:, 1]):
                plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')

            axes = plt.gca()
            axes.set_xlim([-200,200])
            axes.set_ylim([-200,200])

            plt.axis('off')
            plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')

            plt.savefig("embeddings_{}.png".format(embedding_plot_n))

            embedding_plot_n += 1

    plot_embeddings()
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
            [train_op, predictions_tf, cross_entropy_tf],
            feed_dict={seq_input: text_batch,
                       targets: cap_batch,
                       lengths: batch_lengths,
                       dropout_plc: 0.5})
        accuracy = evaluation(
            predictions, cap_batch, batch_lengths)
        print("batch {}:\tacc: {:.4f}\txent: {:.4f}".format(
            batch_n, accuracy, cross_entropy))

        if batch_n % 10 == 0:
            predictions, cross_entropy = session.run(
                [predictions_tf, cross_entropy_tf],
                feed_dict={seq_input: val_text,
                           targets: val_cap,
                           lengths: val_lengths,
                           dropout_plc: 1.0})
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

        if batch_n % 100 == 0:
            plot_embeddings()

    f_text.close()
    f_cap.close()

if __name__ == "__main__":
    main()
