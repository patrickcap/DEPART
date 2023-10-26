import os
from train_.train_model import train_

# load and pre-process data
csv_path = os.path.join(os.getcwd(), 'data.csv')

# train and save model
train_(csv_path, 'test1')
'''
#import perfromance evaluation library
from sklearn.model_selection import cross_val_score
from sklearn.metrics import recall_score, make_scorer, confusion_matrix, roc_curve, auc, accuracy_score, f1_score, roc_auc_score
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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
'''
