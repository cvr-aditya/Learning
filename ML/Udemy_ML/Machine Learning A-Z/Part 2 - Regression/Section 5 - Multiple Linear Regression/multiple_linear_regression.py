# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#Building optimal model using backward elimination
import statsmodels.formula.api as sm
X = np.append(arr=np.ones((len(X), 1)).astype(int), values=X, axis=1)

sl = 0.05
indexes = [i for i in range(len(X[0]))]
done = False
regressor_OLS = None
while not done:
    X_opt = X[:, indexes]
    regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
    pvalues = regressor_OLS.pvalues
    if pvalues.max() > sl:
        poppded_Index = indexes.pop(pvalues.argmax())
        print "Popped index is :: " + str(poppded_Index)
    else:
        done = True
print regressor_OLS.summary()
print indexes

# R&D investment vs Predicted Profit
plt.scatter(X_test[:,2], regressor.predict(X_test))

# Administration vs Predicted Profit
plt.scatter(X_test[:,3], regressor.predict(X_test))