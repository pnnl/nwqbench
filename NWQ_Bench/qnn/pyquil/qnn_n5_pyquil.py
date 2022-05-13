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

ro = p.declare('ro', memory_type='BIT', memory_size=10)

p.inst(yy_defgate)
p.inst(zz_defgate)
p.inst(cry_defgate)
p.inst(crz_defgate)

p.inst(H(0))
p.inst(RY(4.9053416, 1))
p.inst(RY(2.6219432, 2))
p.inst(RY(2.1643378, 3))
p.inst(RY(2.035242, 4))
p.inst(RZ(5.321323, 1))
p.inst(RZ(2.8180595, 2))
p.inst(RZ(2.5775709, 3))
p.inst(RZ(0.54460083, 4))
p.inst(yy(3.8044817)(1, 2))
p.inst(zz(2.9653883)(1, 2))
p.inst(cry(3.8801311)(1, 2))
p.inst(crz(3.4880895)(1, 2))
p.inst(CSWAP(0, 1, 3))
p.inst(CSWAP(0, 2, 4))
p.inst(H(0))
p.inst(MEASURE(0, ro[5]))
p.inst(MEASURE(1, ro[6]))
p.inst(MEASURE(2, ro[7]))
p.inst(MEASURE(3, ro[8]))
p.inst(MEASURE(4, ro[9]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
