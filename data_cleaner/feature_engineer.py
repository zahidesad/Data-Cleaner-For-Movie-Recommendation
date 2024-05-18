import pandas as pd

class FeatureEngineer:
    @staticmethod
    def create_feature(df, new_column, func, *args):
        df[new_column] = df.apply(lambda row: func(row, *args), axis=1)
        return df

    @staticmethod
    def binning(df, column, bins, labels):
        df[column + '_binned'] = pd.cut(df[column], bins=bins, labels=labels)
        return df

    @staticmethod
    def polynomial_features(df, column, degree):
        for i in range(2, degree + 1):
            df[column + f'_{i}'] = df[column] ** i
        return df

    @staticmethod
    def interaction_features(df, columns):
        from itertools import combinations
        for col1, col2 in combinations(columns, 2):
            df[col1 + '_x_' + col2] = df[col1] * df[col2]
        return df
