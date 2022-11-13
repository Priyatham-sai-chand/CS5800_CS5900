#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990- Assignment #4
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

dbTraining = []
dbTest = []
X_training = []
y_training = []
classVotes = [] #this array will be used to count the votes of each classifier

#reading the training data from a csv file and populate dbTraining
#--> add your Python code here
dbTraining = pd.read_csv("optdigits.tra",header=None)

#reading the test data from a csv file and populate dbTest
#--> add your Python code here
dbTest = pd.read_csv("optdigits.tes",header=None).to_numpy()
#inititalizing the class votes for each test sample. Example: classVotes.append([0,0,0,0,0,0,0,0,0,0])
#--> add your Python code here
for test_sample in dbTest:
    classVotes.append([0,0,0,0,0,0,0,0,0,0])
print("Started my base and ensemble classifier ...")

for k in range(20): #we will create 20 bootstrap samples here (k = 20). One classifier will be created for each bootstrap sample
    bootstrapSample = resample(dbTraining, n_samples=len(dbTraining), replace=True)
  #print(bootstrapSample.columns)

  #populate the values of X_training and y_training by using the bootstrapSample
  #--> add your Python code here
    X_training = bootstrapSample.iloc[:,:-1]
    y_training = bootstrapSample.iloc[:,-1]

  #fitting the decision tree to the data
    clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=None) #we will use a single decision tree without pruning it
    clf = clf.fit(X_training, y_training)
    
    for i, testSample in enumerate(dbTest):
     
        #print(testSample)
        class_predicted_tree = clf.predict(testSample[:-1].reshape(1,-1))
        print(class_predicted_tree[0])
        classVotes[i][class_predicted_tree[0]] += 1
      #print("testsample " + str(classVotes[k]))
      #make the classifier prediction for each test sample and update the corresponding index value in classVotes. For instance,
      # if your first base classifier predicted 2 for the first test sample, then classVotes[0,0,0,0,0,0,0,0,0,0] will change to classVotes[0,0,1,0,0,0,0,0,0,0].
      # Later, if your second base classifier predicted 3 for the first test sample, then classVotes[0,0,1,0,0,0,0,0,0,0] will change to classVotes[0,0,1,1,0,0,0,0,0,0]
      # Later, if your third base classifier predicted 3 for the first test sample, then classVotes[0,0,1,1,0,0,0,0,0,0] will change to classVotes[0,0,1,2,0,0,0,0,0,0]
      # this array will consolidate the votes of all classifier for all test samples
      #--> add your Python code here

        if k == 0: #for only the first base classifier, compare the prediction with the true label of the test sample here to start calculating its accuracy
         #--> add your Python code here
         if 
           print("\n")

        if k == 0: #for only the first base classifier, print its accuracy here
     #--> add your Python code here
          print("Finished my base classifier (fast but relatively low accuracy) ...")
     #print("My base classifier accuracy: " + str(accuracy))
          print("")

  #now, compare the final ensemble prediction (majority vote in classVotes) for each test sample with the ground truth label to calculate the accuracy of the ensemble classifier (all base classifiers together)
  #--> add your Python code here

  #printing the ensemble accuracy here
    print(classVotes)
    print("Finished my ensemble classifier (slow but higher accuracy) ...")
  #print("My ensemble accuracy: " + str(accuracy))
    print("")



