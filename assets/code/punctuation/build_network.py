import tensorflow as tf

ALPHABET = list(("_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                 "0123456789\"'?!.,% #@$(){}[]- "))
TARGET_CLASSES = ["0", "1", "2"]


def build_network(embedding_size=32, gru_size=256):
    """RNN architecture for punctuation filling."""
    seq_input = tf.placeholder(tf.int32, shape=[None, None])
    lengths = tf.placeholder(tf.int32, shape=[None])
    dropout_plc = tf.placeholder(tf.float32)

    embeddings = tf.get_variable(
        "embeddings", shape=[len(ALPHABET), embedding_size])

    embedded_sequence = tf.nn.embedding_lookup(embeddings, seq_input)
    embedded_sequence_dropped = tf.nn.dropout(embedded_sequence, dropout_plc)

    with tf.variable_scope("bidi_layer"):
        (output_fw, output_bw), _ = tf.nn.bidirectional_dynamic_rnn(
            tf.nn.rnn_cell.GRUCell(gru_size),
            tf.nn.rnn_cell.GRUCell(gru_size),
            embedded_sequence_dropped,
            dtype=tf.float32,
            sequence_length=lengths
        )
        output_bidi = tf.concat(2, [output_fw, output_bw])

    output = output_bidi
    output_size = 2 * gru_size

    with tf.variable_scope("classifier"):
        weight_matrix = tf.get_variable(
            "W", shape=[output_size, len(TARGET_CLASSES)])
        bias = tf.get_variable("b", shape=[len(TARGET_CLASSES)])
        outputs_reshapes = tf.reshape(output, shape=[-1, output_size])
        outputs_reshapes_dropped = tf.nn.dropout(outputs_reshapes, dropout_plc)
        logits_flatten = tf.matmul(
            outputs_reshapes_dropped, weight_matrix) + bias

    with tf.variable_scope("cost"):
        targets = tf.placeholder(tf.int32, shape=[None, None])
        targets_flatten = tf.reshape(targets, shape=[-1])

        relevance_mask = tf.cast(tf.greater(targets_flatten, 0), tf.float32)

        xent_per_char = tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits_flatten, targets_flatten)

        cost = tf.reduce_sum(xent_per_char * relevance_mask) / \
            tf.reduce_sum(relevance_mask)

        predictions = tf.reshape(
            logits_flatten, shape=[-1, tf.reduce_max(lengths), len(TARGET_CLASSES)])

    return seq_input, lengths, targets, predictions, cost, dropout_plc
