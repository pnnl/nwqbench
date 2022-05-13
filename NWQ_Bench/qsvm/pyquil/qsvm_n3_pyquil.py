from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, RZ, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=6)

p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
# Export to pyquil WARNING: unknown gate "p".# Export to pyquil WARNING: unknown gate "p".# Export to pyquil WARNING: unknown gate "p".p.inst(CNOT(0, 1))
p.inst(RZ(0.42211821, 1))
p.inst(CNOT(0, 1))
p.inst(CNOT(1, 2))
p.inst(RZ(1.9338127, 2))
p.inst(CNOT(1, 2))
p.inst(CNOT(1, 2))
p.inst(RZ(1.3191528, 2))
p.inst(CNOT(1, 2))
p.inst(CNOT(0, 1))
p.inst(RZ(0.045029159, 2))
p.inst(RZ(1.4449089, 1))
p.inst(H(2))
p.inst(CNOT(0, 1))
p.inst(RZ(2.8656361, 0))
p.inst(RZ(1.8271938, 1))
p.inst(H(0))
p.inst(H(1))
p.inst(MEASURE(0, ro[3]))
p.inst(MEASURE(1, ro[4]))
p.inst(MEASURE(2, ro[5]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('3q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
