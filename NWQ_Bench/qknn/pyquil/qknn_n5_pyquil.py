from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RY(2.2439274, 1))
p.inst(RY(0.38780286, 2))
p.inst(RY(2.8663306, 3))
p.inst(RY(2.209665, 4))
p.inst(CSWAP(0, 1, 3))
p.inst(CSWAP(0, 2, 4))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
