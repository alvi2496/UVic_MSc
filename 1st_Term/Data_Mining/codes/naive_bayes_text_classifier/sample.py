import pandas as pd

traintexts = pd.read_csv("datasets/traindata.txt", sep="\n", header=None, names=['text'])
trainlabels = pd.read_csv("datasets/trainlabels.txt", sep="\n", header=None, names=['value'])
traindata = pd.concat([traintexts, trainlabels], axis=1)

testtexts = pd.read_csv("datasets/testdata.txt", sep="\n", header=None, names=['text'])
testlabels = pd.read_csv("datasets/testlabels.txt", sep="\n", header=None, names=['value'])
testdata = pd.concat([testtexts, testlabels], axis=1)

total_document_length = len(traindata.axes[0])
result = set()
traindata.text.str.lower().str.split().apply(result.update)
total_distinct_words = len(result)

p_c = len(traindata.query("value == '1'").axes[0])/total_document_length
p_not_c = len(traindata.query("value == '0'").axes[0])/total_document_length

total_words_in_c = traindata.query("value == '1'").text.str.split().apply(len).sum()
total_words_in_not_c = traindata.query("value == '0'").text.str.split().apply(len).sum()



# Evaluate with traindata
text = input("What's the text: ")

input_array = text.split()

p_fp = p_c
p_ws = p_not_c

# For 1
for w in input_array:
	p_fp *= ( (traindata.query("value == '1'").text.str.count(w).sum() + 1) / 
		(total_words_in_c + total_distinct_words) )

# for 0
for w in input_array:
	p_ws *= ( (traindata.query("value == '0'").text.str.count(w).sum() + 1) / 
		(total_words_in_not_c + total_distinct_words) )

if( p_fp >= p_ws ):
	print("Future Prediction")
elif( p_ws > p_fp ):
	print("Wise Saying")