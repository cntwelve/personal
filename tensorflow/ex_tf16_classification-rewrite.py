# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def main(argv):
    def load_data():
        """get mnist data"""
        return input_data.read_data_sets('MNIST_data', one_hot=True)

    # Build the training input_fn.
    def input_train():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"images": mnist.train.images}, mnist.train.labels)).shuffle(60000).batch(100)
            # Repeat forever
            # .repeat() #.make_one_shot_iterator().get_next()
            )

    def input_test():
        return (
            # Shuffling with a buffer larger than the data set ensures
            # that the examples are well mixed.
            tf.data.Dataset.from_tensor_slices(({"images": mnist.test.images}, mnist.test.labels)).shuffle(10000).batch(100)
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
    my_feature_columns = [tf.feature_column.numeric_column(key="images"),]

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # One hidden layers of 10 nodes each.
        hidden_units=[10],
        n_classes=10,
        )

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

# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def add_layer(inputs, in_size, out_size, activation_function=None,):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1,)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b,)
    return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 784]) # 28x28
ys = tf.placeholder(tf.float32, [None, 10])

# add output layer
prediction = add_layer(xs, 784, 10,  activation_function=tf.nn.softmax)

# the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))       # loss
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
# important step
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 50 == 0:
        print(compute_accuracy(
            mnist.test.images, mnist.test.labels))

