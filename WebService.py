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
from tensorflow.keras.optimizers import SGD,Adam
from tensorflow.python.keras.models import Model
from flask import Flask
from flask import request

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/calculate/', methods=["POST"])
def power():
    model = tf.keras.models.load_model('SavedModelData.h5')
    wSpeed = request.get_json()
    prediction = model.predict(wSpeed)
    #convert to a list and get the first index
    prediction = json.loads(prediction)
    prediction = [ prediction[0] ] 
    return render_template('index.html', embed=prediction)
    
if __name__ == '__main__':
    app.run(debug=True)