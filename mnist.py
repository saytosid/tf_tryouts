import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("/tmp/data/",one_hot=True)

n_nodes_hl1 = 10
n_nodes_hl2 = 10
n_nodes_hl3 = 10

n_classes = 10
batch_size = 100

# x -> input, y -> output
x = tf.placeholder('float',(None,784))  
#shape is optional, but its good to have. If something of other shape comes it will throw exception
y = tf.placeholder('float')

def neural_network_model(data):
    # self explanatory
    hidden_1_layer = {
        'weights':tf.Variable(tf.random_normal((784, n_nodes_hl1))),
        'biases':tf.Variable(tf.random_normal(n_nodes_hl1)),
    }

    hidden_2_layer = {
        'weights':tf.Variable(tf.random_normal((n_nodes_hl1, n_nodes_hl2))),
        'biases':tf.Variable(tf.random_normal(n_nodes_hl2)),
    }

    hidden_3_layer = {
        'weights':tf.Variable(tf.random_normal((n_nodes_hl2, n_nodes_hl2))),
        'biases':tf.Variable(tf.random_normal(n_nodes_hl3)),
    }

    output_layer = {
        'weights':tf.Variable(tf.random_normal((n_nodes_hl3, n_classes))),
        'biases':tf.Variable(tf.random_normal(n_classes)),
    }

    # (input_data * weights) + biases

    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']) + hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']) + hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l1 = tf.add(tf.matmul(l2,hidden_3_layer['weights']) + hidden_3_layer['biases'])
    l1 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output

