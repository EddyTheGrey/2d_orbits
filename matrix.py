import pandas as pd
import numpy as np

def create_matrix(rows, cols):
    """Creates a matrix of zeros with the specified number of rows and columns."""
    return np.zeros((rows, cols))

def create_dataframe(rows, cols):
    """Creates a DataFrame of zeros with the specified number of rows and columns."""
    return pd.DataFrame(np.zeros((rows, cols)))

def update_matrix(matrix, row, col, value):
    """Updates the value at the specified row and column in the matrix."""
    if 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]:
        matrix[row, col] = value
    else:
        raise IndexError("Row or column index out of bounds.")
    
def update_dataframe(df, row, col, value):
    """Updates the value at the specified row and column in the DataFrame."""
    if 0 <= row < df.shape[0] and 0 <= col < df.shape[1]:
        df.iat[row, col] = value
    else:
        raise IndexError("Row or column index out of bounds.")

