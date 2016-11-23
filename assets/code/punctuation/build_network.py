import tensorflow as tf

TARGET_CLASSES = ["_", ",", ";"]


def build_network(alphabet, max_lenght=200, embedding_size=15, gru_size=64):
    seq_input = tf.placeholder(tf.int32, shape=[None, max_lenght])

    embeddings = tf.get_variable(
        "embeddings", shape=[len(alphabet), embedding_size])

    embedded_sequence = tf.nn.embedding_lookup(embeddings, seq_input)

    output, _ = tf.nn.dynamic_rnn(
        tf.nn.rnn_cell.GRUCell(gru_size),
        embedded_sequence,
        dtype=tf.float32
    )

    weight_matrix = tf.get_variable("W", shape=[gru_size, len(TARGET_CLASSES)])
    bias = tf.get_variable("b", shape=[len(TARGET_CLASSES)])
    logits = tf.matmul(tf.reshape(
        output, shape=[-1, gru_size]), weight_matrix) + bias

    targets = tf.placeholder(tf.int32, shape=[None, max_lenght])

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits, tf.reshape(targets, shape=[-1]))

    predictions = tf.reshape(
        logits, shape=[-1, max_lenght, len(TARGET_CLASSES)])

    return seq_input, targets, predictions, cross_entropy
