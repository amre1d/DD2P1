from pathlib import Path

cells = ["invx1", "invx2", "invx4", "invx8"]
input_transitions_ns = [0.0100, 0.0231, 0.0531, 0.1225, 0.2823, 0.6507, 1.5000]
capacitances_pf = [0.0005, 0.0013, 0.0035, 0.0094, 0.0249, 0.0662, 0.1758]

tb_dir = Path("results") / "generated_netlists"
tb_dir.mkdir(parents=True, exist_ok=True)

template = """\
.include "/home/aamreidd/sky130_project/spice_lib/standard_cells.spice"

VDD VPWR 0 1.8
VIN A 0 PULSE(0 1.8 0.1n {tin}n {tin}n 5n 10n)
Cload Y 0 {load}p

XU1 A Y VPWR 0 {cell}

.tran 0.001n 20n

.measure tran tphl trig v(A) val=0.9 rise=1 targ v(Y) val=0.9 fall=1
.measure tran tplh trig v(A) val=0.9 fall=1 targ v(Y) val=0.9 rise=1
.measure tran trise trig v(Y) val=0.36 rise=1 targ v(Y) val=1.44 rise=1
.measure tran tfall trig v(Y) val=1.44 fall=1 targ v(Y) val=0.36 fall=1

.end
"""

count = 0
for cell in cells:
    for tin in input_transitions_ns:
        for load in capacitances_pf:
            tin_str = str(tin).replace(".", "p")
            load_str = str(load).replace(".", "p")
            name = f"{cell}_tin_{tin_str}_load_{load_str}.spice"
            path = tb_dir / name
            path.write_text(template.format(cell=cell, tin=tin, load=load))
            count += 1

print(f"Generated {count} netlists in {tb_dir}")
