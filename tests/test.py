from . import myoutlierremover
import pandas as pd
import numpy as np


def test_outlier_clipper():
    """
    make sure outlier remover works correctly
    """
    dataframe =  pd.DataFrame({'data': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]})

    assert myoutlierremover.remove_outliers(dataframe,['data'], 1.5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'incorrect'
    assert myoutlierremover.remove_outliers(dataframe,['data']) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'incorrect'
