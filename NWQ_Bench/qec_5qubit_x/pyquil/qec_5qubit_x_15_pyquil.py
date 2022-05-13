from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=6)

p.inst(H(0))
p.inst(CNOT(0, 1))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 3))
p.inst(CNOT(1, 3))
p.inst(CNOT(1, 4))
p.inst(CNOT(1, 4))
p.inst(MEASURE(3, ro[0]))
p.inst(MEASURE(4, ro[1]))
p.inst(H(5))
p.inst(CNOT(5, 6))
p.inst(CNOT(6, 7))
p.inst(CNOT(5, 8))
p.inst(CNOT(6, 8))
p.inst(CNOT(6, 9))
p.inst(CNOT(6, 9))
p.inst(MEASURE(8, ro[2]))
p.inst(MEASURE(9, ro[3]))
p.inst(H(10))
p.inst(CNOT(10, 11))
p.inst(CNOT(11, 12))
p.inst(CNOT(10, 13))
p.inst(CNOT(11, 13))
p.inst(CNOT(11, 14))
p.inst(CNOT(11, 14))
p.inst(MEASURE(13, ro[4]))
p.inst(MEASURE(14, ro[5]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('15q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
