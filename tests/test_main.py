import pandas as pd

def test_dummy():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    assert not df.empty

    # tests/test_main.py import sys import os # Add the src directory to the Python module search path sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))) from main import load_data def test_load_data(): df = load_data() print(f"DataFrame shape: {df.shape}") # Debugging information assert not df.empty, "DataFrame should not be empty"