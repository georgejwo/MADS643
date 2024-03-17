def clean_file(file1, file2):
    """
    Clean and merge file
 
    Args:
        file1 (str): The first file.

        file2 (str): The second file.

    Returns:
        DataFrame: pandas dataframe.
    """
    import datetime as dt
    import pandas as pd
    f1 = pd.read_csv(str(file1))
    f2 = pd.read_csv(str(file2))
    combined = pd.merge(f1, f2, on = 'respondent_id')
    combined['birthdate'] = combined['birthdate'].apply(
        lambda x: dt.datetime(year=int(str(x)[-4:]), month=int(str(x)[:-6]), day=int(str(x)[-6:-4])))
    return combined

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help = 'file1')
    parser.add_argument('input2', help = 'file2')
    parser.add_argument('output', help = 'combined')
    args = parser.parse_args()
    cleanned = clean_file(args.input1, args.input2)
    cleanned.to_csv(args.output, index = False)
