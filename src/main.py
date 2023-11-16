from data_loader import DataLoader
from feature_builder import FeatureBuilder
from model_builder import ModelBuilder
from sklearn.model_selection import train_test_split

from model_trainer import train_model, make_predictions, evaluate

def main():
    # Load the data
    df = DataLoader.load_and_clean_data()
    
    # Generate features
    X_train_full, X_test, y_train_full, y_test, selected_feats, X_train_SimStartDate, X_test_SimStartDate = FeatureBuilder.filter_best_features(df)

    print("Number of features: ", len(selected_feats))
    print("X_test sample: ", X_test.head())
    # for f in selected_feats:
    #     print(f)

    model = ModelBuilder.build_linear_model(X_train_full, y_train_full)
    # model = ModelBuilder.build_decision_tree_model(X_train_full, y_train_full)
    model = train_model(X_train_full, y_train_full, model)
    test_preds = make_predictions(model, X_test)

    evaluate(test_preds, X_test, y_test, X_train_SimStartDate, X_test_SimStartDate)

    return

main()
