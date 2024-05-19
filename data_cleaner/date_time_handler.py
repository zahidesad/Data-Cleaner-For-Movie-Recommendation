import pandas as pd

class DateTimeHandler:
    @staticmethod
    def to_datetime(df, column, format=None):
        df[column] = pd.to_datetime(df[column], format=format, errors='coerce')
        return df

    @staticmethod
    def extract_year(df, column, new_column):
        df[new_column] = df[column].dt.year
        return df

    @staticmethod
    def extract_month(df, column, new_column):
        df[new_column] = df[column].dt.month
        return df

    @staticmethod
    def extract_day(df, column, new_column):
        df[new_column] = df[column].dt.day
        return df

    @staticmethod
    def extract_weekday(df, column, new_column):
        df[new_column] = df[column].dt.weekday
        return df

    @staticmethod
    def extract_hour(df, column, new_column):
        df[new_column] = df[column].dt.hour
