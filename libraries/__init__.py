#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import nltk 
import re, string
from nltk.corpus import stopwords
#from nltk.tokenize.toktok import ToktokTokenizer
import spacy
from joblib import load
import sklearn
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import seaborn as sns
#import transformers  # huggingface transformers library
import unicodedata
#import tensorflow as tf
#from tensorflow.keras.preprocessing.sequence import pad_sequences
#from tensorflow.keras.preprocessing.text import Tokenizer
# from transformers import BertTokenizer, TFAutoModel
# import keras
# from keras.utils import np_utils
# from keras.preprocessing.text import Tokenizer, text_to_word_sequence
# from keras.preprocessing import sequence
# #from tensorflow.keras.layers import add
# from keras.initializers import Constant
# from keras.callbacks import ModelCheckpoint
# from keras.models import Sequential, Model, load_model
# from keras.layers import Reshape,Concatenate, Lambda, Average
# from keras.layers import GlobalAveragePooling1D, BatchNormalization, concatenate
# from keras.layers import Dropout, Embedding, GlobalMaxPooling1D, MaxPooling1D, Add, Flatten, SpatialDropout1D
# from keras.layers import Dense, Input, LSTM, Bidirectional, Activation, Conv1D, GRU, TimeDistributed
# from keras import initializers, regularizers, constraints
#from tensorflow.keras.layers import Layer
#from keras import backend as K