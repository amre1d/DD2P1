import csv
from pathlib import Path

cells = [
    "invx1", "invx2", "invx4", "invx8",
    "nand2x1", "nand2x2", "nand2x4",
    "nor2x1", "nor2x2", "nor2x4",
    "maj3x1", "maj3x2", "maj3x4"
]

input_transitions_ns = [0.0100, 0.0231, 0.0531, 0.1225, 0.2823, 0.6507, 1.5000]
capacitances_pf = [0.0005, 0.0013, 0.0035, 0.0094, 0.0249, 0.0662, 0.1758]

out_path = Path("results") / "characterization_plan.csv"
out_path.parent.mkdir(exist_ok=True)

with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["cell", "input_transition_ns", "load_pf"])
    for cell in cells:
        for tin in input_transitions_ns:
            for load in capacitances_pf:
                writer.writerow([cell, tin, load])

print(f"Saved: {out_path}")
print(f"Total runs: {len(cells) * len(input_transitions_ns) * len(capacitances_pf)}")
