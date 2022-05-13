from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RX
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=1)

p.inst(H(0))
p.inst(RX(-3.6924814, 1))
p.inst(RX(5.4291652, 2))
p.inst(RX(1.3594796, 3))
p.inst(RX(-5.9123043, 4))
p.inst(RX(-0.13186279, 5))
p.inst(RX(-4.3869008, 6))
p.inst(RX(4.9830092, 7))
p.inst(RX(-1.4181518, 8))
p.inst(RX(3.9058792, 9))
p.inst(RX(2.1483107, 10))
p.inst(RX(-1.552265, 11))
p.inst(RX(3.5437778, 12))
p.inst(RX(-3.2923147, 13))
p.inst(RX(5.6875289, 14))
p.inst(RX(1.2065807, 15))
p.inst(RX(-6.0041031, 16))
p.inst(RX(0.50271205, 17))
p.inst(RX(-4.1172873, 18))
p.inst(RX(4.8261369, 19))
p.inst(RX(-1.5885531, 20))
p.inst(RX(3.2780951, 21))
p.inst(RX(2.2125048, 22))
p.inst(RX(-2.1338861, 23))
p.inst(RX(2.9294436, 24))
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
