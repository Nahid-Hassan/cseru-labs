# Artificial Intelligence

**Table of Contents**:

- [Artificial Intelligence](#artificial-intelligence)
  - [Install Software and Utilities](#install-software-and-utilities)
  - [Lab - 1](#lab---1)

## Install Software and Utilities 

**System - Ubuntu**:

```bash
$ sudo apt install python3
```

## Lab - 1


## Test Classifier Snippets

```py
#to predict new images 
def predict_image(imagepath, classifier):
    predict = image.load_img(imagepath, target_size = (64, 64))   
    predict_modified = image.img_to_array(predict)
    predict_modified = predict_modified / 255
    predict_modified = np.expand_dims(predict_modified, axis = 0)
    result = classifier.predict(predict_modified)
    if result[0][0] >= 0.5:
        prediction = 'dog'
        probability = result[0][0]
        print ("probability = " + str(probability))
    else:
        prediction = 'cat'
        probability = 1 - result[0][0]
        print ("probability = " + str(probability))
        print("Prediction = " + prediction)
   ```
