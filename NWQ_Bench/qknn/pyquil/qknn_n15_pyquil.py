from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RY(0.27466857, 1))
p.inst(RY(0.9919349, 2))
p.inst(RY(0.1085488, 3))
p.inst(RY(2.6658346, 4))
p.inst(RY(2.6766281, 5))
p.inst(RY(0.24565172, 6))
p.inst(RY(2.9270122, 7))
p.inst(RY(0.16299404, 8))
p.inst(RY(2.3066568, 9))
p.inst(RY(1.5632304, 10))
p.inst(RY(0.523205, 11))
p.inst(RY(0.80548265, 12))
p.inst(RY(1.994984, 13))
p.inst(RY(2.6026488, 14))
p.inst(CSWAP(0, 1, 8))
p.inst(CSWAP(0, 2, 9))
p.inst(CSWAP(0, 3, 10))
p.inst(CSWAP(0, 4, 11))
p.inst(CSWAP(0, 5, 12))
p.inst(CSWAP(0, 6, 13))
p.inst(CSWAP(0, 7, 14))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('15q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
