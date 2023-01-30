from keras import layers, models

vgg16 = models.Sequential([
        layers.Conv2D(input_shape=(224, 224, 3), filters=64, kernel_size=(3,3), padding='same', name='conv2d_1'),
        layers.Conv2D(64, (3,3), padding='same', name='conv2d_2'),
        layers.MaxPooling2D((2,2), name='max_pool_1'),
        
        layers.Conv2D(128, (3,3), padding='same', name='conv2d_3'),
        layers.Conv2D(128, (3,3), padding='same', name='conv2d_4'),
        layers.MaxPooling2D((2,2), name='max_pool_2'),
        
        layers.Conv2D(256, (3,3), padding='same', name='conv2d_5'),
        layers.Conv2D(256, (3,3), padding='same', name='conv2d_6'),
        layers.Conv2D(256, (3,3), padding='same', name='conv2d_7'),
        layers.MaxPooling2D((2,2), name='max_pool_3'),
        
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_8'),
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_9'),
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_10'),
        layers.MaxPooling2D((2,2), name='max_pool_4'),
        
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_11'),
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_12'),
        layers.Conv2D(512, (3,3), padding='same', name='conv2d_13'),
        layers.MaxPooling2D((2,2), name='max_pool_5'),
        
        layers.Flatten(name="flatten_layer"),
        layers.Dense(4096, activation='relu', name = "dense_layer_1"),
        layers.Dense(4096, activation='relu', name = "dense_layer_2"),
        layers.Dense(1000, activation='softmax', name = "output_layer")    
    ])

vgg16.summary()