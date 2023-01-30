from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense
from keras import models


VGG_16 = models.Sequential([
        Conv2D(input_shape=(224, 224, 3), filters=64, kernel_size=(3,3), padding='same', name='conv_layer_1'),
        Conv2D(filters=64, kernel_size=(3,3), padding='same', name='conv_layer_2'),
        MaxPooling2D((2,2), name='max_pooling_1'),
        Conv2D(filters=128, kernel_size=(3,3), padding='same', name='conv_layer_3'),
        Conv2D(filters=128, kernel_size=(3,3), padding='same', name='conv_layer_4'),
        MaxPooling2D((2,2), name='max_pooling_2'),
        Conv2D(filters=256, kernel_size=(3,3), padding='same', name='conv_layer_5'),
        Conv2D(filters=256, kernel_size=(3,3), padding='same', name='conv_layer_6'),
        Conv2D(filters=256, kernel_size=(3,3), padding='same', name='conv_layer_7'),
        MaxPooling2D((2,2), name='max_pooling_3'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_8'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_9'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_10'),
        MaxPooling2D((2,2), name='max_pooling_4'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_11'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_12'),
        Conv2D(filters=512, kernel_size=(3,3), padding='same', name='conv_layer_13'),
        MaxPooling2D((2,2), name='max_pooling_5'),
        Flatten(name="flatten_layer"),
        Dense(4096, activation='relu', name = "fc_layer_1"),
        Dense(4096, activation='relu', name = "fc_layer_2"),
        Dense(1000, activation='softmax', name = "output_layer")    
    ])

VGG_16.summary()