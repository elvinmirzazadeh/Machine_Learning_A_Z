import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('data/Social_Network_Ads.csv')
X = dataset.iloc[:, 2:-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, 
                                                    random_state = 0, shuffle = True)


#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#-------------------Fitting SVM on traindata
from sklearn.svm import SVC 
svc = SVC(kernel='rbf', random_state=0)
svc.fit(X_train, y_train)
acc = svc.score(X_train, y_train)
y_pred = svc.predict(X_test)

#-------------------Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


plt.plot(y_test)
plt.plot(y_pred, color='red')
plt.show()



#-------------------Visualising Trainig results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop = X_set[:,0].max() + 1, step=0.01),
                     np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:,1].max() + 1, step=0.01))

plt.contourf(X1, X2, svc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.15, cmap=ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0], X_set[y_set==j, 1],
                c = ListedColormap(('red', 'green'))(i), label=j)
plt.title = 'Training Set'
plt.show()


#-------------------Visualising Test4 results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test

X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop = X_set[:,0].max() + 1, step=0.01),
                     np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:,1].max() + 1, step=0.01))

plt.contourf(X1, X2, svc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.15, cmap=ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0], X_set[y_set==j, 1],
                c = ListedColormap(('red', 'green'))(i), label=j)
plt.title = 'Test Set'
plt.show()































