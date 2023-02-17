from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

#===========Load Data From CSV File===============
df = pd.read_csv(r'D:\File\Programming Project\Python Project\Machine learning\K-Nearset\teleCust1000t.csv')
print(df.head())

#===========Data Visualization and Analysis============
df['custcat'].value_counts()

#===========281 Plus Service, 266 Basic-service, 236 Total Service, and 217 E-Service customers===================
df.hist(column='income', bins=50)

#==================Feature set====================
df.columns
X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
X[0:5]

#==============What are our labels?================
y = df['custcat'].values
y[0:5]

#==============Normalize Data======================
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]

#===============Train Test Split=====================
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)

#===============Train Model and Predict with K= 4============
from sklearn.neighbors import KNeighborsClassifier
k = 4
#Train Model and Predict  
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)

#================Predicting========================
yhat = neigh.predict(X_test)
yhat[0:5]

#===============Accuracy evaluation================
from sklearn import metrics
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))

#===============Practice The Modul with K = 6===========================
# write your code here
k = 6
#Train Model and Predict  
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat = neigh.predict(X_test)
from sklearn import metrics
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
#===============Practice The Modul with K = 10===========================
Ks = 10
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
ConfustionMx = [];
for n in range(1,Ks):
    #Train Model and Predict  
    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)
    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])
mean_acc
#===============Plot model accuracy for Different number of Neighbors===========================
plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Accuracy ', '+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Nabors (K)')
plt.tight_layout()
plt.show()
print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1) 
#===============Plot model accuracy for Different number of Neighbors===========================
plt.figure()
plt.scatter(X[:,0], X[:,6],c=y, cmap=cmap, edgecolors= 'k',s=100)
plt.show()