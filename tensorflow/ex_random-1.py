"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import tensorflow as tf

random1 = tf.random_normal([10])

with tf.Session() as sess:
    print("tf.random_normal([10])")
    print(sess.run(random1))