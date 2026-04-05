import csv
from pathlib import Path
import matplotlib.pyplot as plt

infile = Path("results") / "inverter_delay_vs_load_midpoint.csv"
rows = list(csv.DictReader(infile.open()))

cells = [row["cell"] for row in rows]
avg_delay = [float(row["avg_delay_ns"]) for row in rows]

plt.figure(figsize=(7, 4.5))
plt.plot(cells, avg_delay, marker="o")
plt.xlabel("Cell")
plt.ylabel("Average delay (ns)")
plt.title("Inverter Delay at Midpoint Load Condition")
plt.grid(True)
plt.tight_layout()

out = Path("results") / "inverter_delay_plot.png"
plt.savefig(out, dpi=200)
print(f"Saved: {out}")
