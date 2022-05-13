from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RY(0.21315685, 1))
p.inst(RY(0.13443125, 2))
p.inst(RY(2.5425711, 3))
p.inst(RY(1.3995784, 4))
p.inst(RY(1.8805686, 5))
p.inst(RY(2.0339493, 6))
p.inst(CSWAP(0, 1, 4))
p.inst(CSWAP(0, 2, 5))
p.inst(CSWAP(0, 3, 6))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('7q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
