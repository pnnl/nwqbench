from pyquil import Program, get_qc
from pyquil.gates import CCNOT, CNOT, MEASURE, X
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=2)

p.inst(X(6))
p.inst(X(9))
p.inst(CCNOT(8, 6, 1))
p.inst(CCNOT(1, 2, 3))
p.inst(CCNOT(8, 7, 4))
p.inst(CNOT(1, 2))
p.inst(CNOT(4, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 2))
p.inst(CCNOT(8, 6, 1))
p.inst(CCNOT(1, 2, 3))
p.inst(CCNOT(8, 7, 4))
p.inst(CNOT(1, 2))
p.inst(CCNOT(9, 6, 4))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(4, 5))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(9, 6, 4))
p.inst(CNOT(1, 2))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 2))
p.inst(MEASURE(2, ro[0]))
p.inst(MEASURE(5, ro[1]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('10q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
