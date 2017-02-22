"""Network definition."""

from collections import namedtuple
import tensorflow as tf

ALPHABET = list(("_aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxzž"
                 "0123456789\"'?!.,% #@$(){}[]- "))
TARGET_CLASSES = ["0", "1", "2"]

Network = namedtuple('Network',
                     ['input', 'lengths', 'targets',
                      'predictions', 'cost'])

def build_network(embedding_size=32, gru_size=256):
    """RNN architecture for guessing y/i."""
    seq_input = tf.placeholder(tf.int32, shape=[None, None])
    lengths = tf.placeholder(tf.int32, shape=[None])
    targets = tf.placeholder(tf.int32, shape=[None, None])

    embeddings = tf.get_variable(
        "embeddings", shape=[len(ALPHABET), embedding_size])

    embedded_sequence = tf.nn.embedding_lookup(embeddings, seq_input)
    rnn_output = _bidirectional_layer(embedded_sequence, lengths, gru_size)

    logits_flatten, predictions = _classifier(rnn_output, 2 * gru_size, lengths)

    cost = _cost_function(logits_flatten, targets)



    return Network(seq_input, lengths, targets, predictions, cost)

def _bidirectional_layer(embedded_sequence, lengths, gru_size):
    with tf.variable_scope("bidi_layer"):
        (output_fw, output_bw), _ = tf.nn.bidirectional_dynamic_rnn(
            tf.nn.rnn_cell.GRUCell(gru_size),
            tf.nn.rnn_cell.GRUCell(gru_size),
            embedded_sequence,
            dtype=tf.float32,
            sequence_length=lengths
        )
        rnn_output = tf.concat(2, [output_fw, output_bw])
    return rnn_output


def _classifier(rnn_output, rnn_out_size, lengths):
    with tf.variable_scope("Classifier"):
        weight_matrix = tf.get_variable(
            "W", shape=[rnn_out_size, len(TARGET_CLASSES)])
        bias = tf.get_variable("b", shape=[len(TARGET_CLASSES)])
        outputs_reshaped = tf.reshape(rnn_output, shape=[-1, rnn_out_size])
        logits_flatten = tf.matmul(outputs_reshaped, weight_matrix) + bias

        predictions = tf.reshape(
            logits_flatten, shape=[-1, tf.reduce_max(lengths), len(TARGET_CLASSES)])

    return logits_flatten, predictions

def _cost_function(logits_flatten, targets):
    with tf.variable_scope("Cost"):
        targets_flatten = tf.reshape(targets, shape=[-1])

        relevance_mask = tf.cast(tf.greater(targets_flatten, 0), tf.float32)

        xent_per_char = tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits_flatten, targets_flatten)

        cost = tf.reduce_sum(xent_per_char * relevance_mask) / \
            tf.reduce_sum(relevance_mask)

    return cost
