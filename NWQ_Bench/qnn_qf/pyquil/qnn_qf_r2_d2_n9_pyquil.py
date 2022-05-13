from pyquil import Program, get_qc
from pyquil.gates import RY, MEASURE
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_sqrt, quil_exp, quil_cis
from pyquil.quilbase import DefGate
from functools import reduce
import numpy as np

shots = 1024

p_theta = Parameter('theta')

cry_array = np.array([[ 1, 0, 0, 0 ],[ 0, 1, 0, 0 ],[ 0, 0, quil_cos(p_theta / 2), -1*quil_sin(p_theta / 2) ],[ 0, 0, quil_sin(p_theta / 2), quil_cos(p_theta / 2) ]])


cry_defgate = DefGate('cry', cry_array, [p_theta])
cry = cry_defgate.get_constructor()


p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=2)

p.inst(cry_defgate)

p.inst(RY(3.0199575, 0))
p.inst(RY(0.6849634, 1))
p.inst(RY(0.19966078, 2))
p.inst(RY(2.4255556, 3))
p.inst(RY(0.17965019, 4))
p.inst(RY(0.21137635, 5))
p.inst(RY(2.1169674, 6))
p.inst(cry(0.81479306)(0, 1))
p.inst(cry(1.0362017)(1, 2))
p.inst(cry(0.95144891)(2, 3))
p.inst(cry(0.37686864)(3, 4))
p.inst(cry(0.59838775)(4, 5))
p.inst(cry(1.8460888)(5, 6))
p.inst(cry(0.10341369)(6, 0))
p.inst(RY(1.0081277, 0))
p.inst(RY(1.8153793, 1))
p.inst(RY(0.60519057, 2))
p.inst(RY(2.9301845, 3))
p.inst(RY(2.2280573, 4))
p.inst(RY(2.5004374, 5))
p.inst(RY(1.5186301, 6))
p.inst(cry(2.516851)(0, 1))
p.inst(cry(2.9520785)(1, 2))
p.inst(cry(1.8930492)(2, 3))
p.inst(cry(2.7177606)(3, 4))
p.inst(cry(2.4212721)(4, 5))
p.inst(cry(0.45559183)(5, 6))
p.inst(cry(0.25042298)(6, 0))
p.inst(RY(2.9043619, 0))
p.inst(RY(0.66974428, 1))
p.inst(RY(2.753528, 2))
p.inst(RY(0.23933046, 3))
p.inst(RY(0.46614657, 4))
p.inst(RY(0.0071772368, 5))
p.inst(RY(3.0222646, 6))
p.inst(cry(2.933675)(0, 7))
p.inst(cry(0.29781348)(1, 7))
p.inst(cry(1.0732682)(2, 7))
p.inst(cry(0.99333707)(3, 7))
p.inst(cry(2.2163495)(4, 7))
p.inst(cry(0.041894959)(5, 7))
p.inst(cry(0.20076766)(6, 7))
p.inst(cry(0.92724922)(0, 8))
p.inst(cry(0.69812999)(1, 8))
p.inst(cry(0.12907076)(2, 8))
p.inst(cry(0.079440692)(3, 8))
p.inst(cry(0.42589212)(4, 8))
p.inst(cry(0.65326438)(5, 8))
p.inst(cry(1.726853)(6, 8))
p.inst(MEASURE(7, ro[0]))
p.inst(MEASURE(8, ro[1]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('9q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
