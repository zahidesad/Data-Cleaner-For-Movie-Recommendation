import pandas as pd

class DataTypeConverter:
    @staticmethod
    def to_numeric(df, column, errors='coerce'):
        df[column] = pd.to_numeric(df[column], errors=errors)
        return df

    @staticmethod
    def to_categorical(df, column):
        df[column] = df[column].astype('category')
        return df

    @staticmethod
    def to_datetime(df, column, format=None):
        df[column] = pd.to_datetime(df[column], format=format, errors='coerce')
        return df
