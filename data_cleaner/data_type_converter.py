import pandas as pd


class DataTypeConverter:
    def __init__(self):
        pass

    def convert_to_numeric(self, data, columns, errors='raise'):
        """
        Convert specified columns to numeric types.
        """
        for column in columns:
            data[column] = pd.to_numeric(data[column], errors=errors)
        return data

    def convert_to_categorical(self, data, columns):
        """
        Convert specified columns to categorical types.
        """
        for column in columns:
            data[column] = data[column].astype('category')
        return data
