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
"""An Example of a DNNClassifier for the Iris dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
import numpy as np


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

        test_x = np.linspace(-1, 1, 3, dtype=np.float32) #[:, np.newaxis]
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
            tf.data.Dataset.from_tensor_slices(({"x": test_x}, test_y)).shuffle(3).batch(3)
            # Repeat forever
            .repeat(3)
            # .make_one_shot_iterator().get_next()
            )


    # Fetch the data
    (train_x, train_y), (test_x, test_y) = load_data()

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

    # # Generate predictions from the model
    # expected = ['Setosa', 'Versicolor', 'Virginica']
    # predict_x = {
    #     'SepalLength': [5.1, 5.9, 6.9],
    #     'SepalWidth': [3.3, 3.0, 3.1],
    #     'PetalLength': [1.7, 4.2, 5.4],
    #     'PetalWidth': [0.5, 1.5, 2.1],
    # }

    # predictions = classifier.predict(
    #     input_fn=lambda:iris_data.eval_input_fn(predict_x,
    #                                             labels=None,
    #                                             batch_size=args.batch_size))

    # for pred_dict, expec in zip(predictions, expected):
    #     template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    #     class_id = pred_dict['class_ids'][0]
    #     probability = pred_dict['probabilities'][class_id]

    #     print(template.format(iris_data.SPECIES[class_id],
    #                           100 * probability, expec))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
