# %%
# Hide log information
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# import tensorflow
import tensorflow as tf

# %%
# load mnist dataset
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# scale or normalize the datasets
training_images=training_images/255.0
test_images=test_images/255.0

training_images.shape, test_images.shape

# %%
# create model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),            # 28 * 28 => (784,1)
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(64, activation=tf.nn.relu),
  tf.keras.layers.Dense(32, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.build(input_shape=(1, 28,28))
model.summary()

# %%
# compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# %%
# fit model
history = model.fit(training_images, training_labels, epochs=10)

# %%
# evaluate model
out = model.evaluate(test_images, test_labels)

# %%
model.summary()

# %%
print("Model Accuracy: {}".format(out[1]))
print("Model Loss:     {}".format(out[0]))

# %%
history.history.keys()

# %%
import matplotlib.pyplot as plt

loss_values = history.history['loss']
accuracy_values = history.history['accuracy']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(loss_values)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.set_title('Loss over time')

ax2.plot(accuracy_values)
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Accuracy')
ax2.set_title('Accuracy over time')

plt.show()


# %%
model.weights


