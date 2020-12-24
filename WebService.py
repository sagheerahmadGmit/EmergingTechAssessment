#Adapted from https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}