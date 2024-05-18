import pandas as pd
from sklearn.impute import SimpleImputer


class MissingValueHandler:
    def impute(df, column, strategy='mean', fill_value=None):
        if strategy in ['mean', 'median', 'most_frequent']:
            imputer = SimpleImputer(strategy=strategy)
        elif strategy == 'constant' and fill_value is not None:
            imputer = SimpleImputer(strategy='constant', fill_value=fill_value)
        else:
            raise ValueError(
                "Invalid strategy. Choose 'mean', 'median', 'most_frequent', or 'constant' with a fill_value.")
        df[column] = imputer.fit_transform(df[[column]])
        return df

    @staticmethod
    def delete_rows(df, columns, how='any'):
        return df.dropna(subset=columns, how=how)

    @staticmethod
    def delete_columns(df, threshold=0.5):
        return df.dropna(axis=1, thresh=int(threshold * len(df)))