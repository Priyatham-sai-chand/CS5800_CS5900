#-------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand Bazaru
# FILENAME: naive_bayes.py
# SPECIFICATION: to predict weather using the naive bayes classifier
# FOR: CS 5990- Assignment #3
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np

#11 classes after discretization
classes = [i for i in range(-22, 40, 6)]

#reading the training data
#--> add your Python code here
training_df=pd.read_csv("weather_training.csv")
training_df.dropna(how="any")

def filterer(row):
    prev = -100
    for c in classes:
        if row > prev and row <= c:
            row = c
        prev = c
    return row

training_df["Temperature (C)"] =[filterer(row) for row in training_df["Temperature (C)"].to_numpy()] 

y_training = training_df["Temperature (C)"]
X_training = np.array(training_df.drop(["Temperature (C)","Formatted Date"],axis=1).values)
y_training = y_training.astype('int')
#update the training class values according to the discretization (11 values only)
#--> add your Python code here

#reading the test data
#--> add your Python code here
test_df=pd.read_csv("weather_test.csv")
test_df.dropna(how="any")


#update the test class values according to the discretization (11 values only)
#--> add your Python code here
test_df["Temperature (C)"] =[filterer(row) for row in test_df["Temperature (C)"].to_numpy()] 
y_test = test_df["Temperature (C)"]
X_test = test_df.drop(["Temperature (C)","Formatted Date"], axis=1).values
y_test = y_test.astype('int')
#fitting the naive_bayes to the data
clf = GaussianNB()
clf = clf.fit(X_training, y_training)
num_of_acc = 0
global_acc = 0
for (x_testSample, y_testSample) in zip(X_test, y_test):
    prediction = clf.predict(np.array([x_testSample]))



#make the naive_bayes prediction for each test sample and start computing its accuracy
#the prediction should be considered correct if the output value is [-15%,+15%] distant from the real output values
#to calculate the % difference between the prediction and the real output values use: 100*(|predicted_value - real_value|)/real_value))
#--> add your Python code here

    percentage_diff = 100*(abs(prediction[0]-y_testSample)/y_testSample)
    if -15 <= percentage_diff <= 15:
        num_of_acc = num_of_acc + 1
local_acc = num_of_acc/len(y_test)
#print the naive_bayes accuracyy
#--> add your Python code here
#print("naive_bayes accuracy: " + str(accuracy))
print("naive_bayes accuracy: " + str(local_acc))



