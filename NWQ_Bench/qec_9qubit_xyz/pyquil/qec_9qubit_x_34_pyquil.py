from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=16)

p.inst(H(0))
p.inst(CNOT(0, 3))
p.inst(CNOT(0, 6))
p.inst(H(0))
p.inst(H(3))
p.inst(H(6))
p.inst(CNOT(0, 1))
p.inst(CNOT(3, 4))
p.inst(CNOT(6, 7))
p.inst(CNOT(0, 2))
p.inst(CNOT(3, 5))
p.inst(CNOT(6, 8))
p.inst(CNOT(0, 18))
p.inst(CNOT(1, 18))
p.inst(CNOT(1, 19))
p.inst(CNOT(2, 19))
p.inst(CNOT(3, 20))
p.inst(CNOT(4, 20))
p.inst(CNOT(4, 21))
p.inst(CNOT(5, 21))
p.inst(CNOT(6, 22))
p.inst(CNOT(7, 22))
p.inst(CNOT(7, 23))
p.inst(CNOT(8, 23))
p.inst(MEASURE(18, ro[0]))
p.inst(MEASURE(19, ro[1]))
p.inst(MEASURE(20, ro[2]))
p.inst(MEASURE(21, ro[3]))
p.inst(MEASURE(22, ro[4]))
p.inst(MEASURE(23, ro[5]))
p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(H(5))
p.inst(H(6))
p.inst(H(7))
p.inst(H(8))
p.inst(CNOT(0, 24))
p.inst(CNOT(3, 25))
p.inst(CNOT(1, 24))
p.inst(CNOT(4, 25))
p.inst(CNOT(2, 24))
p.inst(CNOT(5, 25))
p.inst(CNOT(3, 24))
p.inst(CNOT(6, 25))
p.inst(CNOT(4, 24))
p.inst(CNOT(7, 25))
p.inst(CNOT(5, 24))
p.inst(CNOT(8, 25))
p.inst(MEASURE(24, ro[6]))
p.inst(MEASURE(25, ro[7]))
p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(H(5))
p.inst(H(6))
p.inst(H(7))
p.inst(H(9))
p.inst(CNOT(9, 12))
p.inst(CNOT(9, 15))
p.inst(H(9))
p.inst(H(12))
p.inst(H(15))
p.inst(CNOT(9, 10))
p.inst(CNOT(12, 13))
p.inst(CNOT(15, 16))
p.inst(CNOT(9, 11))
p.inst(CNOT(12, 14))
p.inst(CNOT(15, 17))
p.inst(CNOT(9, 26))
p.inst(CNOT(10, 26))
p.inst(CNOT(10, 27))
p.inst(CNOT(11, 27))
p.inst(CNOT(12, 28))
p.inst(CNOT(13, 28))
p.inst(CNOT(13, 29))
p.inst(CNOT(14, 29))
p.inst(CNOT(15, 30))
p.inst(CNOT(16, 30))
p.inst(CNOT(16, 31))
p.inst(CNOT(17, 31))
p.inst(MEASURE(26, ro[8]))
p.inst(MEASURE(27, ro[9]))
p.inst(MEASURE(28, ro[10]))
p.inst(MEASURE(29, ro[11]))
p.inst(MEASURE(30, ro[12]))
p.inst(MEASURE(31, ro[13]))
p.inst(H(9))
p.inst(H(10))
p.inst(H(11))
p.inst(H(12))
p.inst(H(13))
p.inst(H(14))
p.inst(H(15))
p.inst(H(16))
p.inst(H(17))
p.inst(CNOT(9, 32))
p.inst(CNOT(12, 33))
p.inst(CNOT(10, 32))
p.inst(CNOT(13, 33))
p.inst(CNOT(11, 32))
p.inst(CNOT(14, 33))
p.inst(CNOT(12, 32))
p.inst(CNOT(15, 33))
p.inst(CNOT(13, 32))
p.inst(CNOT(16, 33))
p.inst(CNOT(14, 32))
p.inst(CNOT(17, 33))
p.inst(MEASURE(32, ro[14]))
p.inst(MEASURE(33, ro[15]))
p.inst(H(9))
p.inst(H(10))
p.inst(H(11))
p.inst(H(12))
p.inst(H(13))
p.inst(H(14))
p.inst(H(15))
p.inst(H(16))

p.wrap_in_numshots_loop(shots)

qc = get_qc('34q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
