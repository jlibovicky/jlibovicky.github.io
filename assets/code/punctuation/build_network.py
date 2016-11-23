import tensorflow as tf

ALPHABET = list(("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                 "0123456789\"'?!.% #@$(){}[]_"))
TARGET_CLASSES = ["_", ",", ";"]

def build_network(max_lenght=300, embedding_size=32, gru_size=256):
    seq_input = tf.placeholder(tf.int32, shape=[None, max_lenght])
    lengths = tf.placeholder(tf.int64, shape=[None])
    dropout_plc = tf.placeholder(tf.float32)

    embeddings = tf.get_variable(
        "embeddings", shape=[len(ALPHABET), embedding_size])

    embedded_sequence = tf.nn.embedding_lookup(embeddings, seq_input)
    embedded_sequence_dropped = tf.nn.dropout(embedded_sequence, dropout_plc)

    (output_fw, output_bg), _ = tf.nn.bidirectional_dynamic_rnn(
        tf.nn.rnn_cell.GRUCell(gru_size),
        tf.nn.rnn_cell.GRUCell(gru_size),
        embedded_sequence_dropped,
        dtype=tf.float32,
        sequence_length=lengths
    )
    output = tf.concat(2, [output_fw, output_bg])

    weight_matrix = tf.get_variable("W", shape=[2 * gru_size, len(TARGET_CLASSES)])
    bias = tf.get_variable("b", shape=[len(TARGET_CLASSES)])
    outputs_reshapes = tf.reshape(output, shape=[-1, 2 * gru_size])
    outputs_reshapes_dropped = tf.nn.dropout(outputs_reshapes, dropout_plc)
    logits = tf.matmul(outputs_reshapes_dropped, weight_matrix) + bias

    targets = tf.placeholder(tf.int32, shape=[None, max_lenght])

    cross_entropy = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits, tf.reshape(targets, shape=[-1])))

    predictions = tf.reshape(
        logits, shape=[-1, max_lenght, len(TARGET_CLASSES)])

    return seq_input, lengths, targets, predictions, cross_entropy, dropout_plc
