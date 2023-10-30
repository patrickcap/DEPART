"""
Use the stored dataset to train a machine learning model
"""

import os
from train_model import train_model

#load and pre-process data
csv_path = os.path.join(os.getcwd(),'data.csv')

# train and save model
train_model(csv_path,'test1')
