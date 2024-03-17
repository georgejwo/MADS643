from clean import load_data
from draw import plot_column
import matplotlib.pyplot as plt

def main(file_path: str, column: str):
    """
    Main function to load data, clean it, and plot a column.

    Parameters:
    file_path (str): The path to the CSV file.
    column (str): The column for which to calculate the mean.
    """
    df = load_data(file_path)
    plot_column(df, column)
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help = 'csv filename')
    parser.add_argument('input2', help = 'column name')
    args = parser.parse_args()
    main(args.input1, args.input2)
