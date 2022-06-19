import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import sklearn

data=sm.datasets.fair.load_pandas().data

from sklearn.utils import resample
#create two different dataframe of majority and minority class
df_majority = data[(data['affairs_binary']==0)]
df_minority = data[(data['affairs_binary']==1)]
# upsample minority class
df_minority_upsampled = resample(df_minority,
                                 replace=True,    # sample with replacement
                                 n_samples= 4313, # to match majority class
                                 random_state=42)  # reproducible results
# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_minority_upsampled, df_majority])

from patsy import dmatrices
#y=dependent feature X=independent feature
y,X=dmatrices("affairs~rate_marriage+age+yrs_married+children+religious+educ+C(occupation)+C(occupation_husb)",data=df_upsampled,return_type='dataframe')
X=X.drop('Intercept',axis=1)
X = X.rename(columns ={'C(occupation)[T.2.0]':'occ_2','C(occupation)[T.3.0]':'occ_3','C(occupation)[T.4.0]' : 'occ_4' ,'C(occupation)[T.5.0]' : 'occ_5','C(occupation)[T.6.0]':'occ_6',
'C(occupation_husb)[T.2.0]':'occ_husb_2', 'C(occupation_husb)[T.3.0]' :'occ_husb_3','C(occupation_husb)[T.4.0]':'occ_husb_4' , 'C(occupation_husb)[T.5.0]':'occ_husb_5', 'C(occupation_husb)[T.6.0]':'occ_husb_6'})
X.head()
y=df_upsampled['affairs_binary']
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.linear_model import LogisticRegression
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
clf=LogisticRegression(C=0.001,penalty='l2')
clf.fit(x_train,y_train)
y_predicted=clf.predict(x_test)
y_train_predicted=clf.predict(x_train)
from sklearn.metrics import accuracy_score, confusion_matrix,roc_curve,classification_report
print("train set accuracy score: ",accuracy_score(y_train,y_train_predicted))
print("test set accuracy score :",  accuracy_score(y_test,y_predicted))
from sklearn.metrics import confusion_matrix
confusion=confusion_matrix(y_test,y_predicted)
confusion
labels = ['True Neg','False Pos','False Neg','True Pos']

labels = np.asarray(labels).reshape(2,2)

ax = sns.heatmap(confusion, annot=labels, fmt='', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()
TP = confusion[1,1] # true positive
TN = confusion[0,0] # true negatives
FP = confusion[0,1] # false positives
FN = confusion[1,0]#
print('True Positive :', TP)
print("True Negative :",TN)
print('False Positive :',FP)
print('False Negative :',FN)
accuracy = (TP+TN)/len(y_predicted)
accuracy
#Recall quantifies the number of positive class predictions made negative examples in the dataset.it should be minimum
recall=TP/(TP+FN)
recall
#Precision quantifies the number of positive class predictions that actually belong to the positive class.
precison=TP/(TP+FP)
precison
F_score= 2*(precison*recall)/(precison+recall)
F_score

sensitivity = TP/float(TP+FN)
specificity = TN/float(TN+FP)
FPR = FP/float(TN+FP)
PPV = TP/float(TP+FP)
NPV = TN/float(TN+FN)



import joblib
filename='final_logistic_model.joblib'
joblib.dump(clf,open(filename,'wb'))
