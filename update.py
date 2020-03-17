import tools.importer

SHEET_ID_DEV = "1GDYUsjtJMub8Gh_hZMu4UQw6hAVmtUh6E0rS9dlUl3o"
SHEET_ID_PROD = "1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY"

SHEET_ID = SHEET_ID_PROD

RANGE_STATS = "Statistika!A3:BT"

if __name__ == "__main__":
    tools.importer.sheet2csv(
        id=SHEET_ID, range=RANGE_STATS, filename="data/full.csv",
    )

