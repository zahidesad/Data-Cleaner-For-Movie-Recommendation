import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, column, drop_first=True):
        encoder = OneHotEncoder(drop=drop_first, sparse=False)
        encoded = encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
        df = df.join(encoded_df)
        return df.drop(column, axis=1)

    @staticmethod
    def label_encode(df, column):
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        return df

    @staticmethod
    def target_encode(df, column, target):
        mean_target = df.groupby(column)[target].mean()
        df[column + '_encoded'] = df[column].map(mean_target)
        return df
