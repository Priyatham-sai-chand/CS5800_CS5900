# -------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand Bazaru
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: 3 hrs
# -----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer

dataSets = ['cheat_training_1.csv', 'cheat_training_2.csv']

for ds in dataSets:

    X = []
    Y = []

    df = pd.read_csv("cheat_data.csv", sep=',', header=0)
    df['Taxable Income'] = df['Taxable Income'].str.replace('k','')
    df['Taxable Income'] = df['Taxable Income'].astype(float)
    df['Refund'] = df['Refund'].map(dict(Yes=1, No=0))
    df['Marital Status'] = df['Marital Status'].map(dict(Single=[1,0,0],Divorced=[0,1,0],Married=[0,0,1]))
    df['Cheat'] = df['Cheat'].map(dict(Yes=1, No=0))
    
    # Remove Cheat column
    data_training = np.array(df.values)[:,1:-1]
    print("data training\n")
    print(data_training)
    def make(row):
        row = np.insert(row,1,row[1])
        row = np.delete(row,4)
        return row
    data_training = np.apply_along_axis(make, axis=1, arr=data_training)

    #transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
    #Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
    #be converted to a float.
    
    X = data_training

    #transform the original training classes to numbers and add them to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    Y = df.Cheat

    #loop your training and test tasks 10 times here
    test_df = pd.read_csv('cheat_test.csv', sep=',', header=0)
    test_df['Taxable Income'] = test_df['Taxable Income'].str.replace('k','')
    test_df['Taxable Income'] = test_df['Taxable Income'].astype(float)
    test_df['Refund'] = test_df['Refund'].map(dict(Yes=1, No=0))
    test_df['Marital Status'] = test_df['Marital Status'].map(dict(Single=[1,0,0],Divorced=[0,1,0],Married=[0,0,1]))
    test_df['Cheat'] = test_df['Cheat'].map(dict(Yes=1, No=0))
    

    # Remove Tid column
    test_data = np.array(test_df.values)[:,1:]
    def make(row):
        row = np.insert(row,1,row[1])
        row = np.delete(row,4)
        return row
    test_data = np.apply_along_axis(make, axis=1, arr=test_data)
    accuracies = []
    for i in range (10):

        #fitting the decision tree to the data by using Gini index and no max_depth
        clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=None)
        clf = clf.fit(X, Y)

        #plotting the decision tree
        tree.plot_tree(clf, feature_names=['Refund', 'Single', 'Divorced', 'Married', 'Taxable Income'], class_names=['Yes','No'], filled=True, rounded=True)
        plt.show()

        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for data in test_data:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[1, 0, 1, 0, 115]])[0], where [0] is used to get an integer as the predicted class label so that you can compare it with the true label


           
           print(data)
           predicted_class = clf.predict([data[:-1]])[0]

           #compare the prediction with the true label (located at data[3]) of the test instance to start calculating the model accuracy.
           test_class_value = data[-1]
           
           print("test class " + str(predicted_class))
           if predicted_class == 1 and test_class_value == 1:
               tp+=1
           elif predicted_class == 1 and test_class_value == 0:
               fp+=1
           elif predicted_class == 0 and test_class_value == 1:
               fn+=1
           else:
               tn+=1
        
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        #print("ACCURACY",accuracy)
        accuracies.append(accuracy)
    print("accuracies", accuracies)
       #find the average accuracy of this model during the 10 runs (training and test set)
    avg_accuracy = np.average(accuracies)

    #print the accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on cheat_training_1.csv: 0.2
    print("average accuracy when training on "+str(ds)+":", avg_accuracy)




