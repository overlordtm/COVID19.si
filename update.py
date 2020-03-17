import tools.importer

SHEET_ID = "1GDYUsjtJMub8Gh_hZMu4UQw6hAVmtUh6E0rS9dlUl3o"
RANGE_STATS = "Statistika!A3:BT"

if __name__ == "__main__":
    tools.importer.sheet2csv(
        id=SHEET_ID, range=RANGE_STATS, filename="data/full.csv",
    )

