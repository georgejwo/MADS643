import pandas as pd
import seaborn as sns


def plot_column(df: pd.DataFrame, column: str):
    """
    Plot a specific column with numeric or categorical types.

    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.
    column (str): The column for which to calculate the mean.

    Returns:
    line chart or bar chart depending on data type.
    """

    if df[column].dtype != object:
        df[column].plot()

    else:
        sns.countplot(data = df, x = column)
