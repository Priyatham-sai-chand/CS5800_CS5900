# -------------------------------------------------------------------------
# AUTHOR: Priyatham Sai Chand Bazaru 
# FILENAME: similarity
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
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
print(cos_mat)
# finding the 5th highest after the 4 1s hence 5
idx = np.argsort(cos_mat.ravel())[-5:][::-1]
topN_val = cos_mat.ravel()[idx]
row_col = np.c_[np.unravel_index(idx, cos_mat.shape)]
row_col = row_col[4]
"""
the next highest value after 1s.
and adding 1 to index numbers to get the document numbers.
"""
print("\n")
print("doc"+str(row_col[1] + 1) + " and " + "doc"+ str(row_col[0] + 1) + " with cosine similarity = " + str(cos_mat[row_col[0]][row_col[1]])) 
