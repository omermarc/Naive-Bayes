from tkinter import messagebox as mb

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder






def answer():
    mb.showinfo("Naïve Bayes Classifier", "Building classifier using dialog train-set is done!")


# Converting values to numbers (if they are not numeric)
def clean_data(train, test,attributes):

    test_features = []
    train_features = []
    for col in test.columns:
        test_features.append(col)
    for col in train.columns:
        train_features.append(col)

    le = preprocessing.LabelEncoder()

    for i in train_features:
        if(attributes[i]!="NUMERIC"):

            train[i] = pd.Categorical(train[i])
            categories = train[i].cat.categories
            test[i] = pd.Categorical(test[i], categories)

            train[i] = train[i].cat.codes
            test[i] = test[i].cat.codes

    #print(test)
    #print(train)






## Build model

def build(train, test, structure_features,bins, attributes):

    test_features = []
    train_features = []
    for col in test.columns:
        test_features.append(col)
    for col in train.columns:
        train_features.append(col)
    bins_dict = {}

    #check if the files fit to the structure
    for i in range(0, len(structure_features) - 1):
        if train_features[i] != structure_features[i] or test_features[i] != structure_features[i]:
            print("values are not fit to structure!")
            return False
    filldata(train,attributes)
    filldata(test,attributes)
    #dialog:
    answer()
    bins= int(bins)

    #change strings to nums
    clean_data(train, test, attributes)
    train = discret(train, attributes, bins,True, bins_dict)
    test = discret(test,attributes,bins,True,bins_dict)


    return True


def discret(csv, attributes, got_bins, is_train, bins_dict):
    for at in attributes:
        if attributes[at] == "NUMERIC":

            maximum = int(csv[at].max())
            minimum = int(csv[at].min())

            bins_size = (maximum - minimum) / got_bins
            bins = []
            group_names = []
            bin_num = 1

            for i in range(got_bins):
                if i < got_bins - 1:
                    curr_bin = (bin_num * bins_size) + minimum

                    bin_num += 1
                    bins.append(curr_bin)

                group_names.append(i + 1)
            # binning
            csv[at] = binning(csv[at], bins, group_names)

        if attributes[at] is not "NUMERIC":
            attribute_bins = len(attributes[at].split(","))
            if is_train:
                bins_dict[at] = attribute_bins
    return csv

#bininig the data
def binning( col, cut_p, labels=None):
    minimum = col.min()
    maximum = col.max()
    break_p = [minimum] + cut_p + [maximum]
    if not labels:
        labels = range(len(cut_p) + 1)
    col = pd.cut(col, bins=break_p, labels=labels, include_lowest=True)
    return col


#filling numeric nA's with mean and non numeric with most common
def filldata(csv,attributes):
    for key in attributes:
        if attributes[key] == "NUMERIC":
            filling_value = csv[key].mean()
        else:
            filling_value = csv[key].mode().iloc[0]

        csv[key] = csv[key].fillna(filling_value)
    #print(csv)

