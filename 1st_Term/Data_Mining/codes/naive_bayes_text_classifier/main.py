import pandas as pd

traintexts = pd.read_csv("datasets/traindata.txt", sep="\n", header=None, names=['text'])
trainlabels = pd.read_csv("datasets/trainlabels.txt", sep="\n", header=None, names=['value'])
traindata = pd.concat([traintexts, trainlabels], axis=1)

testtexts = pd.read_csv("datasets/testdata.txt", sep="\n", header=None, names=['text'])
testlabels = pd.read_csv("datasets/testlabels.txt", sep="\n", header=None, names=['value'])
testdata = pd.concat([testtexts, testlabels], axis=1)
print(traindata.head())
print(testdata.head())