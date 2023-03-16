# load tensorflow
import tensorflow as tf

# load dataset
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# normalize dataset
training_images=training_images/255.0
test_images=test_images/255.0

# create model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),            
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(64, activation=tf.nn.relu),
  tf.keras.layers.Dense(32, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# build and summary model
# model.build(input_shape=(1, 28,28))
# model.summary()

# compile and fit the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=10)

# evaluate the model
out = model.evaluate(test_images, test_labels)

print(model.summary())

print("Model Accuracy: {}".format(out[1]))
print("Model Loss:     {}".format(out[0]))
