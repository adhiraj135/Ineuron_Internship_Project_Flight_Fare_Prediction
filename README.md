# **Flight Fare Prediction System**

## **Table of Content**

1. Introduction
2. Approach
3. User Interface
4. Deployment Link
5. Installation
6. Technology Used
7. Document



Input variables are:

1. Airline - Object
2. Date_of_Journey - Object
3. Source - Object
4. Destination - Object
5. Route - Object
6. Dep_Time - Object
7. Arrival_Time - Object
8. Duration - Object
9. Total_Stops - Object
10. Additional_Info - Object


Output variables:

11. Price - INT

## **Approach**

Data Exploration : I started exploring dataset using pandas,numpy,matplotlib and seaborn.

Data visualization : Plotted graphs to get insights about dependent and independent variables.

Feature Engineering : All The Value Are Arrange In One Range.

Model Selection I : Tested all base models to check the base accuracy.

Model Selection II : Performed Hyperparameter tuning using gridsearchCV.

Pickle File : Selected model as per best accuracy and created pickle file using Pickle .

## **Webpage & deployment :**

Created a web form that takes all the necessary inputs from user and shows output.
Deploy

## **User Interface**

The Prediction of Credit Risk Final Model Run in Local Enviornment

Main Page :

![flight1](https://github.com/adhiraj135/Ineuron_Internship_Project_Flight_Fare_Prediction/assets/107035869/731a1a86-3e53-4f0c-b019-08c3c2113301)


Result Page :

![flight](https://github.com/adhiraj135/Ineuron_Internship_Project_Flight_Fare_Prediction/assets/107035869/f37385ec-e6d7-49ca-8d0b-81342a5d3856)


## **Deployment Link**

AWS - http://flightfareapp-env.eba-ppnqypwp.us-east-2.elasticbeanstalk.com/

## **Installation**

The Code is written in Python 3.8.11. If you don't have Python installed you can find it your link here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository.

1. Create a Virtual Env with conda create "Your Env name"
2. pip install -r requirements.txt
3. Run app.py file

## **Technology Used**

1. Python
2. Sklearn
3. Pandas
4. Numpy
5. Flask
6. HTML
7. CSS
8. Cassandra
9. AWS

## **Document**

Below providing the link of all the document that are required for creating the project.

Link: https://github.com/adhiraj135/Ineuron_Internship_Project_Flight_Fare_Prediction/tree/master/documents