class OutlierHandler:
    def __init__(self, threshold=1.5):
        self.threshold = threshold

    def fit_transform(self, data, column):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - self.threshold * IQR
        upper_bound = Q3 + self.threshold * IQR
        outliers = (data[column] < lower_bound) | (data[column] > upper_bound)
        data.loc[outliers, column] = None
        return data
