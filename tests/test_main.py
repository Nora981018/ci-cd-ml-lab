import pandas as pd

def test_dummy():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    assert not df.empty