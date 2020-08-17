import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder as SklearnOneHotEncoder


def training_data(df):
    """
    This gives the training data being worked with.
    """
    X=df.drop("HINCP_x",axis=1)
    y=df["HINCP_x"]
    X_train, X_test,y_train, y_test=train_test_split(X,y,train_size=.8,random_state=2020)
    return X_train, X_test,y_train, y_test


class OneHotEncoder(SklearnOneHotEncoder):
    """(https://towardsdatascience.com/how-to-assign-labels-with-sklearn-one-hot-encoder-e59a5f17df4f)
    """
    def __init__(self, **kwargs):
        super(OneHotEncoder, self).__init__(**kwargs)
        self.fit_flag = False

    def fit(self, X, **kwargs):
        out = super().fit(X)
        self.fit_flag = True
        return out

    def transform(self, X, **kwargs):
        sparse_matrix = super(OneHotEncoder, self).transform(X)
        new_columns = self.get_new_columns(X=X)
        d_out = pd.DataFrame(sparse_matrix.toarray(), columns=new_columns, index=X.index)
        return d_out

    def fit_transform(self, X, **kwargs):
        self.fit(X)
        return self.transform(X)

    def get_new_columns(self, X):
        new_columns = []
        for i, column in enumerate(X.columns):
            j = 0
            while j < len(self.categories_[i]):
                new_columns.append(f'{column}_<{self.categories_[i][j]}>')
                j += 1
        return new_columns
    
def process_data(df):   
    #clearing the target column of nan values
    no_target_nans=df["HINCP"].dropna()
    #Clearing the targert column of zero values
    non_nans_and_non_zero= no_target_nans[no_target_nans!=0]
    #mergring our dataframes with the non zero and non nan df to get our applicable rows
    base_df_1=df.merge(non_nans_and_non_zero,how="inner",right_index=True,left_index=True)
    #get our features of interest based on pearson correlation
    df1_with_with_features=base_df_1.loc[:,
                                        ["HINCP_x","PUMA","NP","ACR","BDSP","BUS","CONP",
                                         "FS","INSP","MRGP","MRGI","RMSP","RNTP",
                                         "SMP","TOIL","VALP","VEH","YBL","TAXAMT",
                                         "SVAL","SMOCP","WIF"]]
#spitting up the df with numerica and categorical features
    df1_numeric=df1_with_with_features[["HINCP_x","SMOCP","PUMA","NP","BDSP","CONP","INSP","MRGP","RMSP","RNTP","SMP","VALP","TAXAMT"]]
    #dropping columns based on amount of values that need to be imputed and the distribution of data.
    df1_numeric_dropepd_columns=df1_with_with_features[["HINCP_x","SMOCP","PUMA","NP","BDSP","CONP","INSP","MRGP","RMSP","VALP","TAXAMT"]]
    #organizing final data grame with the qualified variables
    df1_numeric_dropepd_columns_v2=df1_with_with_features[["HINCP_x","SMOCP","PUMA","NP","BDSP","INSP","RMSP","VALP","TAXAMT"]]

#imputing the amount for taxes paid column
    tax_meadian=df1_numeric_dropepd_columns[df1_numeric_dropepd_columns.TAXAMT>0]
    taxx_meadian=tax_meadian.TAXAMT.median()
    df1_numeric_dropepd_columns_v2.TAXAMT.replace(np.nan,taxx_meadian,inplace=True)
    taxx_meadian
#imputing the amount for value of property column

    val_meadian=df1_numeric_dropepd_columns[df1_numeric_dropepd_columns.VALP>0]
    vall_meadian=val_meadian.VALP.median()
    df1_numeric_dropepd_columns_v2.VALP.replace(np.nan,vall_meadian,inplace=True)
    vall_meadian
#imputing the amount for the insurance paid column

    insp_meadian=df1_numeric_dropepd_columns[df1_numeric_dropepd_columns.INSP>0]
    inspp_meadian=insp_meadian.INSP.median()
    df1_numeric_dropepd_columns_v2.INSP.replace(np.nan,inspp_meadian,inplace=True)
    inspp_meadian
#imputing the amount for selected monthy owenr cost column

    smocp_meadian=df1_numeric_dropepd_columns[df1_numeric_dropepd_columns.SMOCP>0]
    smocpp_meadian=smocp_meadian.SMOCP.median()
    df1_numeric_dropepd_columns_v2.SMOCP.replace(np.nan,smocpp_meadian,inplace=True)
    smocpp_meadian

#making the categorical data frame
    df1_categorical_columns_v2=df1_with_with_features[["HINCP_x","ACR","BUS","FS","TOIL","VEH","YBL"]]

#making the most commmon categorical and allow for base df to remain
    df_most_common_categorical=df1_categorical_columns_v2
   # imputing the acr and bus colimn based on the most common value in each column
    df_most_common_categorical[["ACR","BUS"]]=df1_categorical_columns_v2[["ACR","BUS"]].apply(lambda x: x.fillna(x.value_counts().index[0]))


#instantiating the onehot encoder
    encoder=OneHotEncoder()
#encoding the needed values
    encoded_catecories=encoder.fit_transform(df_most_common_categorical.drop("HINCP_x",axis=1))
#merging the numerical and catergorical features dataframes
    final_df=df1_numeric_dropepd_columns_v2.merge(encoded_catecories,how="inner",right_index=True,left_index=True)
#dropping the puma code column due to it being an identifier
    final_df=final_df.drop("PUMA",axis=1)
    
#retuning the final data frame via a train test split
    return training_data(final_df)