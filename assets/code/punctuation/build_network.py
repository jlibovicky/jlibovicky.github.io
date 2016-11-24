import tensorflow as tf

ALPHABET = list(("_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                 "0123456789\"'?!.% #@$(){}[]- "))
TARGET_CLASSES = ["_", ",", ";"]

def build_network(max_lenght=300, embedding_size=32, gru_size=256):
    seq_input = tf.placeholder(tf.int32, shape=[None, max_lenght])
    lengths = tf.placeholder(tf.int64, shape=[None])
    dropout_plc = tf.placeholder(tf.float32)

    embeddings = tf.get_variable(
        "embeddings", shape=[len(ALPHABET), embedding_size])

    embedded_sequence = tf.nn.embedding_lookup(embeddings, seq_input)
    embedded_sequence_dropped = tf.nn.dropout(embedded_sequence, dropout_plc)

    (output_fw, output_bw), _ = tf.nn.bidirectional_dynamic_rnn(
        tf.nn.rnn_cell.GRUCell(gru_size),
        tf.nn.rnn_cell.GRUCell(gru_size),
        embedded_sequence_dropped,
        dtype=tf.float32,
        sequence_length=lengths
    )

    with tf.variable_scope("punct_classifier"):
        output = tf.concat(2, [output_fw, output_bw])
        weight_matrix = tf.get_variable("W", shape=[2 * gru_size, len(TARGET_CLASSES)])
        bias = tf.get_variable("b", shape=[len(TARGET_CLASSES)])
        outputs_reshapes = tf.reshape(output, shape=[-1, 2 * gru_size])
        outputs_reshapes_dropped = tf.nn.dropout(outputs_reshapes, dropout_plc)
        logits = tf.matmul(outputs_reshapes_dropped, weight_matrix) + bias

        targets = tf.placeholder(tf.int32, shape=[None, max_lenght])

        cost = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits, tf.reshape(targets, shape=[-1])))

        predictions = tf.reshape(
            logits, shape=[-1, max_lenght, len(TARGET_CLASSES)])

    with tf.variable_scope("fw_language_model"):
        fw_lm_weight_matrix = tf.get_variable("W", shape=[gru_size, len(ALPHABET)])
        fw_lm_bias = tf.get_variable("b", shape=[len(ALPHABET)])

        reshaped_fw_outputs = tf.reshape(output_fw[:,:-1,:], shape=[-1, gru_size])
        fw_lm_logits = tf.matmul(reshaped_fw_outputs, fw_lm_weight_matrix) + fw_lm_bias

        cost += tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
            fw_lm_logits, tf.reshape(seq_input[:,1:], shape=[-1])))


    with tf.variable_scope("bw_language_model"):
        bw_lm_weight_matrix = tf.get_variable("W", shape=[gru_size, len(ALPHABET)])
        bw_lm_bias = tf.get_variable("b", shape=[len(ALPHABET)])

        reshaped_bw_outputs = tf.reshape(output_fw[:,1:,:], shape=[-1, gru_size])
        fw_lm_logits = tf.matmul(reshaped_fw_outputs, fw_lm_weight_matrix) + fw_lm_bias

        cost += tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
            fw_lm_logits, tf.reshape(seq_input[:,:-1], shape=[-1])))

    return seq_input, lengths, targets, predictions, cost, dropout_plc
