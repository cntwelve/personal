# -*- coding: utf-8 -*-

#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
结合Google的示例程序（https://github.com/tensorflow/tensorflow/tree/r1.5/tensorflow/examples/get_started/regression）
对教程中的例子（https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tf11_build_network/full_code.py）进行了重写。
在过程中，主要问题在对dataset，FeatureColumn等的理解
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')


def main(argv):
    args = parser.parse_args(argv[1:])

    def load_data():
        """Returns 自己生成的测试数据 dataset as (train_x, train_y), (test_x, test_y)."""
        train_x = np.linspace(-1, 1, 1000, dtype=np.float32) # [:, np.newaxis]
        noise = np.random.normal(0, 0.05, train_x.shape).astype(np.float32)
        train_y = np.square(train_x) - 0.5 + noise

        test_x = np.linspace(-1, 1, 300, dtype=np.float32) #[:, np.newaxis]
        noise = np.random.normal(0, 0.05, test_x.shape).astype(np.float32)
        test_y = np.square(test_x) - 0.5 + noise

        return (train_x, train_y), (test_x, test_y)

    # Build the training input_fn.
    def input_train():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"x": train_x}, train_y)).shuffle(1000).batch(128)
            # Repeat forever
            .repeat() #.make_one_shot_iterator().get_next()
            )

    def input_test():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"x": test_x}, test_y)).shuffle(300).batch(30)
            # Repeat forever
            .repeat(3)
            # .make_one_shot_iterator().get_next()
            )

    def input_predict():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"x": [0.5, -0.5, 0.3]})).batch(3)
            # Repeat forever
            .repeat(1)
            # .make_one_shot_iterator().get_next()
            )

    def input_predict_plt():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"x": test_x})).batch(300)
            )

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = load_data()

    # plot the real data
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(train_x, train_y)
    plt.ion()#本次运行请注释，全局运行不要注释
    plt.show()

    # Feature columns describe how to use the input.
    my_feature_columns = [tf.feature_column.numeric_column(key="x"),]

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNRegressor(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10])

    # Train the Model.
    classifier.train(
        input_fn=input_train, steps=10000)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=input_test)

    # print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
    print(eval_result)
    print('\nTest set accuracy: {average_loss:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    predict_x = {
        'x': [0.5, -0.5, 0.3],
    }

    # predictions = classifier.predict(
    #     input_fn=input_predict)

    # print("\nPrediction results:")
    # for i, prediction in enumerate(predictions):
    #     print(prediction["predictions"][0])

    predictions = classifier.predict(
        input_fn=input_predict_plt)

    # pl = list(classifier.predict(input_fn=input_predict_plt))
    # print(pl)

    predict_y = []
    for i, prediction in enumerate(predictions):
        predict_y.append(prediction["predictions"][0])

    try:
        ax.lines.remove(lines[0])
    except Exception:
        pass
    # plot the prediction
    lines = ax.plot(test_x, predict_y, 'r-', lw=5)
    plt.pause(10)

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
