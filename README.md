# DD2P1

Standard Cell Library Design and Characterization using SKY130 and ngspice.

## Implemented cells

### Inverter family
- invx1
- invx2
- invx4
- invx8

### NAND2 family
- nand2x1
- nand2x2
- nand2x4

### NOR2 family
- nor2x1
- nor2x2
- nor2x4

### MAJ3 family
- maj3x1
- maj3x2
- maj3x4

## Current progress
- Ubuntu environment prepared
- ngspice installed and verified
- SKY130 device models connected successfully
- Standard cell SPICE library created
- One characterization point completed for each required cell
- Summary CSV files generated
- Inverter midpoint delay plot generated
- Initial automation script created for characterization planning
- Inverter batch netlists generated automatically

## Repository structure
- `spice_lib/` : standard cell SPICE library
- `testbenches/` : manual characterization testbenches
- `scripts/` : automation and plotting scripts
- `results/` : generated CSV files, netlists, and plots

## Main result files
- `results/characterization_summary.csv`
- `results/inverter_summary.csv`
- `results/inverter_delay_vs_load_midpoint.csv`
- `results/inverter_delay_plot.png`
- `results/characterization_plan.csv`

## Notes
This repository currently contains the implemented cells, successful sample characterization runs, summary data, and starter automation. The next stage is extending the automation flow to run all characterization combinations and export full timing tables.
