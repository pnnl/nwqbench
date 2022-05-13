from pyquil import Program, get_qc
from pyquil.gates import CNOT, CCNOT, MEASURE, X
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=20)

p.inst(X(1))
p.inst(X(2))
p.inst(X(3))
p.inst(X(4))
p.inst(X(8))
p.inst(CNOT(0, 4))
p.inst(CNOT(0, 8))
p.inst(CCNOT(8, 4, 0))
p.inst(CNOT(1, 5))
p.inst(CNOT(1, 0))
p.inst(CCNOT(0, 5, 1))
p.inst(CNOT(2, 6))
p.inst(CNOT(2, 1))
p.inst(CCNOT(1, 6, 2))
p.inst(CNOT(3, 7))
p.inst(CNOT(3, 2))
p.inst(CCNOT(2, 7, 3))
p.inst(CNOT(3, 9))
p.inst(CCNOT(2, 7, 3))
p.inst(CNOT(3, 2))
p.inst(CNOT(2, 7))
p.inst(CCNOT(1, 6, 2))
p.inst(CNOT(2, 1))
p.inst(CNOT(1, 6))
p.inst(CCNOT(0, 5, 1))
p.inst(CNOT(1, 0))
p.inst(CNOT(0, 5))
p.inst(CCNOT(8, 4, 0))
p.inst(CNOT(0, 8))
p.inst(CNOT(8, 4))
p.inst(MEASURE(0, ro[10]))
p.inst(MEASURE(1, ro[11]))
p.inst(MEASURE(2, ro[12]))
p.inst(MEASURE(3, ro[13]))
p.inst(MEASURE(4, ro[14]))
p.inst(MEASURE(5, ro[15]))
p.inst(MEASURE(6, ro[16]))
p.inst(MEASURE(7, ro[17]))
p.inst(MEASURE(8, ro[18]))
p.inst(MEASURE(9, ro[19]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('10q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
