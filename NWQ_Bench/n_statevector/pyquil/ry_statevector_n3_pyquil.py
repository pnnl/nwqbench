from pyquil import Program, get_qc
from pyquil.gates import RY, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=3)

p.inst(RY(2.1506626, 0))
p.inst(RY(1.4482467, 1))
p.inst(RY(2.3705663, 2))
p.inst(MEASURE(0, ro[0]))
p.inst(MEASURE(1, ro[1]))
p.inst(MEASURE(2, ro[2]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('3q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
