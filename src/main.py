import data_loader as dl
import build_features as bf
import model as m
import scripts.build_features as fl
from sklearn.model_selection import train_test_split

def main():
    # Load the data
    df = fl.load_and_clean_data()

    # Generate features
    X, y, selected_feats = bf.generate_features(df)

    # Split the data into training and testing sets
    X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0,test_size=0.4)
    print("Train set size: ", X_train.shape)

    model = m.train_model(X_train[selected_feats], y_train, model)

    preds = m.make_predictions(model, X_test[selected_feats])

    # Print the accuracy of the model
    print('Accuracy:', accuracy_score(y_test, predictions))

main()
