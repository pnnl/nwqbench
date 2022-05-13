from pyquil import Program, get_qc
from pyquil.gates import RY, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=15)

p.inst(RY(2.1506626, 0))
p.inst(RY(1.4482467, 1))
p.inst(RY(2.3705663, 2))
p.inst(RY(1.9765769, 3))
p.inst(RY(0.62383312, 4))
p.inst(RY(2.8280429, 5))
p.inst(RY(2.120318, 6))
p.inst(RY(2.1798952, 7))
p.inst(RY(0.7320994, 8))
p.inst(RY(1.4714046, 9))
p.inst(RY(1.3094267, 10))
p.inst(RY(2.5935193, 11))
p.inst(RY(1.8626523, 12))
p.inst(RY(2.2725045, 13))
p.inst(RY(1.4573817, 14))
p.inst(MEASURE(0, ro[0]))
p.inst(MEASURE(1, ro[1]))
p.inst(MEASURE(2, ro[2]))
p.inst(MEASURE(3, ro[3]))
p.inst(MEASURE(4, ro[4]))
p.inst(MEASURE(5, ro[5]))
p.inst(MEASURE(6, ro[6]))
p.inst(MEASURE(7, ro[7]))
p.inst(MEASURE(8, ro[8]))
p.inst(MEASURE(9, ro[9]))
p.inst(MEASURE(10, ro[10]))
p.inst(MEASURE(11, ro[11]))
p.inst(MEASURE(12, ro[12]))
p.inst(MEASURE(13, ro[13]))
p.inst(MEASURE(14, ro[14]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('15q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
