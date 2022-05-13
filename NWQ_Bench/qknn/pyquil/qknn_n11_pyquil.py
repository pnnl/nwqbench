from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RY(2.8008902, 1))
p.inst(RY(0.69545835, 2))
p.inst(RY(0.099936864, 3))
p.inst(RY(3.078129, 4))
p.inst(RY(0.68494174, 5))
p.inst(RY(0.53728786, 6))
p.inst(RY(3.0576215, 7))
p.inst(RY(0.26289246, 8))
p.inst(RY(1.1357725, 9))
p.inst(RY(0.98289791, 10))
p.inst(CSWAP(0, 1, 6))
p.inst(CSWAP(0, 2, 7))
p.inst(CSWAP(0, 3, 8))
p.inst(CSWAP(0, 4, 9))
p.inst(CSWAP(0, 5, 10))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('11q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
