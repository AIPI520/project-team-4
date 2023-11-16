import os
import pandas as pd
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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

        model = RandomForestRegressor()
        grid_search = GridSearchCV(model, params, cv=5)
        grid_search.fit(X_train,y_train)
        print('Best parameters: ', grid_search.best_params_)

        model = RandomForestRegressor(**grid_search.best_params_)
        return model
    
    @staticmethod
    def build_linear_model(X_train, y_train):
        print('Building linear model...')
        model = LinearRegression()
        return model