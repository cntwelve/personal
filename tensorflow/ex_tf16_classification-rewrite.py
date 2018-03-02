# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
需要注意，在读取数据的时候，不能用one-hot
需要定义label的类型
另外，需要定义feature_column的shape
"""
from __future__ import print_function

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

def main(argv):
    def load_data():
        """get mnist data"""
        return input_data.read_data_sets('MNIST-data')

    # Build the training input_fn.
    def input_train():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"images": mnist.train.images}, mnist.train.labels.astype(np.int32))).shuffle(60000).batch(100)
            # Repeat forever
            # .repeat() #.make_one_shot_iterator().get_next()
            )

    def input_test():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"images": mnist.test.images}, mnist.test.labels.astype(np.int32))).shuffle(10000).batch(100)
            # Repeat forever
            # .repeat(3)
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

    # Fetch the data
    mnist = load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = [tf.feature_column.numeric_column(key="images", shape=[28, 28]),]

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # One hidden layers of 10 nodes each.
        hidden_units=[10],
        n_classes=10)

    # Train the Model.
    classifier.train(
        input_fn=input_train, steps=600)

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
        # msg = ("X: {: 9.2f}, "
        #        "Prediction: ${: 9.2f}")
        # msg = msg.format(predict_x["x"][i],
        #                  prediction["predictions"][0])

    # print("    " + msg)

    # for pred_dict, expec in zip(predictions, expected):
    #     template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    #     class_id = pred_dict['class_ids'][0]
    #     probability = pred_dict['probabilities'][class_id]

    #     print(template.format(iris_data.SPECIES[class_id],
    #                           100 * probability, expec))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)

