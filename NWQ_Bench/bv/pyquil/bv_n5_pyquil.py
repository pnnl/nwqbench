from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE, CNOT, X
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=5)

p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(X(4))
p.inst(H(0))
p.inst(H(1))
p.inst(H(4))
p.inst(CNOT(2, 4))
p.inst(H(2))
p.inst(CNOT(3, 4))
p.inst(H(3))
p.inst(MEASURE(0, ro[0]))
p.inst(MEASURE(1, ro[1]))
p.inst(MEASURE(2, ro[2]))
p.inst(MEASURE(3, ro[3]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
