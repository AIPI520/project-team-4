from data_loader import DataLoader
from feature_builder import FeatureBuilder
from model_builder import ModelBuilder
from sklearn.model_selection import train_test_split

from model_trainer import train_model, make_predictions, evaluate

def main():
    # Load the data
    df = DataLoader.load_and_clean_data()
    
    # remove features with only one value
    df = FeatureBuilder.remove_one_value_features(df)

    # Generate features
    X_train, X_test, y_train, y_test, selected_feats = FeatureBuilder.filter_best_features(df)

    X_train.columns[0]

    print("Number of features: ", len(selected_feats))
    print("X_test sample: ", X_test.head())
    
    #model = ModelBuilder.build_lasso_model()
    #model = ModelBuilder.build_linear_model()

    print("X_train shape: ", X_train.shape)

    # get only 30% of the data for training
    #X_train, _, y_train, _ = train_test_split(X_train, y_train, test_size=0.7, random_state=42)
    
    model = ModelBuilder.build_decision_tree_model(X_train, y_train)
    model = train_model(X_train, y_train, model)
    test_preds = make_predictions(model, X_test)

    evaluate(test_preds, X_test, y_test)

    return

main()
