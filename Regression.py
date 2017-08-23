import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt

data=pd.read_csv("CCC.csv")


#print(data.head())


target=data['PE']

#print(target.head())

X_train=data[0:5000]
y_train=target[0:5000]

#print(X_train)


lm=linear_model.LinearRegression()
model=lm.fit(X_train,y_train)

X_test=data[5000:9560]
y_test=target[5000:9560]

predictions=lm.predict(X_test)

for x in range (0,10):
	print(X_test.iloc[x].PE,predictions[x])

print(lm.score(X_test,y_test))

