import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


def trainning_data ():
    """
    This gives the training data being worked with.
    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    df=pd.read_csv("../../Data/Imputed.csv")
    X=df.drop("HINCP_x",axis=1)
    y=df["HINCP_x"]
    X_train, X_test,y_train, y_test=train_test_split(X,y,train_size=.8,random_state=2020)
    return X_train, X_test,y_train, y_test
