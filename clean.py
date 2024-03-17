import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data.
    """
    if file_path[-4:] == ".csv":
        df = pd.read_csv(file_path)
    else:
        raise Exception("Sorry, need csv file")
    df = df.dropna()
    return df
    