from data_loader import DataLoader
from feature_builder import FeatureBuilder
from sklearn.model_selection import train_test_split

def main():
    # Load the data
    df = DataLoader.load_and_clean_data()
    
    # Generate features
    X_train_full, X_test, y_train_full, y_test, selected_feats = FeatureBuilder.filter_best_features(df)

    print("Number of features: ", len(selected_feats))
    for f in selected_feats:
        print(f)

    return

main()
