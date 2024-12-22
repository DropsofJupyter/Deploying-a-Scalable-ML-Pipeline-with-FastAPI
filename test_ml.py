import pytest

# TODO: add necessary import
import pandas as pd
import os
from ml.model import load_model
from sklearn.linear_model import LogisticRegression


# TODO: implement the first test. Change the function name and input as needed
def test_cat_features():
    """
    check whether the categorical columns in the census.csv dataset match the categorical columns being transformed in the cat_features variable as it is instantiated in the main.py file at the project root.
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
def test_two():
    """
    # add description for the second test
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "model.pkl") # TODO: enter the path for the saved model 
    model = load_model(path)

    print(type(model))

    print(isinstance(model, LogisticRegression))



# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
