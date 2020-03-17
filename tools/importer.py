from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dateutil import parser
import csv
import os
import os.path
import sys


class DuplicateColException(Exception):
    def __init__(self, col):
        message = "Duplicate column: {}".format(col)
        super().__init__(message)


def parse_date(datestr):
    return parser.isoparse(datestr[0:10]).date()


def find_duplicates(l):
    # stupid but simple
    return set([x for x in l if l.count(x) > 1])


def sheet2csv(id, range, filename="export.csv"):
    api_key = os.environ["GOOGLE_API_KEY"]

    service = build("sheets", "v4", developerKey=api_key)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=id, range=range).execute()
    values = result.get("values", [])

    if not values:
        raise Exception("No data found.")

    headers = values[0]

    cols = []
    col_map = {}

    for col_idx, col_name in enumerate(headers):
        if col_name:
            cols.append(col_name)
            col_map[col_name] = col_idx

    if len(cols) > len(set(cols)):
        dupe_cols = find_duplicates(cols)
        raise DuplicateColException(dupe_cols)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(cols)

        for row in values[1:]:

            # pad each row with empty values
            row += [""] * (len(cols) - len(row))
            print(row)

            csvrow = []
            for col in cols:
                idx = col_map[col]
                try:
                    if col == "date":
                        cell = parse_date(row[idx])
                    else:
                        cell = row[idx]
                except IndexError:
                    cell = None
                csvrow.append(cell)
            writer.writerow(csvrow)

