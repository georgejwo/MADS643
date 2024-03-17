import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def make_pipeline():
    # Replace this and the line below with your code.
    # The function should return a sklearn pipeline.
    #raise NotImplementedError
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import RandomForestRegressor
    num_feats = ['permit_lot_size']
    num_trans = Pipeline(steps = [('imputer', SimpleImputer(strategy = 'median')), ('scaler', StandardScaler())])
    cat_feats = ['permit_type', 'permit_subtype']
    cat_trans = Pipeline(steps = [('imputer', SimpleImputer(strategy = 'constant', fill_value='missing')),
    ('ohe', OneHotEncoder(handle_unknown='ignore'))])
    preprocessor = ColumnTransformer(transformers=[('num', num_trans, num_feats), ('cat', cat_trans, cat_feats)])
    pipe = Pipeline(steps=[("prepcocessor", preprocessor), ("regressor", RandomForestRegressor())])
    return pipe


def train(data_frame):
    # We are predicting the wait time
    y = (data_frame["issued_date"] - data_frame["submitted_date"]).dt.days

    # Drop columns in dataframe that shouldn't be used to predict wait time
    x = data_frame.drop(
        [
            "issued_date",
            "submitted_date",
        ],
        axis=1,
    )

    # Split data into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

    trained_model = make_pipeline()

    trained_model.fit(x_train, y_train)

    # Store model metrics in a dictionary
    model_metrics = {
        "train_data": {
            "score": trained_model.score(x_train, y_train),
            "mae": mean_absolute_error(y_train, trained_model.predict(x_train)),
        },
        "test_data": {
            "score": trained_model.score(x_test, y_test),
            "mae": mean_absolute_error(y_test, trained_model.predict(x_test)),
        },
    }
    print(model_metrics)

    return trained_model


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="cleaned data file (CSV)")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display metrics",
    )
    args = parser.parse_args()

    input_data = pd.read_csv(
        args.input_file,
        parse_dates=["submitted_date", "issued_date"],
    )

    model = train(input_data)
