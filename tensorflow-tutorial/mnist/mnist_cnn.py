#!/usr/bin/env python
# coding=utf-8


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import input_data

import tensorflow as tf

NUM_CLASSES = 10

IMAGE_SIZE = 28
IMAGE_PIXELS = IMAGE_SIZE * IMAGE_SIZE


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return initial

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')


def train(x, y_, mnist):
    
    x_image = tf.reshape(x, [-1, IMAGE_SIZE, IMAGE_SIZE, 1])

    # hidden 1 layer
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    # hidden 2 layer
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # full connect layer
    W_fc1 = weight_variable([7*7*64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
   
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_))

    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_pred = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        
        for i in range(20000):
            batch = mnist.train.next_batch(50)
            sess.run(train_step, feed_dict={x: batch[0], y_:batch[1], keep_prob:0.5})
            if i % 200 == 0:
                train_accuracy = sess.run(accuracy, feed_dict={x:batch[0], y_:batch[1], keep_prob:0.5})
                print('step %d: training accuracy: %g ' %(i, train_accuracy))

        test_accuracy = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob:0.5})
        print("test accuracy: %g" % test_accuracy)




if __name__ == "__main__":

    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    mnist = input_data.read_data_sets('/home/jkmiao/workspace/data', one_hot=True)

    train(x, y_, mnist)

