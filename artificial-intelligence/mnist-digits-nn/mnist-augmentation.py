import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape the images to have a single channel
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

# Convert the image data to float32 and normalize the pixel values
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Create a data generator for data augmentation
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=20,      # Rotate the images by up to 20 degrees
    width_shift_range=0.1,  # Shift the images horizontally by up to 10%
    height_shift_range=0.1, # Shift the images vertically by up to 10%
    zoom_range=0.1,         # Zoom in on the images by up to 10%
    shear_range=0.1,        # Shear the images by up to 10%
    fill_mode='nearest'     # Fill in missing pixels with the nearest value
)

# Fit the data generator to the training data
datagen.fit(train_images)

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model using the augmented data
history = model.fit(datagen.flow(train_images, train_labels, batch_size=32),
                    steps_per_epoch=len(train_images) / 32,
                    epochs=10,
                    validation_data=(test_images, test_labels))

