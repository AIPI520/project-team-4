import numpy as np
import pandas as pd

def train_model(X_train, y_train, model):
    model.fit(X_train, y_train)
    return model

def make_predictions(model, X_test):
    predictions = model.predict(X_test)
    return predictions

def evaluate(test_preds, X_test, y_test, X_train_SimStartDate, X_test_SimStartDate):
    # Aggregate predictions by SimStartDate and event_type
    preds_df = X_test.copy()
    preds_df['outage_count'] = test_preds
    preds_df['SimStartDate'] = X_test_SimStartDate

    grouped_preds = preds_df.groupby(['SimStartDate','event_type']).outage_count.sum().sort_index()
    print("Number of predictions: ", len(grouped_preds))
    # display(grouped_preds)
    print("Predictions: ", grouped_preds)

    # Aggregate true values by SimStartDate and event_type
    true_vals_df = X_test.copy()
    true_vals_df['outage_count'] = y_test
    true_vals_df['SimStartDate'] = X_test_SimStartDate

    grouped_trues = true_vals_df.groupby(['SimStartDate','event_type']).outage_count.sum().sort_index()
    print("Number of true values: ", len(grouped_trues))
    # display(grouped_trues)
    print("True values: ", grouped_trues)

    mse_sq = np.square(grouped_preds - grouped_trues).mean()
    print("MSE: ", mse_sq)

    mae = np.abs(grouped_preds - grouped_trues).mean()
    print("MAE: ", mae)

    mape = np.abs((grouped_preds - grouped_trues) / grouped_trues).mean()
    print("MAPE: ", mape)