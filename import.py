from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dateutil import parser
import csv
import os
import os.path
import sys

# old legacy stuff


def api_key():
    api_key = os.environ["GOOGLE_API_KEY"]

    if not api_key:
        raise Exception("No GOOGLE_API_KEY in env")
    else:
        return api_key


service = build("sheets", "v4", developerKey=api_key())
sheet = service.spreadsheets()


def parse_date(datestr):
    return parser.isoparse(datestr[0:10]).date()


def cell_index(letter):
    # ord(a) = 97
    letter = letter.lower()
    if len(letter) == 1:
        return ord(letter) - 97
    elif len(letter) == 2:
        return (ord(letter[0]) - 97) * 26 + ord(letter[1]) - 97 + 26
    else:
        raise Exception("Unsupported cell index")


def col_name(idx):
    i2 = idx // 26
    i1 = idx % 26
    if i2 > 0:
        return "{}{}".format(chr(97 + i2), chr(97 + i1))
    else:
        return chr(97 + i1)


def pad(lst, l):
    if len(lst) == 0:
        return [""] * l
    if len(lst) < l:
        lst.extend([""] * (l - len(lst)))
        return lst
    else:
        return lst


def get_range(row, col_start, col_end):
    desired_len = cell_index(col_end) - cell_index(col_start) + 1
    data = row[cell_index(col_start) : cell_index(col_end) + 1]
    padded = pad(data, desired_len)
    return padded


def import_cases(filename="covid19-slovenia-cases.csv"):
    result = (
        sheet.values()
        .get(
            spreadsheetId="1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY",
            range="Primeri!A2:I",
        )
        .execute()
    )
    values = result.get("values", [])

    if not values:
        raise Exception("No data found.")

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

        fieldnames = [
            "case #",
            "date",
            "region",
            "city",
            "source",
            "desc",
            "cluster",
            "state",
            "news_source",
        ]

        writer.writerow(fieldnames)

        for row in values:
            try:
                row[1] = parse_date(row[1])
                prow = pad(row, 9)
                writer.writerow(prow)
            except Exception as e:
                print("import_cases: Failed to parse row: {} {}".format(row, e))


def import_stats(filename="covid19-slovenia-full.csv"):
    result = (
        sheet.values()
        .get(
            spreadsheetId="1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY",
            range="Statistika!A2:BS",
        )
        .execute()
    )
    values = result.get("values", [])

    if not values:
        raise Exception("No data found.")
    else:
        with open(filename, "w", newline="") as csvfile:

            # find columns
            headers = values[0]
            COL_DAY_OF_OUTBREAK = headers.index("dan")
            COL_DATE = headers.index("datum")
            COL_PANDEMIC_PHASE = 2
            COL_TESTS_PERFORMED_CUM = headers.index("testov")
            COL_TESTS_PERFORMED_DAY = headers.index("testov na dan")
            COL_POSITIVE_TESTS_CUM = headers.index("potrjeni")
            COL_POSITIVE_TESTS_DAY = headers.index("novi potrjeni")
            COL_COUNT_IN_CARE = headers.index("v zdr. oskrbi")
            COL_COUNT_IN_HOSPITAL = headers.index("hospitalizirano")
            COL_COUNT_IN_ICU = headers.index("intenzivna nega ICU")
            COL_COUNT_IN_ICU_BAD = headers.index("kritično stanje")
            COL_DEATHS_CUM = headers.index("umrli")

            regions = get_range(headers, "AA", "AM")
            facilities = get_range(headers, "BL", "BR")
            age_groups = ["0-15", "16-29", "30-49", "50-59", "60+"]

            fieldnames = (
                [
                    "day_of_outbreak",
                    "date",
                    "pandemic_phase",
                    "tests_performed_cum",
                    "tests_performed_day",
                    "positive_tests_cum",
                    "positive_tests_day",
                    "count_in_care",
                    "count_in_hospital",
                    "count_in_icu",
                    "count_in_icu_bad",
                    "deaths_cum",
                ]
                + list(map(lambda g: "region_{}".format(g), regions))
                + list(map(lambda g: "age_{}".format(g), age_groups))
                + list(map(lambda g: "female_age_{}".format(g), age_groups))
                + list(map(lambda g: "male_age_{}".format(g), age_groups))
                + ["source_ita", "source_aut", "source_esp", "source_slo"]
                + list(map(lambda g: "facility_{}".format(g.lower()), facilities))
            )

            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)

            for row in values[1:]:
                row = pad(row, len(headers))
                try:
                    day_of_outbreak = row[COL_DAY_OF_OUTBREAK]
                    date = parse_date(row[COL_DATE])
                    pandemic_phase = row[COL_PANDEMIC_PHASE]
                    tests_performed_cum = row[COL_TESTS_PERFORMED_CUM]
                    tests_performed_day = row[COL_TESTS_PERFORMED_DAY]
                    positive_tests_cum = row[COL_POSITIVE_TESTS_CUM]
                    positive_tests_day = row[COL_POSITIVE_TESTS_DAY]
                    count_in_care = row[COL_COUNT_IN_CARE]
                    count_in_hospital = row[COL_COUNT_IN_HOSPITAL]
                    count_in_icu = row[COL_COUNT_IN_ICU]
                    count_in_icu_bad = row[COL_COUNT_IN_ICU_BAD]
                    deaths_cum = row[COL_DEATHS_CUM]

                    regional_data = get_range(row, "AA", "AM")

                    by_age = get_range(row, "AO", "AS")
                    by_age_female = get_range(row, "AU", "AY")
                    by_age_male = get_range(row, "BA", "BE")

                    by_source = get_range(row, "BG", "BJ")

                    workers = get_range(row, "BL", "BR")

                    csvrow = (
                        [
                            day_of_outbreak,
                            date,
                            pandemic_phase,
                            tests_performed_cum,
                            tests_performed_day,
                            positive_tests_cum,
                            positive_tests_day,
                            count_in_care,
                            count_in_hospital,
                            count_in_icu,
                            count_in_icu_bad,
                            deaths_cum,
                        ]
                        + regional_data
                        + by_age
                        + by_age_female
                        + by_age_male
                        + by_source
                        + workers
                    )
                    writer.writerow(csvrow)
                except IndexError as e:
                    print(e)
                    print(row)


if __name__ == "__main__":
    import_stats("data/full.csv")
    import_cases("data/cases.csv")
