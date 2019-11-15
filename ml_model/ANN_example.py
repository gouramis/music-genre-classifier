# ANN_example.py

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from genres import classes, NUM_GENRES
from ANN_parameter import Parameter
from ANN_result import Result
from ANN_class import ANN
from ANN_encode import encode, decode
import random

# set your experiment seed for train test split
EXPERIMENT_SEED = 42

# TODO rename to your name
MODEL_NAME = ''

# Load the Data Management's interface
import sys
sys.path.append('../DataManagement/')
import CSVInterface

print('Initializing...')
# reads the data from the csv
reader = CSVInterface.featRead()

# Data stuff
# D = { X | Y }
# D[X][Y]
D = {}
print('reading all features')
# X
D['X'] =  {
	'small'	: reader.getSubset(
				reader.getFrame('features')
			),
	'full'	: reader.getFrame('features')
}

D['Y'] = {
	'small'	: reader.getSubset(
		reader.getFrame('track')['genre_top']
	),
	'full'	: reader.getFrame('track')['genre_top']
}

# Show all the weights prior to training
# net.show_weights(net.num_hidden_layers + 1)

# The data after removing outliers
# data = outlier_method(RawData)

# TODO change to a list of features
indepent_features = 'mfcc'

# the ind vars
X =  pd.DataFrame(D['X']['small'][
		indepent_features]
	)
# the dependent var
Y = pd.DataFrame(D['Y']['small'], columns=['genre_top'])

# Test and train split using encoded Y labels (vector of 0s with one 1)
trainx, testx, trainy, testy = train_test_split(
	X.values,
	encode(Y), # one hot encoder, see ANN_encode.py
	test_size=0.34,
	random_state=EXPERIMENT_SEED
)

sample = trainx[0].copy()

print('\n\nBuilding neural net')
print('input : {}'.format(len(sample)))
print('output: {}'.format(NUM_GENRES))

net = 0
history = 0
callback = 0

# Use this for pre trained models
if MODEL_NAME != '':
	net = ANN(trained_model=MODEL_NAME)
else:
	# Use this to test your own architecture
	net = ANN(p=Parameter(
		num_input=len(sample),
		num_hidden_layers=2,
		nodes_per_hidden=2,
		num_output=NUM_GENRES,
		hidden_activation='relu',
		output_activation='softmax',
		initialize=False,
		learning_rate=10,
		loss_function='categorical_crossentropy'
	))

	# Show the weights
	# net.show_weights(net.num_hidden_layers + 1)

	# Train the network
	# returns history of training process, and a callback object that can
	# extract information about the model at the end of events ANN_callbacks.py
	history, callback = net.train(
		trainx,
		trainy,
		num_iter=1500,
		testing=(testx, np.array(testy)),
		batch=1000
	)

# Set the sample to a specific value. I recommend producing a synthetic sample
# from the data set. Look into pandas.DataFrame.quantile(0, 1.00) to get the min and max to to
# a standard the bounds for the distribution
# for i in range(0, len(sample)):
# 	sample[i] = random.uniform(-100, 100)

# The software engineering team makes this ANN.predict() call, then
# add missing information to ANN_result.Result, then adds it to a wrapper
# to send to the front end!

# Let's see how accurate the model is for the top @num_to_check many categories
# keeps track of number of matches
matches = 0
# the number of test samples to predict
samples = 1000
# the number of results to check
num_to_check = 4

for i in range(0, samples):
	sample = testx[i].copy()
	result = net.predict(pd.DataFrame([sample]))

	counter = 0
	sample_category = decode(testy[i])

	for genre in result.res['prediction']:
		if genre == sample_category: matches = matches + 1
		if counter > num_to_check: break
		# print("{0}: {1}".format(genre, result.res['prediction'][genre]))
		counter = counter + 1

print('Classification rate for top {0}:\t{1}'.format(num_to_check, matches / samples))

# For the ML team: copy and paste this file and name it one word, <your name>
# ANN_<your name>.py
g = input("Save model, {}? (y/n)\t".format(MODEL_NAME)) 
if g == 'Y' or g == 'y':
	g = input('model name: ')
	net.save_to_disk(g)