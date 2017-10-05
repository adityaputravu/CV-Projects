import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

from keras import backend as K

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

mnist = input_data.read_data_sets("/Users/aditya/Desktop/Pycharm/MachineLearning/SentDex/NeuralNetwork", one_hot=True)

# 10 classes, 0-9 handwritten
'''
Output as 
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
and so on
'''

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100  # Batches of 100 imgs at a time


# Height x Width ---> vector squashed to one line (0,1,0....)
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')


def neural_network_model(data):
    # (input_data * weights) + biases
    # 1: K.variable -> Random values -> shape
    # hidden_1_layer = {'weights': K.variable(tf.random_normal([784, n_nodes_hl1])),
    #                   'biases': K.variable(tf.random_normal([n_nodes_hl1]))}
    #
    # hidden_2_layer = {'weights': K.variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
    #                   'biases': K.variable(tf.random_normal([n_nodes_hl2]))}
    #
    # hidden_3_layer = {'weights': K.variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
    #                   'biases': K.variable(tf.random_normal([n_nodes_hl3 ]))}
    #
    # output_layer = {'weights': K.variable(tf.random_normal([n_nodes_hl3, n_classes])),
    #                   'biases': K.variable(tf.random_normal([n_classes]))}


    # Produces better accuracy
    # Smaller initial values making training smoother
    hidden_1_layer = {'weights': K.variable(K.truncated_normal([784, n_nodes_hl1], stddev=0.1)),
                      'biases': K.variable(K.constant(0.1, shape=[n_nodes_hl1]))}

    hidden_2_layer = {'weights': K.variable(K.truncated_normal([n_nodes_hl1, n_nodes_hl2], stddev=0.1)),
                      'biases': K.variable(K.constant(0.1, shape=[n_nodes_hl2]))}

    hidden_3_layer = {'weights': K.variable(K.truncated_normal([n_nodes_hl2, n_nodes_hl3], stddev=0.1)),
                      'biases': K.variable(K.constant(0.1, shape=[n_nodes_hl3]))}

    output_layer = {'weights': K.variable(K.truncated_normal([n_nodes_hl3, n_classes], stddev=0.1)),
                      'biases': K.variable(K.constant(0.1, shape=[n_classes]))}


    # (input_data * weights) + biases
    # Matmul is matrix multiplication

    l1 = tf.add(K.dot(data, hidden_1_layer['weights']) , hidden_1_layer['biases'])
    # Passes through activation function
    # Official definiton: Computes rectified linear and returns a Tensor
    l1 = tf.nn.relu(l1)

    #                 input data
    #                     √
    l2 = tf.add(K.dot(l1, hidden_2_layer['weights']) , hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(K.dot(l2, hidden_3_layer['weights']) , hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = K.dot(l3, output_layer['weights']) + output_layer['biases']

    return output

def train_neural_network(X):
    prediction = neural_network_model(X)
    # Cost function -- how good it did with respect to it's given training sample and the expected output
    # Using cross entropy with logits and labels
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    # Want to minimise cost
    #                                                 , learningrate = 0.001
    optimiser = tf.train.AdamOptimizer().minimize(cost )  # lel

    # Cycles of feedforward and backprops
    howmany_epochs = 10

    with tf.Session() as sess:
        K.set_session(sess)

        # initialises variables
        sess.run(tf.global_variables_initializer())

        correct = K.equal(K.argmax(prediction, 1), K.argmax(y, 1))


        accuracy = tf.reduce_mean(K.cast(correct, 'float'))
        acc_eval = accuracy.eval({x:mnist.test.images, y:mnist.test.labels})

        # Evaluate all accuracies test images to labels
        print('Accuracy:', acc_eval)
        # Training
        for epoch in range(howmany_epochs):
            epoch_loss = 0
            # How many times we need to cycle
            for _ in range(int(mnist.train.num_examples/batch_size)):
                # Chunks through datasize
                X, Y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimiser, cost], feed_dict={x: X, y: Y})

                epoch_loss += c
            # To know how much longer to wait
            print("Epoch:", epoch+1, "completed out of", howmany_epochs, "Loss:", epoch_loss)

            # correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
            #
            # accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
            # acc_eval = accuracy.eval({x:mnist.test.images, y:mnist.test.labels})
            # # Evaluate all accuracies test images to labels
            # print('Accuracy:', acc_eval)




        # tf.argmax returns index of max value and hoping these are identical
        correct = K.equal(K.argmax(prediction, 1), K.argmax(y, 1))

        accuracy = tf.reduce_mean(K.cast(correct, 'float'))
        # Evaluate all accuracies test images to labels
        print('Accuracy:', accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))


train_neural_network(x)