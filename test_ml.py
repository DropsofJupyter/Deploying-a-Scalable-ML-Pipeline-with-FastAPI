import pytest

# TODO: add necessary import
import pandas as pd
import os
from ml.model import load_model
from ml.data import process_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# TODO: implement the first test. Change the function name and input as needed
def test_cat_features():
    """
    check whether the categorical columns in the census.csv dataset from the project's data directory match the categorical columns being transformed in the cat_features variable as it is instantiated in the main.py file at the project root.
    """
    # Your code here
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(project_path, "data", "census.csv")
    
    data = pd.read_csv(data_path)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    data_cat_features = data.select_dtypes(include="object").drop(columns='salary')

    assert sorted(cat_features) == sorted(data_cat_features)

# TODO: implement the second test. Change the function name and input as needed
def test_model_type():
    """
    Loads the model pickle file from the model file of the project and ensures that it is, in fact, an instance of Sklearn.linear_model.LogisticRegression
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "model.pkl") # TODO: enter the path for the saved model 
    model = load_model(path)

    assert isinstance(model, LogisticRegression)


# TODO: implement the third test. Change the function name and input as needed
def test_train_xy_shape():
    """
    load csv dataset for training from project root '/data/census.csv', then performs the train_test_split with same random state as is used in the train_model.py file. Finally, compares the X_train and y_train from the process_data function in the project root '/ml/data.py' file
    """
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(project_path, "data", "census.csv")
    
    df = pd.read_csv(data_path)

    train, _ = train_test_split(df, test_size=0.3, random_state=42)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_train, y_train, _, _ = process_data(
    # your code here
    # use the train dataset 
    # use training=True
    # do not need to pass encoder and lb as input
    X=train,
    categorical_features=cat_features,
    label="salary"
    )

    assert X_train.shape[0] == y_train.shape[0]


