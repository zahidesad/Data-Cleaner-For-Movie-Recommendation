from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
import pandas as pd


class Scaler:
    @staticmethod
    def min_max_scaling(df, columns):
        scaler = MinMaxScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

    @staticmethod
    def standard_scaling(df, columns):
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

    @staticmethod
    def robust_scaling(df, columns):
        scaler = RobustScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df
