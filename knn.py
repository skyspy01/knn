import numpy as np # linear algebra
import matplotlib.pyplot as plt # For plotting
import pandas as pd 
from KNearestNeighbor import KNearestNeighbors
from sklearn.matrics import confusion_matrix
data=pd.read_csv('Social_Network_Ads.csv')
data

x = dat.iloc[:,2:4].values
y = data.iloc[:,-1].values







from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)




def predict_new():
	age = int(input("enter the age"))
	salary = int ( intput("enter the salary"))
	X_nwe = np.array([[age],[salary]]).reshape(1,2)
	
	X_new = scaler.transform(X_new)
	
	result = knn.predict(X_new)
	
	if result ==0:
		print(" will not purchase")
	else:
		print("will purchasse")
predict_new()
