#-------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand Bazaru
# FILENAME: knn.py
# SPECIFICATION: a program to find the highest accuracy possible with various hyperparameters
# FOR: CS 5990- Assignment #3
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np
#defining the hyperparameter values of KNN
k_values = [i for i in range(1, 20)]
p_values = [1, 2]
w_values = ['uniform', 'distance']

#reading the training data
#reading the test data
#hint: to convert values to float while reading them -> np.array(df.values)[:,-1].astype('f')
training_df=pd.read_csv("weather_training.csv")
training_df.dropna(how="any")
y_training = np.array(training_df["Temperature (C)"])
X_training = np.array(training_df.drop(["Temperature (C)","Formatted Date"],axis=1).values)
test_df=pd.read_csv("weather_test.csv")
test_df.dropna(how="any")
y_test = test_df["Temperature (C)"]
X_test = test_df.drop(["Temperature (C)","Formatted Date"], axis=1).values
#loop over the hyperparameter values (k, p, and w) ok KNN
#--> add your Python code here
global_acc = 0
for k in k_values:
    for p in p_values:
        for w in w_values:
            
            #fitting the knn to the data
            #--> add your Python code here
            #fitting the knn to the data
            clf = KNeighborsRegressor(n_neighbors=k, p=p, weights=w)
            clf = clf.fit(X_training, y_training)

            #make the KNN prediction for each test sample and start computing its accuracy
            #hint: to iterate over two collections simultaneously, use zip()
            num_of_acc = 0
            for (x_testSample, y_testSample) in zip(X_test, y_test):
                prediction = clf.predict(np.array([x_testSample]))
                #print("prediction", prediction, "actual", y_testSample)
            #the prediction should be considered correct if the output value is [-15%,+15%] distant from the real output values.
            #to calculate the % difference between the prediction and the real output values use: 100*(|predicted_value - real_value|)/real_value))
            #--> add your Python code here
                percentage_diff = 100*(abs(prediction[0]-y_testSample)/y_testSample)
                if -15 <= percentage_diff <= 15:
                    num_of_acc = num_of_acc + 1

            local_acc = num_of_acc/len(y_test)
            #check if the calculated accuracy is higher than the previously one calculated. If so, update the highest accuracy and print it together
            #with the KNN hyperparameters. Example: "Highest KNN accuracy so far: 0.92, Parameters: k=1, p=2, w= 'uniform'"
            #--> add your Python code here
            if local_acc > global_acc:
                global_acc = local_acc
                print(f"Highest KNN accuracy so far: {global_acc}, Parameters: k={k}, p={p}, w= {w}".format(global_acc,k,p,w))





