import sys
sys.path.append("..\\data_cleaner")

import unittest
import pandas as pd
from data_cleaner.missing_value_handler import MissingValueHandler

class TestMissingValueHandler(unittest.TestCase):
    def setUp(self):
        data = {
            'ColumnWithMissingValues': [1, 2, None, 4],
            'AnotherColumn': [10, 20, 30, 40]
        }
        self.df = pd.DataFrame(data)

    def test_impute_mean(self):
        df = self.df.copy()
        MissingValueHandler.impute(df, 'ColumnWithMissingValues', strategy='mean')
        self.assertAlmostEqual(df['ColumnWithMissingValues'].iloc[2], 2.333, places=3)

    def test_delete_rows(self):
        df = self.df.copy()
        result = MissingValueHandler.delete_rows(df, ['ColumnWithMissingValues'])
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
