#necessary imports

# import numpy class
import numpy as np
# import panda class for handling data
import pandas as pd
# Plotting
import matplotlib.pyplot as plt
# keras imports to split the dataset for training and testing
import tensorflow as tf
# Neural networks.
import tensorflow.keras as kr
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.models import Model
from flask import Flask
from flask import request
import sys

import json
#create a flask apps
app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')#load in the index home page

@app.route('/calculate/turbine/power', methods=['POST'])
def parse_request():
    data = request.data
    jon = json.loads(data)
    #get the speed input from the user
    windSpeed = float(jon['speed'])
    #load in the data from the model that was saved from the jupyter notebook
    model = tf.keras.models.load_model('SavedModelData.h5')
    #predict the power value using the model
    prediction = model.predict([windSpeed])
    #turn 2d array into 1d array for predictions
    flatten = prediction.flatten()
    print(flatten[0])
    #return the value as a string
    return str(flatten[0])

if __name__ == '__main__':
    app.run(debug=True)