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
The program is currently Reading in the data using the panda class. It is taking in the link that was provided on MOodle and saving it into the powerProduction variable. The data being read in is from a csv file. A csv file is a basic text file. Csv is used for storing tabular data in text form, meaning the commas are used to seperate each column and newlines are used to seperate rows. Typically, the first row in a CSV file contains the names of the columns for the data. [1]

The data is then printed out out using the head function. The head function is part of the panda library and is use dto return the n number of rows from the data, for example in this instance it is returning the first 5 lines of data.

The describe function is used to output a summary of statistics relating to the dataframe columns. It prints values such as the Mean, STD, and the IQR values.[2]

[1] Reading data using the panda library  
https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/  
  
[2] The describe function  
https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm#:~:text=The%20describe()%20function%20computes,pertaining%20to%20the%20DataFrame%20columns.&text=This%20function%20gives%20the%20mean,given%20summary%20about%20numeric%20columns.  


#### How to run the web service

```bash
$ export FLASK_APP=WebService.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```