import numpy as np
import pandas as pd

def train_model(X_train, y_train, model):
    for col in X_train.columns:
        print(col)

    model.fit(X_train, y_train)
    return model

def make_predictions(model, X_test):
    predictions = model.predict(X_test)

    return predictions

def evaluate(test_preds, X_test, y_test):
    # Aggregate predictions by SimStartDate and event_type
    preds_df = X_test.copy()
    preds = np.round(test_preds).astype(int)+1
    y_test = y_test+1
    print("Number of predictions: ", len(preds_df))
    
    mse_sq = np.square(preds - y_test).mean()
    print("MSE: ", mse_sq)

    mae = np.abs(preds - y_test).mean()
    print("MAE: ", mae)

    mape = np.abs((preds - y_test) / y_test).mean()
    print("MAPE: ", mape)