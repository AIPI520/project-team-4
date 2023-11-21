import os
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

class ModelBuilder:

    """
    Class Description:
    """
    @staticmethod
    def build_decision_tree_model(X_train, y_train):
        print('Building decision tree model...')
        # Set up and run a cross-validated grid search to find the best parameters
        params = {'min_samples_leaf':[1,3,10],'n_estimators':[100,1000],
            'max_features':[0.1,0.5,1.],'max_samples':[0.5,None]}

        #params = {'max_depth': None, 'max_features': 0.1, 'max_samples': None, 'min_samples_leaf': 3, 'n_estimators': 1000}

        m = RandomForestRegressor()
        grid_search = GridSearchCV(m,params,cv=3)
        grid_search.fit(X_train,y_train)
        print('Best parameters: ', grid_search.best_params_)

        model = RandomForestRegressor(**grid_search.best_params_)

        #model = RandomForestRegressor(**params)
        model.set_params(n_jobs=-1)

        return model
    
    @staticmethod
    def build_linear_model():
        print('Building linear model...')
        model = LinearRegression()
        return model
    
    @staticmethod
    def build_lasso_model():
        print('Building lasso model...')
        model = Lasso(alpha=0.3)
        return model
    