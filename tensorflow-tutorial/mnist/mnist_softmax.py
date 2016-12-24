#!/usr/bin/env python
# coding=utf-8

import argparse
import sys
import tensorflow as tf
import input_data


FLAGS = None

def main(_):

    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # create the model
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b

    # define the loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 10])
    
    cross_entroy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entroy)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        
        for i in range(10000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(train_step, feed_dict={x:batch_xs, y_: batch_ys})

            if i % 200 == 0:
                # test trained model
                print('step: %d' % i)
                correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
                accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
                print(sess.run(accuracy, feed_dict={
                    x: mnist.test.images,
                    y_: mnist.test.labels
                }))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/home/jkmiao/workspace/data', help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
