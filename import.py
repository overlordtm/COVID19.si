from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dateutil import parser
import csv
import os
import os.path
import sys


def api_key():
    api_key = os.environ["GOOGLE_API_KEY"]

    if not api_key:
        raise Exception("No GOOGLE_API_KEY in env")
    else:
        return api_key


service = build("sheets", "v4", developerKey=api_key())
sheet = service.spreadsheets()


def parse_date(datestr):
    parser.isoparse(datestr[0:10]).date()


def cell_index(letter):
    letter = letter.lower()
    if len(letter) == 1:
        return ord(letter) - ord("a")
    elif len(letter) == 2:
        return (ord(letter[0]) - ord("a")) * 26 + ord(letter[1]) - ord("a") + 26
    else:
        raise Exception("Unsupported cell index")


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
                writer.writerow(row)
            except Exception as e:
                print("import_cases: Failed to parse row: {}".format(row))


def import_stats(filename="covid19-slovenia-full.csv"):
    result = (
        sheet.values()
        .get(
            spreadsheetId="1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY",
            range="Statistika!A3:BP",
        )
        .execute()
    )
    values = result.get("values", [])

    if not values:
        raise Exception("No data found.")
    else:
        with open(filename, "w", newline="") as csvfile:

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
                    "region_lj",
                    "region_nm",
                    "region_ce",
                    "region_mb",
                    "region_kr",
                    "region_po",
                    "region_kp",
                    "region_ms",
                    "region_ng",
                    "region_sg",
                    "region_kk",
                    "region_foreign",
                    "region_unknown",
                ]
                + list(map(lambda g: "age_{}".format(g), age_groups))
                + list(map(lambda g: "female_age_{}".format(g), age_groups))
                + list(map(lambda g: "male_age_{}".format(g), age_groups))
                + ["source_ita", "source_aut", "source_esp", "source_slo"]
                + [
                    "workers_ukc_lj",
                    "workers_ukc_mb",
                    "workers_zd_m",
                    "workers_b_ms",
                    "workers_b_ng",
                ]
            )

            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            writer.writerow(fieldnames)
            for row in values:
                day_of_outbreak = row[cell_index("A")]
                date = parse_date(row[cell_index("B")])
                pandemic_phase = row[cell_index("C")]
                tests_performed_cum = row[cell_index("D")]
                tests_performed_day = row[cell_index("F")]
                positive_tests_cum = row[cell_index("H")]
                positive_tests_day = row[cell_index("J")]
                count_in_care = row[cell_index("L")]
                count_in_hospital = row[cell_index("M")]
                count_in_icu = row[cell_index("N")]
                count_in_icu_bad = row[cell_index("O")]
                deaths_cum = row[cell_index("P")]

                reginal_data = row[cell_index("Z") : cell_index("AL") + 1]

                by_age = row[cell_index("AN") : cell_index("AR") + 1]
                by_age_female = row[cell_index("AT") : cell_index("AX") + 1]
                by_age_male = row[cell_index("AZ") : cell_index("BD") + 1]

                by_source = row[cell_index("BF") : cell_index("BI") + 1]

                workers = row[cell_index("BK") : cell_index("BO") + 1]

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
                    + reginal_data
                    + by_age
                    + by_age_female
                    + by_age_male
                    + by_source
                )

                writer.writerow(csvrow)


if __name__ == "__main__":
    import_stats("data/full.csv")
    import_cases("data/cases.csv")
