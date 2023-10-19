#import soupport file
from data_processing import *
from model_setting import *

import os
#import pipeline related lib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
#import perfromance evaluation library
from sklearn.model_selection import cross_val_score
from sklearn.metrics import recall_score, make_scorer, confusion_matrix, roc_curve, auc, accuracy_score, f1_score, roc_auc_score
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#load and pre-process data
csv_path = os.path.join(os.getcwd(),'data.csv')
df = process_add_columns(drop_columns(compute_delay(load_data(csv_path))))

#split test and train data set
train_data,train_labels,test_data,test_labels = split_dataset(df)

#transformer
transformer = ColumnTransformer(transformers=[
    ('tnf1',OrdinalEncoder(categories=[['morning','afternoon','evening','night'],['N','I']]),['part_of_day','flight_type']),
    ('tnf2',OneHotEncoder(handle_unknown='ignore',sparse=False,drop='first'),['sched_destination_city_code','sched_airlinecode','is_weekend','sched_flight_month'])
],remainder='passthrough')

#pipeline
#please add new model in model_setting.py and just change the model fucntion in pipeline
XGBCV_pipeline = Pipeline([
    ('transformer', transformer),
    ('XB_boosting', GridXGB)
    ])

# Train it and print the best parameters (3 pts)
XGBCV_pipeline.fit(train_data, train_labels)

print(XGBCV_pipeline['XB_boosting'].best_params_)
XGB = XGBCV_pipeline['XB_boosting'].best_estimator_
#shows performance
XGB_pipeline = Pipeline([
    ('transformer', transformer),
    ('XB_boosting', XGB)
    ])

cv = cross_val_score(XGB_pipeline, train_data, train_labels, cv=5, scoring='accuracy', error_score='raise').mean()
print('CV Accuracy Score: ', str(cv))

pred_test_labels = XGB_pipeline.fit(train_data, train_labels).predict(test_data)

accuracy = accuracy_score(pred_test_labels, test_labels)
f1 = f1_score(pred_test_labels, test_labels, average="weighted")
print('Accuracy Score: ', str(accuracy))
print('f1 Score: ', str(f1))

cm = confusion_matrix(test_labels, pred_test_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Delayed", "On Time"])
disp.plot()


prob_test_labels = XGB_pipeline.fit(train_data, train_labels).predict_proba(test_data)
prob_test_labels = prob_test_labels[:, 1]

# Calculate the ROC curve points
fpr, tpr, thresholds = roc_curve(test_labels,prob_test_labels)

# Save the AUC in a variable to display it
auc = np.round(roc_auc_score(y_true = test_labels, y_score = prob_test_labels), decimals = 3)

# Create and show the plot

plt.plot(fpr,tpr,label="AUC = " + str(auc))
plt.legend(loc=4)
plt.xlabel(r'False Positive Rate')
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()