#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

from __future__ import print_function

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print("Training time: {:.1f}s".format(time() - t0))

t0 = time()
predictions = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)
print("Prediction time: {:.1f}s".format(time() - t0))

print("Accuracy: {:.3f}".format(accuracy))

#########################################################


