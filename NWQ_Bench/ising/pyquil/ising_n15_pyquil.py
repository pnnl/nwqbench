from pyquil import Program, get_qc
from pyquil.gates import H, RZ, CNOT, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=30)

p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(H(5))
p.inst(H(6))
p.inst(H(7))
p.inst(H(8))
p.inst(H(9))
p.inst(H(10))
p.inst(H(11))
p.inst(H(12))
p.inst(H(13))
p.inst(H(14))
p.inst(RZ(-1.5002017, 0))
p.inst(RZ(1.5002017, 1))
p.inst(RZ(0.38294136, 2))
p.inst(RZ(-0.38294136, 3))
p.inst(RZ(-0.34345858, 4))
p.inst(RZ(0.34345858, 5))
p.inst(RZ(-0.70756849, 6))
p.inst(RZ(0.70756849, 7))
p.inst(RZ(0.53735569, 8))
p.inst(RZ(-0.53735569, 9))
p.inst(RZ(0.758994, 10))
p.inst(RZ(-0.758994, 11))
p.inst(RZ(0.61260149, 12))
p.inst(RZ(-0.61260149, 13))
p.inst(RZ(1.1049346, 14))
p.inst(RZ(1.5002017, 1))
p.inst(RZ(-0.38294136, 3))
p.inst(RZ(0.34345858, 5))
p.inst(RZ(0.70756849, 7))
p.inst(RZ(-0.53735569, 9))
p.inst(RZ(-0.758994, 11))
p.inst(RZ(-0.61260149, 13))
p.inst(RZ(1.1049346, 14))
p.inst(CNOT(0, 1))
p.inst(CNOT(2, 3))
p.inst(CNOT(4, 5))
p.inst(CNOT(6, 7))
p.inst(CNOT(8, 9))
p.inst(CNOT(10, 11))
p.inst(CNOT(12, 13))
p.inst(RZ(-1.5002017, 1))
p.inst(RZ(0.38294136, 3))
p.inst(RZ(-0.34345858, 5))
p.inst(RZ(-0.70756849, 7))
p.inst(RZ(0.53735569, 9))
p.inst(RZ(0.758994, 11))
p.inst(RZ(0.61260149, 13))
p.inst(CNOT(0, 1))
p.inst(CNOT(2, 3))
p.inst(CNOT(4, 5))
p.inst(CNOT(6, 7))
p.inst(CNOT(8, 9))
p.inst(CNOT(10, 11))
p.inst(CNOT(12, 13))
p.inst(H(0))
p.inst(RZ(-0.69551246, 1))
p.inst(RZ(0.69551246, 2))
p.inst(RZ(1.4543177, 3))
p.inst(RZ(-1.4543177, 4))
p.inst(RZ(-0.97094792, 5))
p.inst(RZ(0.97094792, 6))
p.inst(RZ(1.2189608, 7))
p.inst(RZ(-1.2189608, 8))
p.inst(RZ(1.0237262, 9))
p.inst(RZ(-1.0237262, 10))
p.inst(RZ(-1.7521421, 11))
p.inst(RZ(1.7521421, 12))
p.inst(RZ(-1.1049346, 13))
p.inst(RZ(0, 0))
p.inst(RZ(0.69551246, 2))
p.inst(RZ(-1.4543177, 4))
p.inst(RZ(0.97094792, 6))
p.inst(RZ(-1.2189608, 8))
p.inst(RZ(-1.0237262, 10))
p.inst(RZ(1.7521421, 12))
p.inst(CNOT(13, 14))
p.inst(H(0))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(CNOT(5, 6))
p.inst(CNOT(7, 8))
p.inst(CNOT(9, 10))
p.inst(CNOT(11, 12))
p.inst(RZ(-1.1049346, 14))
p.inst(RZ(0, 0))
p.inst(RZ(-0.69551246, 2))
p.inst(RZ(1.4543177, 4))
p.inst(RZ(-0.97094792, 6))
p.inst(RZ(1.2189608, 8))
p.inst(RZ(1.0237262, 10))
p.inst(RZ(-1.7521421, 12))
p.inst(CNOT(13, 14))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(CNOT(5, 6))
p.inst(CNOT(7, 8))
p.inst(CNOT(9, 10))
p.inst(CNOT(11, 12))
p.inst(H(13))
p.inst(H(14))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(H(5))
p.inst(H(6))
p.inst(H(7))
p.inst(H(8))
p.inst(H(9))
p.inst(H(10))
p.inst(H(11))
p.inst(H(12))
p.inst(RZ(0, 13))
p.inst(RZ(0, 14))
p.inst(RZ(0, 1))
p.inst(RZ(0, 2))
p.inst(RZ(0, 3))
p.inst(RZ(0, 4))
p.inst(RZ(0, 5))
p.inst(RZ(0, 6))
p.inst(RZ(0, 7))
p.inst(RZ(0, 8))
p.inst(RZ(0, 9))
p.inst(RZ(0, 10))
p.inst(RZ(0, 11))
p.inst(RZ(0, 12))
p.inst(H(13))
p.inst(H(14))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(H(5))
p.inst(H(6))
p.inst(H(7))
p.inst(H(8))
p.inst(H(9))
p.inst(H(10))
p.inst(H(11))
p.inst(H(12))
p.inst(RZ(0, 13))
p.inst(RZ(0, 14))
p.inst(RZ(0, 1))
p.inst(RZ(0, 2))
p.inst(RZ(0, 3))
p.inst(RZ(0, 4))
p.inst(RZ(0, 5))
p.inst(RZ(0, 6))
p.inst(RZ(0, 7))
p.inst(RZ(0, 8))
p.inst(RZ(0, 9))
p.inst(RZ(0, 10))
p.inst(RZ(0, 11))
p.inst(RZ(0, 12))
p.inst(MEASURE(0, ro[15]))
p.inst(MEASURE(1, ro[16]))
p.inst(MEASURE(2, ro[17]))
p.inst(MEASURE(3, ro[18]))
p.inst(MEASURE(4, ro[19]))
p.inst(MEASURE(5, ro[20]))
p.inst(MEASURE(6, ro[21]))
p.inst(MEASURE(7, ro[22]))
p.inst(MEASURE(8, ro[23]))
p.inst(MEASURE(9, ro[24]))
p.inst(MEASURE(10, ro[25]))
p.inst(MEASURE(11, ro[26]))
p.inst(MEASURE(12, ro[27]))
p.inst(MEASURE(13, ro[28]))
p.inst(MEASURE(14, ro[29]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('15q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)