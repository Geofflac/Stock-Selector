from project import is_normal, is_profitable_5, get_symbol, get_close_volume
import numpy as np
import pandas as pd
import re

def test_get_close_volume():
    df = get_close_volume("MC.PA OR.PA MRK.PA RMS.PA CDI.PA TTE.PA", "1y", "1d")
    assert df.isnull().values.any() == False

def test_get_symbole():
    r = re.compile('.*')
    s = get_symbol("FR")
    assert r.match(s) != None

def test_is_normal():
    df = pd.DataFrame({
    'Col_1': np.random.normal(0, 2, 3000),
    'Col_2': np.random.uniform(5, 3, 3000)
    })
    assert is_normal(df['Col_1']) == True
    assert is_normal(df['Col_2']) == False

def test_is_profitable_5():
    df = pd.DataFrame({
    'Col_1': [5,5,5,5,5,5,5,5,5,0.1],
    'Col_2': [5,5,5,5,5,5,5,5,5,20]
    })
    assert is_profitable_5(df['Col_1']) == True
    assert is_profitable_5(df['Col_2']) == False






