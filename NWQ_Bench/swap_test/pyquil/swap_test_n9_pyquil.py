from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RX
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RX(-3.8535372, 1))
p.inst(RX(-4.2592974, 2))
p.inst(RX(0.76934517, 3))
p.inst(RX(5.2757681, 4))
p.inst(RX(-4.3555394, 5))
p.inst(RX(-1.1088457, 6))
p.inst(RX(0.60673656, 7))
p.inst(RX(3.1760628, 8))
p.inst(CSWAP(0, 1, 5))
p.inst(CSWAP(0, 2, 6))
p.inst(CSWAP(0, 3, 7))
p.inst(CSWAP(0, 4, 8))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('9q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
