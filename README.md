# EmergingTechAssessment

<hr>
This is my solution to the assessment that I must complete for the 2020 Emerging Technology module. My name is Sagheer Ahmad  (G00357770@gmit.ie).

The aim of this project is to: 

```
    1. Jupyter notebook that trains a model using the data set. In the notebook you
       should explain your model and give an analysis of its accuracy.
    2. Python script that runs a web service based on the model, as above.
    3. Dockerfile to build and run the web service in a container.
    4. Standard items in a git repository such as a README.
```

<hr>
# Part One
***
The first part of the project was to create a jupyter notebook that reads in the data using the panda class. It is taking in the link that was provided on moodle and saving it into the powerProduction variable. The data being read in is from a csv file. A csv file is a basic text file. Csv is used for storing tabular data in text form, meaning the commas are used to seperate each column and newlines are used to seperate rows. Typically, the first row in a CSV file contains the names of the columns for the data. [1]

The data is then being printed onto a graph. After outputting the data i created two models using keras to predict the power of the wind depending on the wind speed. The first model was not very accurate and had a big loss so i had to remake the model with a better accuracy and loss. 

To do this i added a few more layers and gave an activation layer of sigmoid because the dataset resembled a sigmoid function. I also messed around with the epochs and batch size values to get the most accurate results.

The notebook then prints out the data and the predictions made by the data onto a graph to give us a better understanding of the accuracy of the predictions. The second model was more accurate and gave a better loss so i decided to use this model.

The next step was to save the model into a h5 file so that it can be read into a web service so that the user can input a speed and get an accurate prediction back. After saving the model i started to work on the web service.

There is more research and information about this aspect of the project in the jupyter notebook itself.


<hr>
# Part Two
***
The second part of this project was to create a flask web service that could read in a speed variable and give a power output based on the predictions made by the model. To do this I created an index file which allows the user to input the speed. I went for a minimalistic look and used some css to make the page look nice.

After creating the index page i started working in the python file that would read in the h5 file that we created in the jupyter notebook. After reading in the file. The model could make the predictions. I had a few errors with this part where the model could not send the data back to the user due to it being the wrong format. In order to fix this i used the flatten function to change the array from a 2d to a 1d array.

The data is being read in using json and is sent using javascript. The data is first turned into a string and then sent to the python file to be used for the prediction. The prediction is being read in using javascript is well and, a fetch response.

# Part Three
***
This third part of this project was to set up docker. Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating system kernel and therefore use fewer resources than virtual machines.

We  created a docker image to run the project. The image was created using a Dockerfile that runs the app. The image is ran inside a container. The container can be running in the background and does not take space in cmder so the user does not need to exit the flask run function to run the notebook. It can also be accessed anytime and the user does not need to rerun the flask app every time they load up the project.

The docker also runs a requirements.txt file to make sure the user has all the necessary downloads to run the project and makes sure the environment is set up properly.

#### How to run the web service

The project should be ran using docker for best performance.

In order to run the project we need to build a docker image: 

```
docker build -t web-service .
```
We can view the Image by using:

```
docker images ls
```

To run the image, we need to use the following commambd:

```
docker run -d -p 5000:5000 web-service
```

If you dont want to to use docker to run the app then you can run the app by using the following commands based on your operating system:

Linux System:
```bash
$ export FLASK_APP=WebService.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```
 
 Windows System:
 ```bash
$ set FLASK_APP=WebService.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 ```