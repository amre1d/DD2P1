import csv
from pathlib import Path

infile = Path("results") / "inverter_delay_vs_load_midpoint.csv"
rows = list(csv.DictReader(infile.open()))

print("Data loaded for midpoint inverter delay plot:")
for row in rows:
    print(
        row["cell"],
        row["load_pf"],
        row["tphl_ns"],
        row["tplh_ns"],
        row["avg_delay_ns"]
    )
