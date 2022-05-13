from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RY(0.93346815, 1))
p.inst(RY(0.82988213, 2))
p.inst(RY(1.181111, 3))
p.inst(RY(1.802503, 4))
p.inst(RY(2.969805, 5))
p.inst(RY(1.5765553, 6))
p.inst(RY(1.8340893, 7))
p.inst(RY(2.741925, 8))
p.inst(RY(1.5106361, 9))
p.inst(RY(0.76354036, 10))
p.inst(RY(0.15484631, 11))
p.inst(RY(1.9311432, 12))
p.inst(RY(0.69057517, 13))
p.inst(RY(0.74294505, 14))
p.inst(RY(0.79338648, 15))
p.inst(RY(1.9075145, 16))
p.inst(RY(2.5852457, 17))
p.inst(RY(1.5388629, 18))
p.inst(RY(0.8484669, 19))
p.inst(RY(1.9789905, 20))
p.inst(RY(1.177473, 21))
p.inst(RY(0.46112786, 22))
p.inst(RY(0.17065064, 23))
p.inst(RY(1.8262873, 24))
p.inst(CSWAP(0, 1, 13))
p.inst(CSWAP(0, 2, 14))
p.inst(CSWAP(0, 3, 15))
p.inst(CSWAP(0, 4, 16))
p.inst(CSWAP(0, 5, 17))
p.inst(CSWAP(0, 6, 18))
p.inst(CSWAP(0, 7, 19))
p.inst(CSWAP(0, 8, 20))
p.inst(CSWAP(0, 9, 21))
p.inst(CSWAP(0, 10, 22))
p.inst(CSWAP(0, 11, 23))
p.inst(CSWAP(0, 12, 24))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('25q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
