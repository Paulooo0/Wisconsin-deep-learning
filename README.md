
<h1 align="center">BC Wisconsing | deep learning</h1>

A neural network model, that will classificate if a tumor is benign or malignant. Using area, radius, texture, smothness and other parameters to do the prediction.

# Summary
* [The neural network classifier](#the-neural-network-classifier)
* [Page](#page)
* [What was used](#what-was-used)
* [How to run?](#how-to-run)

## The neural network classifier
The model has 30 neurons in the first layer, 10 in second layer and 1 in last layer. Approximately a accuracy of `92%`, can be checked in the arquive `check_model.py`.
This model choices between `benign` or `malignant` (0 or 1) based on established condictions found in `app.py`.

## Page
In the page I preset a few parameters, for demonstrative purposes. I recommend to try others parameters finded in the dataset or generate your own parameters.
Has a script to do the result change the color, `Benign = green` and `Malignant = red`. The form is in a container, it's a little prettier than scolling down the page.

## What was used
<img src="https://github.com/Paulooo0/Wisconsin-deep-learning/assets/110143071/5242afd9-f23e-4afc-a0c6-d71d33ef3ae1" width="100" height="100" alt="Python">
<img src="https://github.com/Paulooo0/Wisconsin-deep-learning/assets/110143071/c5f2acd2-2a24-456c-b55f-1ceaeb6ad6ff" width="100" height="100" alt="Tensorflow">
<img src="https://github.com/Paulooo0/Wisconsin-deep-learning/assets/110143071/8aa018ed-2aca-4ad6-a7ed-35ec5da92562" width="100" height="100" alt="Flask">

- [Python](https://www.python.org)
- [Tensorflow](www.tensorflow.org)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)

To create the model and deploy was used these technologies. Desconsidering the page that was used HTML, CSS and Javascript.

## How to run?
In your terminal or console, run `git clone https://github.com/Paulooo0/Wisconsin-deep-learning`, then run `app.py`. All dependencies will be installed automatically, and `localhost:5000` will be opened in your main browser. So you finally can use the application.
