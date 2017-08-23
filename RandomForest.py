import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

#print count of each value in column workclass , so as to fill missing data with mode

#print(train.workclass.value_counts())
train.workclass.fillna('Private',inplace=True)
#print(train.isnull().sum())

#print(train.occupation.value_counts())
train.occupation.fillna('Prof-speciality',inplace=True)
#print(train.isnull().sum())

#print(train.info())
#print(train['native.country'].value_counts())
train['native.country'].fillna('United-States',inplace=True)

#print(pd.crosstab(train.education,train.target,margins=True)/train.shape[0])

#label each value in numeric format for better analysis

for x in train.columns:
	if train[x].dtype=='object':
		lbl=preprocessing.LabelEncoder()
		lbl.fit(list(train[x].values))
		train[x]=lbl.transform(list(train[x].values))

for x in test.columns:
	if test[x].dtype=='object':
		lbl=preprocessing.LabelEncoder()
		lbl.fit(list(test[x].values))
		test[x]=lbl.transform(list(test[x].values))




cols=[]

for x in train.columns:
	cols.append(x)

colsRes=['target']

trainArr=train.as_matrix(cols)
trainRes=train.as_matrix(colsRes)


rf=RandomForestClassifier(n_estimators=10)
rf.fit(trainArr,trainRes)

testArr=test.as_matrix(cols)
results=rf.predict(testArr)

test['ans']=results

print (test.head())

temp=0
tot=0

print(test.ans.value_counts())
print(test.target.value_counts())

