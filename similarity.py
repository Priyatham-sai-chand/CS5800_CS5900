# -------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand Bazaru 
# FILENAME: similarity
# SPECIFICATION: calculate the cosine similarity between various documents and print the most similar documents.
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from numpy import unravel_index
count_vectorizer = CountVectorizer()

# Defining the documents
doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "I support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document matrix
# [soccer, my, favorite, sport, I, like, one, support, olympic, game]
# --> Add your Python code here

# the word list adjusted for soccer and games word
word_list = ["soccer", "my", "favorite", "sport", "I", "like", "one", "support", "olympic", "games"]

# spliting the sentences into words to be compared with the document matrix
doc_full_list=[doc1,doc2,doc3,doc4]
doc_list = [doc1.split(" "),doc2.split(" "),doc3.split(" "),doc4.split(" ")]
# define the list to hold the occurance matrix
doc_one = [[],[],[],[]]

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
# --> Add your Python code here

#  add 1 if the word is present in the sentence else add 0
for word in word_list:
    for i in range(len(doc_list)):
        if word in doc_list[i]: doc_one[i].append(1)
        else: doc_one[i].append(0)


# Print the highest cosine similarity following the template below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here

cos_mat = cosine_similarity(doc_one,doc_one)
print("cosine similarity matrix of doc1 to doc4\n")
cos_mat = np.round(cos_mat,5)
print(cos_mat)

# initalize variables to store the highest value and it's indexes
high_similarity = 0
high_idxs = [0,0]
for i in range(4):
    for j in range(4):
        if cos_mat[i][j] != 1 and cos_mat[i][j] > high_similarity:
            high_similarity = cos_mat[i][j]
            high_idxs[0] = i
            high_idxs[1] = j
print("\n")
print("The most similar documents are doc"+str(high_idxs[0] + 1) + " and " + "doc"+ str(high_idxs[1] + 1) + " with cosine similarity = " + str(high_similarity)) 
