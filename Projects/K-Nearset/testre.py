import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Print Data Set
df = pd.read_csv(r"D:\Programming Project\Python Project\Machine learning\K-Nearset\teleCust1000t.csv")
print(df.head())

# فصل البيانات الى فيتشرز ولابليبز
columes = ['region','tenure','age','marital','address','income','ed','employ','retire','gender','reside','custcat']
lables = df['custcat'].values
features = df[list(columes)].values

# train test split فصل البيانات الى تدريب وتقيم باستخدام 
X_train , X_test , Y_train , Y_test = train_test_split(features,lables,test_size=0.30) # give 30% of data for testing
clf = RandomForestClassifier(n_estimators=3)
clf = clf.fit(features,lables) # fit is responsbal for train the module
# traine dataset after spreat it to train and data
acc = clf.score(X_train,Y_train)
print(acc * 100)

dataset = pd.read_csv(r"D:\Programming Project\Python Project\Machine learning\K-Nearset\teleCust1000t.csv")

#determin independent values.
x=dataset.iloc[:,-1].values
#determin dependent values  train_test_split(X,y,test_size=0.3, random_state=0)
y =dataset.iloc[:,1].values #spliting the dataset into the training set and test set

from sklearn.model_selection import train_test_split
X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

y_pred=regressor.predict(X_test)
y_pred_train=regressor.predict(X_train)

x_train= X_train.reshape(-1, 1)
y_train= Y_train.reshape(-1, 1)
x_test = X_test.reshape(-1, 1)

plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,y_pred_train,color='blue')
plt.title('Salary vs Experience(training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,y_pred_train,color='blue')
plt.title('Salary vs Experience(test set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()