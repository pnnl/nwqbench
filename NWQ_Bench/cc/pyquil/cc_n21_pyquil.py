from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE, X, MOVE, NOT, IOR, AND
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=22)

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
p.inst(H(15))
p.inst(H(16))
p.inst(H(17))
p.inst(H(18))
p.inst(H(19))
p.inst(CNOT(0, 20))
p.inst(CNOT(1, 20))
p.inst(CNOT(2, 20))
p.inst(CNOT(3, 20))
p.inst(CNOT(4, 20))
p.inst(CNOT(5, 20))
p.inst(CNOT(6, 20))
p.inst(CNOT(7, 20))
p.inst(CNOT(8, 20))
p.inst(CNOT(9, 20))
p.inst(CNOT(10, 20))
p.inst(CNOT(11, 20))
p.inst(CNOT(12, 20))
p.inst(CNOT(13, 20))
p.inst(CNOT(14, 20))
p.inst(CNOT(15, 20))
p.inst(CNOT(16, 20))
p.inst(CNOT(17, 20))
p.inst(CNOT(18, 20))
p.inst(CNOT(19, 20))
p.inst(MEASURE(20, ro[20]))

p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(X(20)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(20)))


p.if_then(ro[20], Program(H(0)))


p.if_then(ro[20], Program(H(1)))


p.if_then(ro[20], Program(H(2)))


p.if_then(ro[20], Program(H(3)))


p.if_then(ro[20], Program(H(4)))


p.if_then(ro[20], Program(H(5)))


p.if_then(ro[20], Program(H(6)))


p.if_then(ro[20], Program(H(7)))


p.if_then(ro[20], Program(H(8)))


p.if_then(ro[20], Program(H(9)))


p.if_then(ro[20], Program(H(10)))


p.if_then(ro[20], Program(H(11)))


p.if_then(ro[20], Program(H(12)))


p.if_then(ro[20], Program(H(13)))


p.if_then(ro[20], Program(H(14)))


p.if_then(ro[20], Program(H(15)))


p.if_then(ro[20], Program(H(16)))


p.if_then(ro[20], Program(H(17)))


p.if_then(ro[20], Program(H(18)))


p.if_then(ro[20], Program(H(19)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(CNOT(6, 20)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(0)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(1)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(2)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(3)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(4)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(5)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(6)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(7)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(8)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(9)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(10)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(11)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(12)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(13)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(14)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(15)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(16)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(17)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(18)))


p.inst(MOVE(ro[21], 0))
p.inst(IOR(ro[21], ro[0]))
p.inst(IOR(ro[21], ro[1]))
p.inst(IOR(ro[21], ro[2]))
p.inst(IOR(ro[21], ro[3]))
p.inst(IOR(ro[21], ro[4]))
p.inst(IOR(ro[21], ro[5]))
p.inst(IOR(ro[21], ro[6]))
p.inst(IOR(ro[21], ro[7]))
p.inst(IOR(ro[21], ro[8]))
p.inst(IOR(ro[21], ro[9]))
p.inst(IOR(ro[21], ro[10]))
p.inst(IOR(ro[21], ro[11]))
p.inst(IOR(ro[21], ro[12]))
p.inst(IOR(ro[21], ro[13]))
p.inst(IOR(ro[21], ro[14]))
p.inst(IOR(ro[21], ro[15]))
p.inst(IOR(ro[21], ro[16]))
p.inst(IOR(ro[21], ro[17]))
p.inst(IOR(ro[21], ro[18]))
p.inst(IOR(ro[21], ro[19]))
p.inst(IOR(ro[21], ro[20]))
p.inst(NOT(ro[21]))
p.if_then(ro[21], Program(H(19)))

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
p.inst(MEASURE(15, ro[15]))
p.inst(MEASURE(16, ro[16]))
p.inst(MEASURE(17, ro[17]))
p.inst(MEASURE(18, ro[18]))
p.inst(MEASURE(19, ro[19]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('21q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
