from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE, X, MOVE, NOT, IOR, AND
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=7)

p.inst(H(0))
p.inst(H(1))
p.inst(H(2))
p.inst(H(3))
p.inst(H(4))
p.inst(CNOT(0, 5))
p.inst(CNOT(1, 5))
p.inst(CNOT(2, 5))
p.inst(CNOT(3, 5))
p.inst(CNOT(4, 5))
p.inst(MEASURE(5, ro[5]))

p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(X(5)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(5)))


p.if_then(ro[5], Program(H(0)))


p.if_then(ro[5], Program(H(1)))


p.if_then(ro[5], Program(H(2)))


p.if_then(ro[5], Program(H(3)))


p.if_then(ro[5], Program(H(4)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(CNOT(1, 5)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(0)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(1)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(2)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(3)))


p.inst(MOVE(ro[6], 0))
p.inst(IOR(ro[6], ro[0]))
p.inst(IOR(ro[6], ro[1]))
p.inst(IOR(ro[6], ro[2]))
p.inst(IOR(ro[6], ro[3]))
p.inst(IOR(ro[6], ro[4]))
p.inst(IOR(ro[6], ro[5]))
p.inst(NOT(ro[6]))
p.if_then(ro[6], Program(H(4)))

p.inst(MEASURE(0, ro[0]))
p.inst(MEASURE(1, ro[1]))
p.inst(MEASURE(2, ro[2]))
p.inst(MEASURE(3, ro[3]))
p.inst(MEASURE(4, ro[4]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('6q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
