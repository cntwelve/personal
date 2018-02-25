from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

dataset = tf.data.Dataset.from_tensor_slices(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))
iterator = dataset.make_one_shot_iterator()
one_element = iterator.get_next()

dataset2 = tf.data.Dataset.from_tensor_slices(
    {
        "a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),                                       
        "b": np.random.uniform(size=(5, 2))
    }
)
iterator2 = dataset2.make_one_shot_iterator()
one_element2 = iterator2.get_next()

train_x = np.linspace(-1, 1, 1000, dtype=np.float32)
noise = np.random.normal(0, 0.05, train_x.shape).astype(np.float32)
train_y = np.square(train_x) - 0.5 + noise

train_x = tf.constant(train_x)
train_y = tf.constant(train_y)

# tf.data.Dataset.from_tensor_slices((dict(train_x), train_y)).shuffle(1000).batch(128).repeat().make_one_shot_iterator().get_next()
ds = tf.data.Dataset.from_tensor_slices((train_x, train_y))
ds = ds.shuffle(1000).batch(128).repeat()
it = ds.make_one_shot_iterator().get_next()

with tf.Session() as sess:
    print("format 1:")
    for i in range(5):
        print(sess.run(one_element))
    print("format 2:")
    for i in range(5):
        print(sess.run(one_element2))
    for i in range(10):
    	print("Printing it:")
    	print(sess.run(it))
