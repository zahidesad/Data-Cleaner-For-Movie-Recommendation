class MissingValueHandler:
    def __init__(self, strategy='mean', constant_value=None):
        self.strategy = strategy
        self.constant_value = constant_value

    def fit_transform(self, data, column):
        if self.strategy == 'mean':
            return data.fillna(data[column].mean())
        elif self.strategy == 'median':
            return data.fillna(data[column].median())
        elif self.strategy == 'constant':
            if self.constant_value is None:
                raise ValueError("Please provide a constant value for the 'constant' strategy.")
            return data.fillna(self.constant_value)
        elif self.strategy == 'delete':
            return data.dropna()
        else:
            raise ValueError("Invalid strategy. Please choose from 'mean', 'median', 'constant', or 'delete'.")

    def remove_column(self, data, column):
        return data.drop(column, axis=1)


