from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE, X, MOVE, NOT, IOR, AND
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=12)

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
p.inst(CNOT(0, 10))
p.inst(CNOT(1, 10))
p.inst(CNOT(2, 10))
p.inst(CNOT(3, 10))
p.inst(CNOT(4, 10))
p.inst(CNOT(5, 10))
p.inst(CNOT(6, 10))
p.inst(CNOT(7, 10))
p.inst(CNOT(8, 10))
p.inst(CNOT(9, 10))
p.inst(MEASURE(10, ro[10]))

p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(X(10)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(10)))


p.if_then(ro[10], Program(H(0)))


p.if_then(ro[10], Program(H(1)))


p.if_then(ro[10], Program(H(2)))


p.if_then(ro[10], Program(H(3)))


p.if_then(ro[10], Program(H(4)))


p.if_then(ro[10], Program(H(5)))


p.if_then(ro[10], Program(H(6)))


p.if_then(ro[10], Program(H(7)))


p.if_then(ro[10], Program(H(8)))


p.if_then(ro[10], Program(H(9)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(CNOT(3, 10)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(0)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(1)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(2)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(3)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(4)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(5)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(6)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(7)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(8)))


p.inst(MOVE(ro[11], 0))
p.inst(IOR(ro[11], ro[0]))
p.inst(IOR(ro[11], ro[1]))
p.inst(IOR(ro[11], ro[2]))
p.inst(IOR(ro[11], ro[3]))
p.inst(IOR(ro[11], ro[4]))
p.inst(IOR(ro[11], ro[5]))
p.inst(IOR(ro[11], ro[6]))
p.inst(IOR(ro[11], ro[7]))
p.inst(IOR(ro[11], ro[8]))
p.inst(IOR(ro[11], ro[9]))
p.inst(IOR(ro[11], ro[10]))
p.inst(NOT(ro[11]))
p.if_then(ro[11], Program(H(9)))

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

p.wrap_in_numshots_loop(shots)

qc = get_qc('11q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
