# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('new_auto_data.csv')
# X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, 3].values 
X = dataset[['engine-size', 'city-mpg']]
y = dataset.price

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y) 

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb')) 

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[130,1]]))
