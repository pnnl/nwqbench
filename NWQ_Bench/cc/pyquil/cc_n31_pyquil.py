from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE, X, MOVE, NOT, IOR, AND
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=32)

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
p.inst(H(20))
p.inst(H(21))
p.inst(H(22))
p.inst(H(23))
p.inst(H(24))
p.inst(H(25))
p.inst(H(26))
p.inst(H(27))
p.inst(H(28))
p.inst(H(29))
p.inst(CNOT(0, 30))
p.inst(CNOT(1, 30))
p.inst(CNOT(2, 30))
p.inst(CNOT(3, 30))
p.inst(CNOT(4, 30))
p.inst(CNOT(5, 30))
p.inst(CNOT(6, 30))
p.inst(CNOT(7, 30))
p.inst(CNOT(8, 30))
p.inst(CNOT(9, 30))
p.inst(CNOT(10, 30))
p.inst(CNOT(11, 30))
p.inst(CNOT(12, 30))
p.inst(CNOT(13, 30))
p.inst(CNOT(14, 30))
p.inst(CNOT(15, 30))
p.inst(CNOT(16, 30))
p.inst(CNOT(17, 30))
p.inst(CNOT(18, 30))
p.inst(CNOT(19, 30))
p.inst(CNOT(20, 30))
p.inst(CNOT(21, 30))
p.inst(CNOT(22, 30))
p.inst(CNOT(23, 30))
p.inst(CNOT(24, 30))
p.inst(CNOT(25, 30))
p.inst(CNOT(26, 30))
p.inst(CNOT(27, 30))
p.inst(CNOT(28, 30))
p.inst(CNOT(29, 30))
p.inst(MEASURE(30, ro[30]))

p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(X(30)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(30)))


p.if_then(ro[30], Program(H(0)))


p.if_then(ro[30], Program(H(1)))


p.if_then(ro[30], Program(H(2)))


p.if_then(ro[30], Program(H(3)))


p.if_then(ro[30], Program(H(4)))


p.if_then(ro[30], Program(H(5)))


p.if_then(ro[30], Program(H(6)))


p.if_then(ro[30], Program(H(7)))


p.if_then(ro[30], Program(H(8)))


p.if_then(ro[30], Program(H(9)))


p.if_then(ro[30], Program(H(10)))


p.if_then(ro[30], Program(H(11)))


p.if_then(ro[30], Program(H(12)))


p.if_then(ro[30], Program(H(13)))


p.if_then(ro[30], Program(H(14)))


p.if_then(ro[30], Program(H(15)))


p.if_then(ro[30], Program(H(16)))


p.if_then(ro[30], Program(H(17)))


p.if_then(ro[30], Program(H(18)))


p.if_then(ro[30], Program(H(19)))


p.if_then(ro[30], Program(H(20)))


p.if_then(ro[30], Program(H(21)))


p.if_then(ro[30], Program(H(22)))


p.if_then(ro[30], Program(H(23)))


p.if_then(ro[30], Program(H(24)))


p.if_then(ro[30], Program(H(25)))


p.if_then(ro[30], Program(H(26)))


p.if_then(ro[30], Program(H(27)))


p.if_then(ro[30], Program(H(28)))


p.if_then(ro[30], Program(H(29)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(CNOT(6, 30)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(0)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(1)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(2)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(3)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(4)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(5)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(6)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(7)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(8)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(9)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(10)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(11)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(12)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(13)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(14)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(15)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(16)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(17)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(18)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(19)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(20)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(21)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(22)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(23)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(24)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(25)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(26)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(27)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(28)))


p.inst(MOVE(ro[31], 0))
p.inst(IOR(ro[31], ro[0]))
p.inst(IOR(ro[31], ro[1]))
p.inst(IOR(ro[31], ro[2]))
p.inst(IOR(ro[31], ro[3]))
p.inst(IOR(ro[31], ro[4]))
p.inst(IOR(ro[31], ro[5]))
p.inst(IOR(ro[31], ro[6]))
p.inst(IOR(ro[31], ro[7]))
p.inst(IOR(ro[31], ro[8]))
p.inst(IOR(ro[31], ro[9]))
p.inst(IOR(ro[31], ro[10]))
p.inst(IOR(ro[31], ro[11]))
p.inst(IOR(ro[31], ro[12]))
p.inst(IOR(ro[31], ro[13]))
p.inst(IOR(ro[31], ro[14]))
p.inst(IOR(ro[31], ro[15]))
p.inst(IOR(ro[31], ro[16]))
p.inst(IOR(ro[31], ro[17]))
p.inst(IOR(ro[31], ro[18]))
p.inst(IOR(ro[31], ro[19]))
p.inst(IOR(ro[31], ro[20]))
p.inst(IOR(ro[31], ro[21]))
p.inst(IOR(ro[31], ro[22]))
p.inst(IOR(ro[31], ro[23]))
p.inst(IOR(ro[31], ro[24]))
p.inst(IOR(ro[31], ro[25]))
p.inst(IOR(ro[31], ro[26]))
p.inst(IOR(ro[31], ro[27]))
p.inst(IOR(ro[31], ro[28]))
p.inst(IOR(ro[31], ro[29]))
p.inst(IOR(ro[31], ro[30]))
p.inst(NOT(ro[31]))
p.if_then(ro[31], Program(H(29)))

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
p.inst(MEASURE(20, ro[20]))
p.inst(MEASURE(21, ro[21]))
p.inst(MEASURE(22, ro[22]))
p.inst(MEASURE(23, ro[23]))
p.inst(MEASURE(24, ro[24]))
p.inst(MEASURE(25, ro[25]))
p.inst(MEASURE(26, ro[26]))
p.inst(MEASURE(27, ro[27]))
p.inst(MEASURE(28, ro[28]))
p.inst(MEASURE(29, ro[29]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('31q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
