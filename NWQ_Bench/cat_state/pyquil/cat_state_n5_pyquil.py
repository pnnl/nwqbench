from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=10)

p.inst(H(0))
p.inst(CNOT(0, 1))
p.inst(CNOT(1, 2))
p.inst(CNOT(2, 3))
p.inst(CNOT(3, 4))
p.inst(MEASURE(0, ro[5]))
p.inst(MEASURE(1, ro[6]))
p.inst(MEASURE(2, ro[7]))
p.inst(MEASURE(3, ro[8]))
p.inst(MEASURE(4, ro[9]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
