# ANN_parameter.py
# author nick s.

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from tensorflow.keras.optimizers import SGD

# Placeholder classes
genres = ['Genre 1', 'Genre 2', 'Genre 3', 'Genre 4']

DEF_INPUT_NODES = 8
DEF_OUTPUT_NODES = len(genres)
DEF_HIDDEN_LAYERS = 2
DEF_NODES_PER_LAYER = 3
DEF_HIDDEN_ACTIVATION = 'sigmoid'
DEF_OUTPUT_ACTIVATION = 'sigmoid'
DEF_LEARNING_RATE = 10
DEF_LOSS_FUNCTION = 'mean_squared_error'

# Call back function used to extract info from the model
# during trainingß
class CallBack(keras.callbacks.Callback):
	# add variables to keep track of parameters

	def on_train_begin(self, logs={}):
		return

	def on_train_end(self, logs={}):
		return
 
	def on_epoch_begin(self, logs={}):
		return
 
	def on_epoch_end(self, epoch, logs={}):
		return
 
	def on_batch_begin(self, batch, logs={}):
		return
 
	def on_batch_end(self, batch, logs={}):
		return


# Make a parameter object to be passed to the constructor of the ANN
# Interface for the .csv file
class ANN_Parameter():
	# interface
	keys = [
		'num_input',
		'num_hidden_layers',
		'nodes_per_hidden',
		'num_output',
		'hidden_activation',
		'output_activation',
		'initialize',
		'learning_rate',
		'loss_function'
	]

	# cosntructor
	def __init__(
		self,
		num_input=DEF_INPUT_NODES,
		num_hidden_layers=DEF_HIDDEN_LAYERS,
		nodes_per_hidden=DEF_NODES_PER_LAYER,
		num_output=DEF_OUTPUT_NODES,
		hidden_activation=DEF_HIDDEN_ACTIVATION,
		output_activation=DEF_OUTPUT_ACTIVATION,
		initialize=True,
		learning_rate=DEF_LEARNING_RATE,
		loss_function=DEF_LOSS_FUNCTION):

		self.parameters = {
			'num_input': num_input,
			'num_hidden_layers': num_hidden_layers,
			'nodes_per_hidden': nodes_per_hidden,
			'num_output': num_output,
			'hidden_activation': hidden_activation,
			'output_activation': output_activation,
			'initialize': initialize,
			'learning_rate':learning_rate,
			'loss_function': loss_function
		}