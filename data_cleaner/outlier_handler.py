import pandas as pd
import numpy as np


class OutlierHandler:
    @staticmethod
    def iqr_outlier_detection(df, column, threshold=1.5):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    @staticmethod
    def z_score_outlier_detection(df, column, threshold=3):
        mean = df[column].mean()
        std = df[column].std()
        df['z_score'] = (df[column] - mean) / std
        return df[abs(df['z_score']) <= threshold].drop(columns=['z_score'])

    @staticmethod
    def replace_outliers(df, column, method='mean'):
        if method == 'mean':
            replacement_value = df[column].mean()
        elif method == 'median':
            replacement_value = df[column].median()
        else:
            raise ValueError("Invalid method. Choose 'mean' or 'median'.")

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
               
        df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), replacement_value, df[column])
        return df
