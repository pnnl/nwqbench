from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY, RZ
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_sqrt, quil_exp, quil_cis
from pyquil.quilbase import DefGate
from functools import reduce
import numpy as np

shots = 1024

p_theta = Parameter('theta')
p_phi = Parameter('phi')

yy_array = np.array([ [quil_cos(p_theta), 0, 0, 1j*quil_sin(p_theta)], [0, quil_cos(p_theta), -1j*quil_sin(p_theta), 0], [0, -1j*quil_sin(p_theta), quil_cos(p_theta), 0], [1j*quil_sin(p_theta), 0, 0, quil_cos(p_theta)] ])
zz_array = np.array([ [ quil_exp(-1j * p_theta / 2), 0, 0, 0 ], [ 0, quil_exp(1j * p_theta / 2), 0, 0], [ 0, 0, quil_exp(1j * p_theta / 2), 0 ], [ 0, 0, 0, quil_exp(-1j * p_theta / 2) ] ])
cry_array = np.array([[ 1, 0, 0, 0 ],[ 0, 1, 0, 0 ],[ 0, 0, quil_cos(p_theta / 2), -1*quil_sin(p_theta / 2) ],[ 0, 0, quil_sin(p_theta / 2), quil_cos(p_theta / 2) ]])
crz_array = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, quil_cos(p_phi / 2) - 1j * quil_sin(p_phi / 2), 0], [0, 0, 0, quil_cos(p_phi / 2) + 1j * quil_sin(p_phi / 2)]])


yy_defgate = DefGate('yy', yy_array, [p_theta])
yy = yy_defgate.get_constructor()
zz_defgate = DefGate('zz', zz_array, [p_theta])
zz = zz_defgate.get_constructor()
cry_defgate = DefGate('cry', cry_array, [p_theta])
cry = cry_defgate.get_constructor()
crz_defgate = DefGate('crz', crz_array, [p_phi])
crz = crz_defgate.get_constructor()


p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=18)

p.inst(yy_defgate)
p.inst(zz_defgate)
p.inst(cry_defgate)
p.inst(crz_defgate)

p.inst(H(0))
p.inst(RY(3.7977104, 1))
p.inst(RY(2.1872989, 2))
p.inst(RY(1.8219176, 3))
p.inst(RY(3.8088077, 4))
p.inst(RY(-0.83617905, 5))
p.inst(RY(-0.84824244, 6))
p.inst(RY(-2.3567766, 7))
p.inst(RY(1.9180287, 8))
p.inst(RZ(5.465414, 1))
p.inst(RZ(4.0266574, 2))
p.inst(RZ(4.2161812, 3))
p.inst(RZ(5.6376766, 4))
p.inst(RZ(1.7639482, 5))
p.inst(RZ(3.0085304, 6))
p.inst(RZ(-1.9598407, 7))
p.inst(RZ(-0.015369036, 8))
p.inst(yy(2.5820511)(1, 2))
p.inst(zz(0.77865462)(1, 2))
p.inst(yy(3.4375327)(2, 3))
p.inst(zz(3.1808425)(2, 3))
p.inst(cry(1.2040922)(1, 2))
p.inst(yy(3.9571394)(3, 4))
p.inst(crz(2.7980963)(1, 2))
p.inst(zz(4.9835202)(3, 4))
p.inst(cry(0.35436225)(2, 3))
p.inst(crz(1.063099)(2, 3))
p.inst(cry(0.24436762)(3, 4))
p.inst(crz(3.2324448)(3, 4))
p.inst(CSWAP(0, 1, 5))
p.inst(CSWAP(0, 2, 6))
p.inst(CSWAP(0, 3, 7))
p.inst(CSWAP(0, 4, 8))
p.inst(H(0))
p.inst(MEASURE(0, ro[9]))
p.inst(MEASURE(1, ro[10]))
p.inst(MEASURE(2, ro[11]))
p.inst(MEASURE(3, ro[12]))
p.inst(MEASURE(4, ro[13]))
p.inst(MEASURE(5, ro[14]))
p.inst(MEASURE(6, ro[15]))
p.inst(MEASURE(7, ro[16]))
p.inst(MEASURE(8, ro[17]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('9q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
