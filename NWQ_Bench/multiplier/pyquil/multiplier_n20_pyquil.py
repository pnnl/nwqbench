from pyquil import Program, get_qc
from pyquil.gates import CCNOT, CNOT, MEASURE, X
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=4)

p.inst(X(13))
p.inst(X(16))
p.inst(X(17))
p.inst(CCNOT(16, 12, 1))
p.inst(CCNOT(1, 2, 3))
p.inst(CCNOT(16, 13, 4))
p.inst(CNOT(1, 2))
p.inst(CCNOT(4, 5, 6))
p.inst(CCNOT(16, 14, 7))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(4, 5))
p.inst(CCNOT(7, 8, 9))
p.inst(CCNOT(16, 15, 10))
p.inst(CCNOT(3, 5, 6))
p.inst(CNOT(7, 8))
p.inst(CNOT(10, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(9, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CCNOT(7, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CNOT(6, 8))
p.inst(CCNOT(3, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CCNOT(4, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 2))
p.inst(CCNOT(16, 12, 1))
p.inst(CCNOT(1, 2, 3))
p.inst(CCNOT(16, 13, 4))
p.inst(CNOT(1, 2))
p.inst(CCNOT(16, 14, 7))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(16, 15, 10))
p.inst(CCNOT(17, 12, 4))
p.inst(CCNOT(4, 5, 6))
p.inst(CCNOT(17, 13, 7))
p.inst(CNOT(4, 5))
p.inst(CCNOT(7, 8, 9))
p.inst(CCNOT(17, 14, 10))
p.inst(CCNOT(3, 5, 6))
p.inst(CNOT(7, 8))
p.inst(CNOT(10, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(9, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CCNOT(7, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CNOT(6, 8))
p.inst(CCNOT(3, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CCNOT(4, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(17, 12, 4))
p.inst(CNOT(1, 2))
p.inst(CCNOT(4, 5, 6))
p.inst(CCNOT(17, 13, 7))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(4, 5))
p.inst(CCNOT(17, 14, 10))
p.inst(CNOT(1, 2))
p.inst(CCNOT(18, 12, 7))
p.inst(CNOT(0, 2))
p.inst(CCNOT(7, 8, 9))
p.inst(CCNOT(18, 13, 10))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(7, 8))
p.inst(CNOT(10, 11))
p.inst(CNOT(1, 2))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(3, 5, 6))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(9, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CCNOT(7, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CNOT(6, 8))
p.inst(CCNOT(3, 5, 6))
p.inst(CCNOT(18, 12, 7))
p.inst(CNOT(4, 5))
p.inst(CCNOT(7, 8, 9))
p.inst(CCNOT(18, 13, 10))
p.inst(CCNOT(4, 5, 6))
p.inst(CNOT(7, 8))
p.inst(CCNOT(19, 12, 10))
p.inst(CNOT(4, 5))
p.inst(CNOT(10, 11))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(4, 5, 6))
p.inst(CNOT(1, 2))
p.inst(CNOT(4, 5))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 2))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CCNOT(0, 2, 3))
p.inst(CCNOT(3, 5, 6))
p.inst(CCNOT(6, 8, 9))
p.inst(CNOT(9, 11))
p.inst(CCNOT(6, 8, 9))
p.inst(CCNOT(19, 12, 10))
p.inst(CNOT(7, 8))
p.inst(CCNOT(7, 8, 9))
p.inst(CNOT(7, 8))
p.inst(CNOT(6, 8))
p.inst(CCNOT(3, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CCNOT(4, 5, 6))
p.inst(CNOT(4, 5))
p.inst(CNOT(3, 5))
p.inst(CCNOT(0, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CCNOT(1, 2, 3))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 2))
p.inst(MEASURE(2, ro[0]))
p.inst(MEASURE(5, ro[1]))
p.inst(MEASURE(8, ro[2]))
p.inst(MEASURE(11, ro[3]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('20q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
