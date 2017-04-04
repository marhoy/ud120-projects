#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


def prettyPicture(clf, X_train, y_train, X_test, y_test):
    x_min, x_max = (0.0, 1.0)
    y_min, y_max = (0.0, 1.0)
    
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

    # Plot also the training points
    grade_fast_train = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii] == 0]
    bumpy_fast_train = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii] == 0]
    grade_slow_train = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii] == 1]
    bumpy_slow_train = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii] == 1]

    # Plot also the test points
    grade_fast_test = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    bumpy_fast_test = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    grade_slow_test = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    bumpy_slow_test = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]

    plt.scatter(grade_fast_train, bumpy_fast_train, facecolors='none', edgecolors='b', label="train_fast")
    plt.scatter(grade_slow_train, bumpy_slow_train, facecolors='none', edgecolors='r', label="train_slow")
    plt.scatter(grade_fast_test, bumpy_fast_test, c='b', label="test_fast")
    plt.scatter(grade_slow_test, bumpy_slow_test, c='r', label="test_slow")
    plt.legend()
    plt.xlabel("grade")
    plt.ylabel("bumpiness")
    # plt.savefig("test.png")
    plt.show()


import base64
import json
import subprocess


def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print image_start+json.dumps(data)+image_end
