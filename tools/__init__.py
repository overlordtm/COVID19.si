import pandas as pd
from functools import reduce


def parse_csv(filename):
    df = pd.read_csv(
        filename,
        parse_dates=["Date"],
        index_col=False,
        # index_col=0,
        dayfirst=True,
        header=0,
        low_memory=False,
        dtype=float,
    )
    return df.apply(pd.to_numeric)


def export_csv(frame, filename):
    with open(filename, "w+") as f:
        return frame.to_csv(f, sep=",", encoding="utf-8")

