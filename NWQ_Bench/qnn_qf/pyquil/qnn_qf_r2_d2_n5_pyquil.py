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

p.inst(RY(0.74112722, 0))
p.inst(RY(1.1897021, 1))
p.inst(RY(1.6820708, 2))
p.inst(cry(0.95224137)(0, 1))
p.inst(cry(0.68008628)(1, 2))
p.inst(cry(1.9511137)(2, 0))
p.inst(RY(0.75913465, 0))
p.inst(RY(2.0517674, 1))
p.inst(RY(2.3983248, 2))
p.inst(cry(1.3839028)(0, 1))
p.inst(cry(2.7005981)(1, 2))
p.inst(cry(1.1385292)(2, 0))
p.inst(RY(2.3976709, 0))
p.inst(RY(1.7424099, 1))
p.inst(RY(2.352948, 2))
p.inst(cry(3.0359317)(0, 3))
p.inst(cry(2.5548187)(1, 3))
p.inst(cry(0.52892069)(2, 3))
p.inst(cry(2.9779363)(0, 4))
p.inst(cry(0.52004459)(1, 4))
p.inst(cry(0.22143418)(2, 4))
p.inst(MEASURE(3, ro[0]))
p.inst(MEASURE(4, ro[1]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('5q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
