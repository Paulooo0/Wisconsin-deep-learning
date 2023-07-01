* - - - - - Under development 
  
# Wisconsin-deep-learning
A neural network model, that will classificate if a tumor is benign or malignant. Using area, radius, texture, smothness and other parameters to do the prediction.

# Summary
* [The neural network classifier](#the-neural-network-classifier)
* [Page](#page)
* [What was used](#what-was-used)
* [How run?](#how-run)

## The neural network classifier
The model has 30 neurons in the first layer, 10 in second layer and 1 in last layer. Approximately a accuracy of `92%`, can be checked in the arquive `check_model.py`.
This model choices between `benign` or `malignant` (0 or 1) based on established condictions found in `app.py`.

## Page
In the page I preset a few parameters, for demonstrative purposes. I recommend to try others parameters finded in the dataset or generate your own parameters.
Has a script to do the result change the color, `Benign = green` and `Malignant = red`. The form is in a container, it's a little prettier than scolling down the page.

## What was used
- Python
- Tensorflow
- Flask
- Html and CSS

## How torun?
In your terminal or console, run `git clone https://github.com/Paulooo0/Wisconsin-deep-learning`, open the folder and run `python app.py`. The flask application will start, and you will be able to open the application in your browser with `http://localhost:5000` (the port link will be printed). Now you can use the application, type your parameters and press `submit`.
