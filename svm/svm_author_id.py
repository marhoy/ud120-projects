#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



# Possibly reduce the set of the training set:
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

for zeros in range(4, 6):
    C = float(10**zeros)
    print("Value of C: {:,.0f}".format(C))

    clf = SVC(kernel='rbf', C=C)

    print("\tStarting SVM fitting")
    t0 = time()
    clf.fit(features_train, labels_train)
    print("\tTraining time: {:.1f}s".format(time() - t0))

    print("\tStarting SVM predictions")
    t0 = time()
    pred_train = clf.predict(features_train)
    pred_test = clf.predict(features_test)
    print("\tPrediction time: {:.1f}s".format(time() - t0))

    acc_train = accuracy_score(labels_train, pred_train)
    acc_test = accuracy_score(labels_test, pred_test)

    print("Accuracy with C={:,.0f}: Train: {:.3f}, Test: {:.3f}".format(C, acc_train, acc_test))

    items = [10, 26, 50]
    print("Predictions for items {}: {}".format(items, pred_test[items]))

    print("Emails predicted to be written by Chris: {}".format(sum(pred_test == 1)))
#########################################################
