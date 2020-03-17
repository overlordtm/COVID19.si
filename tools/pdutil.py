import pandas as pd


def read_csv(filename):
    df = pd.read_csv(
        filename,
        parse_dates=["date"],
        index_col=False,
        header=0,
        # dtype=float,
    )
    # return df.apply(pd.to_numeric)
    return df


def to_csv(frame, filename):
    with open(filename, "w+") as f:
        return frame.to_csv(f, sep=",", encoding="utf-8")
