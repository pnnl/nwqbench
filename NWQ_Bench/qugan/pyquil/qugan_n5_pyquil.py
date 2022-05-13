from pyquil import Program, get_qc
from pyquil.gates import CCNOT, RX, CNOT, RZ, MEASURE
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_sqrt, quil_exp, quil_cis
from pyquil.quilbase import DefGate
from functools import reduce
import numpy as np

shots = 1024

p_phi = Parameter('phi')
p_lambda = Parameter('lambda')
p_theta = Parameter('theta')

u2_array = np.array([[1/quil_sqrt(2),-quil_exp(1j*p_lambda)*1/quil_sqrt(2)],[quil_exp(1j*p_phi)*1/quil_sqrt(2),quil_exp(1j*p_lambda+1j*p_phi)*1/quil_sqrt(2)]])
u3_array = np.array([[quil_cos(p_theta/2),-quil_exp(1j*p_lambda)*quil_sin(p_theta/2)],[quil_exp(1j*p_phi)*quil_sin(p_theta/2),quil_exp(1j*p_lambda+1j*p_phi)*quil_cos(p_theta/2)]])


u2_defgate = DefGate('u2', u2_array, [p_phi, p_lambda])
u2 = u2_defgate.get_constructor()
u3_defgate = DefGate('u3', u3_array, [p_theta, p_phi, p_lambda])
u3 = u3_defgate.get_constructor()


p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=2)

p.inst(u2_defgate)
p.inst(u3_defgate)

p.inst(u2(0, np.pi)(0))
# Export to pyquil WARNING: unknown gate "r".# Export to pyquil WARNING: unknown gate "r".# Export to pyquil WARNING: unknown gate "r".# Export to pyquil WARNING: unknown gate "r".p.inst(RX(np.pi / 2, 1))
p.inst(RX(np.pi / 2, 2))
p.inst(RX(np.pi / 2, 3))
p.inst(RX(np.pi / 2, 4))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(RZ(0.16702648, 2))
p.inst(RZ(2.8732151, 4))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(RX(-np.pi / 2, 1))
p.inst(RX(-np.pi / 2, 2))
p.inst(RX(-np.pi / 2, 3))
p.inst(RX(-np.pi / 2, 4))
p.inst(u3(1.0109876, 0, 0)(2))
p.inst(u3(0.33986129, 0, 0)(4))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(u3(-1.0109876, 0, 0)(2))
p.inst(u3(-0.33986129, 0, 0)(4))
p.inst(CNOT(1, 2))
p.inst(CNOT(3, 4))
p.inst(CNOT(3, 1))
p.inst(CCNOT(0, 1, 3))
p.inst(CNOT(3, 1))
p.inst(CNOT(4, 2))
p.inst(CCNOT(0, 2, 4))
p.inst(u2(0, np.pi)(0))
p.inst(CNOT(4, 2))
p.inst(MEASURE(3, ro[0]))
p.inst(MEASURE(4, ro[1]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
