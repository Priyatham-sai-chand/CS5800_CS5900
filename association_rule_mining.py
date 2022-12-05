#-------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990- Assignment #5
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

#Use the command: "pip install mlxtend" on your terminal to install the mlxtend library

#read the dataset using pandas
df = pd.read_csv('retail_dataset.csv', sep=',')

#find the unique items all over the data an store them in the set below
itemset = set()
for i in range(0, len(df.columns)):
    items = (df[str(i)].unique())
    itemset = itemset.union(set(items))

#remove nan (empty) values by using:
itemset.remove(np.nan)

print("itemset\n")
print(itemset)
print("itemset\n")
print(df)

#To make use of the apriori module given by mlxtend library, we need to convert the dataset accordingly. Apriori module requires a
# dataframe that has either 0 and 1 or True and False as data.
#Example:

#Bread Wine Eggs
#1     0    1
#0     1    1
#1     1    1

#To do that, create a dictionary (labels) for each transaction, store the corresponding values for each item (e.g., {'Bread': 0, 'Milk': 1}) in that transaction,
#and when is completed, append the dictionary to the list encoded_vals below (this is done for each transaction)
#-->add your python code below
label = {k: v for v, k in enumerate(itemset)}
print("label " + str(label))
encoded_vals = []
for index, row in df.iterrows():

    labels = {}
    for item in itemset:
        if item in row.values:
            labels[item] = 1
            #label = {k:1 for v,k in enumerate(itemset)}
        else:
            labels[item] = 0
    #labels = {k:v for v,k in enumerate(itemset)}

    #rower = row.str.get_dummies()
    #row_dict = rower.to_dict()
    #inv_map = {v: k for k, v in row_dict.items()}
    print("\n row type " + str(labels))
    encoded_vals.append(labels)

#adding the populated list with multiple dictionaries to a data frame
ohe_df = pd.DataFrame(encoded_vals)
print("\n dataset")
print(ohe_df)

#calling the apriori algorithm informing some parameters
freq_items = apriori(ohe_df, min_support=0.2, use_colnames=True, verbose=1)
rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

#iterate the rules data frame and print the apriori algorithm results by using the following format:
for index, rule in rules.iterrows():
    print(','.join(list(rule.antecedents))+" -> "+','.join(list(rule.consequents)))
    print("Support:"+str(rule.support))
    print("Confidence:"+str(rule.confidence))
    #supportCount = calcSupportCount(list(rule.antecedents), df)
    #prior = supportCount/len(encoded_vals)
    #print("Prior:"+str(prior))
    #print("Gain in Confidence: " + str(100*(rule.confidence-prior)/prior))
#Meat, Cheese -> Eggs
#Support: 0.21587301587301588
#Confidence: 0.6666666666666666
#Prior: 0.4380952380952381
#Gain in Confidence: 52.17391304347825
#-->add your python code below

#To calculate the prior and gain in confidence, find in how many transactions the consequent of the rule appears (the supporCount below). Then,
#use the gain formula provided right after.
#prior = suportCount/len(encoded_vals) -> encoded_vals is the number of transactions
#print("Gain in Confidence: " + str(100*(rule_confidence-prior)/prior))
#-->add your python code below
print("\n" +  str(rules.keys))

#Finally, plot support x confidence
plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
plt.xlabel('support')
plt.ylabel('confidence')
plt.title('Support vs Confidence')
plt.show()
