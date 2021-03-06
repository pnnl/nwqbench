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
p.inst(RX(3.5074824, 13))
p.inst(RX(-3.1458178, 14))
p.inst(RX(2.9808713, 15))
p.inst(RX(-4.5722067, 16))
p.inst(RX(-2.9717581, 17))
p.inst(RX(4.3812134, 18))
p.inst(RX(-0.54413824, 19))
p.inst(RX(2.8824416, 20))
p.inst(RX(0.99178896, 21))
p.inst(RX(5.4169858, 22))
p.inst(RX(5.7239307, 23))
p.inst(RX(3.7629698, 24))
p.inst(RX(-4.5485128, 25))
p.inst(RX(-3.2923147, 26))
p.inst(RX(5.6875289, 27))
p.inst(RX(1.2065807, 28))
p.inst(RX(-6.0041031, 29))
p.inst(RX(0.50271205, 30))
p.inst(RX(-4.1172873, 31))
p.inst(RX(4.8261369, 32))
p.inst(RX(-1.5885531, 33))
p.inst(RX(3.2780951, 34))
p.inst(RX(2.2125048, 35))
p.inst(RX(-2.1338861, 36))
p.inst(RX(2.9294436, 37))
p.inst(RX(4.0850493, 38))
p.inst(RX(-2.9631606, 39))
p.inst(RX(2.9322572, 40))
p.inst(RX(-4.3125018, 41))
p.inst(RX(-2.9593885, 42))
p.inst(RX(4.335384, 43))
p.inst(RX(-0.18151701, 44))
p.inst(RX(3.026406, 45))
p.inst(RX(0.67977512, 46))
p.inst(RX(5.3901384, 47))
p.inst(RX(5.4778772, 48))
p.inst(RX(3.2416375, 49))
p.inst(RX(-4.6932636, 50))
p.inst(CSWAP(0, 1, 26))
p.inst(CSWAP(0, 2, 27))
p.inst(CSWAP(0, 3, 28))
p.inst(CSWAP(0, 4, 29))
p.inst(CSWAP(0, 5, 30))
p.inst(CSWAP(0, 6, 31))
p.inst(CSWAP(0, 7, 32))
p.inst(CSWAP(0, 8, 33))
p.inst(CSWAP(0, 9, 34))
p.inst(CSWAP(0, 10, 35))
p.inst(CSWAP(0, 11, 36))
p.inst(CSWAP(0, 12, 37))
p.inst(CSWAP(0, 13, 38))
p.inst(CSWAP(0, 14, 39))
p.inst(CSWAP(0, 15, 40))
p.inst(CSWAP(0, 16, 41))
p.inst(CSWAP(0, 17, 42))
p.inst(CSWAP(0, 18, 43))
p.inst(CSWAP(0, 19, 44))
p.inst(CSWAP(0, 20, 45))
p.inst(CSWAP(0, 21, 46))
p.inst(CSWAP(0, 22, 47))
p.inst(CSWAP(0, 23, 48))
p.inst(CSWAP(0, 24, 49))
p.inst(CSWAP(0, 25, 50))
p.inst(H(0))
p.inst(MEASURE(0, ro[0]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('51q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
