# necessary imports
# keras imports to split the dataset for training and testing
import tensorflow as tf
from flask import Flask, request  # flask imports
import json

# create a flask apps
app = Flask(__name__)

@app.route('/')
def home_page():
    # load in the index home page
    return app.send_static_file('index.html')

@app.route('/calculate/turbine/power', methods=['POST'])
def parse_request():
    jon = json.loads(request.data)
    # get the speed input from the user
    convertSpeedFloat = float(jon['speed'])
    # load in the data from the model that was saved from the jupyter notebook
    model = tf.keras.models.load_model('SavedModelData.h5')
    # predict the power value using the model
    prediction = model.predict([convertSpeedFloat])
    # turn 2d array into 1d array for predictions
    flattenPrediction = prediction.flatten()
    # return the value as a string
    return str(flattenPrediction[0])

if __name__ == '__main__':
    app.run(debug=True)