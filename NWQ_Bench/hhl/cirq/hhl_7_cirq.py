import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

circuit = cirq.Circuit(
    cirq.rz(-np.pi / 4)(q[0]),
    cirq.rx(3.8098602)(q[1]),
    cirq.rx(3.8098602)(q[2]),
    cirq.rx(3.8098602)(q[3]),
    cirq.rx(3.8098602)(q[4]),
    cirq.rx(3.8098602)(q[5]),
    cirq.ry(0.28967817)(q[6]),
    cirq.ry(np.pi)(q[0]),
    cirq.ry(-np.pi / 2)(q[1]),
    cirq.ry(-np.pi / 2)(q[2]),
    cirq.ry(-np.pi / 2)(q[3]),
    cirq.ry(-np.pi / 2)(q[4]),
    cirq.ry(-np.pi / 2)(q[5]),
    cirq.rz(np.pi / 4)(q[0]),
    cirq.CNOT(q[1], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[1], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-1.7108829)(q[1]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[2]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-3.4217658)(q[2]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[3]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[3]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[3]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.56034639)(q[3]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-1.1206928)(q[4]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(0.6682675)(q[5]),
    cirq.rz(0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(2.4710034)(q[5]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(np.pi / 2)(q[5]),
    cirq.CNOT(q[4], q[5]),
    cirq.rz(np.pi / 4)(q[5]),
    cirq.CNOT(q[4], q[5]),
    cirq.H(q[4]),
    cirq.rz(-np.pi / 4)(q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.rz(np.pi / 8)(q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.rz(-np.pi / 4)(q[3]),
    cirq.rz(-np.pi / 8)(q[5]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(np.pi / 4)(q[4]),
    cirq.CNOT(q[3], q[4]),
    cirq.H(q[3]),
    cirq.rz(-np.pi / 4)(q[4]),
    cirq.CNOT(q[2], q[5]),
    cirq.rz(np.pi / 16)(q[5]),
    cirq.CNOT(q[2], q[5]),
    cirq.rz(-np.pi / 8)(q[2]),
    cirq.rz(-np.pi / 16)(q[5]),
    cirq.CNOT(q[2], q[4]),
    cirq.rz(np.pi / 8)(q[4]),
    cirq.CNOT(q[2], q[4]),
    cirq.rz(-np.pi / 4)(q[2]),
    cirq.rz(-np.pi / 8)(q[4]),
    cirq.CNOT(q[2], q[3]),
    cirq.rz(np.pi / 4)(q[3]),
    cirq.CNOT(q[2], q[3]),
    cirq.H(q[2]),
    cirq.rz(-np.pi / 4)(q[3]),
    cirq.CNOT(q[1], q[5]),
    cirq.rz(np.pi / 32)(q[5]),
    cirq.CNOT(q[1], q[5]),
    cirq.rz(-np.pi / 16)(q[1]),
    cirq.rz(-np.pi / 32)(q[5]),
    cirq.CNOT(q[1], q[4]),
    cirq.CNOT(q[5], q[6]),
    cirq.rz(np.pi / 16)(q[4]),
    cirq.ry(-0.07880704)(q[6]),
    cirq.CNOT(q[1], q[4]),
    cirq.rz(-np.pi / 8)(q[1]),
    cirq.rz(-np.pi / 16)(q[4]),
    cirq.CNOT(q[1], q[3]),
    cirq.CNOT(q[4], q[6]),
    cirq.rz(np.pi / 8)(q[3]),
    cirq.ry(-0.10745406)(q[6]),
    cirq.CNOT(q[1], q[3]),
    cirq.CNOT(q[5], q[6]),
    cirq.rz(-np.pi / 4)(q[1]),
    cirq.rz(-np.pi / 8)(q[3]),
    cirq.ry(0.059433034)(q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[3], q[6]),
    cirq.rz(np.pi / 4)(q[2]),
    cirq.ry(0.037086759)(q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[5], q[6]),
    cirq.H(q[1]),
    cirq.rz(-np.pi / 4)(q[2]),
    cirq.ry(-0.11113425)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.090469198)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.11644025)(q[6]),
    cirq.CNOT(q[2], q[6]),
    cirq.ry(0.097611808)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.09205678)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.11154458)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.033985812)(q[6]),
    cirq.CNOT(q[3], q[6]),
    cirq.ry(0.049624102)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.10831791)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.083772717)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.16223736)(q[6]),
    cirq.CNOT(q[1], q[6]),
    cirq.ry(0.14683263)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.084469198)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.10841311)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.048240009)(q[6]),
    cirq.CNOT(q[3], q[6]),
    cirq.ry(0.033623576)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.11157749)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.092239785)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.094908439)(q[6]),
    cirq.CNOT(q[2], q[6]),
    cirq.ry(0.10838905)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.090848564)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.11118869)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.036333382)(q[6]),
    cirq.CNOT(q[3], q[6]),
    cirq.ry(0.055353647)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(-0.107649)(q[6]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(-0.080853948)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.ry(0.20101829)(q[6]),
    cirq.CNOT(q[1], q[6]),
    cirq.rx(-3 * np.pi / 4)(q[1]),
    cirq.ry(-np.pi / 2)(q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(-np.pi / 4)(q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(np.pi / 8)(q[1]),
    cirq.CNOT(q[1], q[3]),
    cirq.rz(5 * np.pi / 4)(q[2]),
    cirq.rz(-np.pi / 8)(q[3]),
    cirq.ry(np.pi / 2)(q[2]),
    cirq.rz(np.pi / 4)(q[2]),
    cirq.CNOT(q[1], q[3]),
    cirq.rz(np.pi / 16)(q[1]),
    cirq.CNOT(q[1], q[4]),
    cirq.rz(np.pi / 8)(q[3]),
    cirq.rz(-np.pi / 16)(q[4]),
    cirq.CNOT(q[2], q[3]),
    cirq.rz(-np.pi / 4)(q[3]),
    cirq.CNOT(q[2], q[3]),
    cirq.rz(np.pi / 8)(q[2]),
    cirq.rz(5 * np.pi / 4)(q[3]),
    cirq.ry(np.pi / 2)(q[3]),
    cirq.rz(np.pi / 4)(q[3]),
    cirq.CNOT(q[1], q[4]),
    cirq.rz(np.pi / 32)(q[1]),
    cirq.CNOT(q[1], q[5]),
    cirq.rz(np.pi / 16)(q[4]),
    cirq.rz(-np.pi / 32)(q[5]),
    cirq.CNOT(q[2], q[4]),
    cirq.rz(-np.pi / 8)(q[4]),
    cirq.CNOT(q[2], q[4]),
    cirq.rz(np.pi / 16)(q[2]),
    cirq.rz(np.pi / 8)(q[4]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(-np.pi / 4)(q[4]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(np.pi / 8)(q[3]),
    cirq.rz(5 * np.pi / 4)(q[4]),
    cirq.ry(np.pi / 2)(q[4]),
    cirq.rz(np.pi / 4)(q[4]),
    cirq.CNOT(q[1], q[5]),
    cirq.rz(-0.6682675)(q[1]),
    cirq.rz(np.pi / 32)(q[5]),
    cirq.CNOT(q[2], q[5]),
    cirq.rz(-np.pi / 16)(q[5]),
    cirq.CNOT(q[2], q[5]),
    cirq.rz(-0.6682675)(q[2]),
    cirq.rz(np.pi / 16)(q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.rz(-np.pi / 8)(q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.rz(-0.6682675)(q[3]),
    cirq.rz(np.pi / 8)(q[5]),
    cirq.CNOT(q[4], q[5]),
    cirq.rz(-np.pi / 4)(q[5]),
    cirq.CNOT(q[4], q[5]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-3 * np.pi / 4)(q[5]),
    cirq.ry(np.pi / 2)(q[5]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[5], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(3.8121819)(q[5]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.ry(np.pi / 2)(q[5]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[4], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(3.4768873)(q[4]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.ry(np.pi / 2)(q[4]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[3]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[3]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[3]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[3], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(3.30924)(q[3]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.ry(np.pi / 2)(q[3]),
    cirq.CNOT(q[2], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-0.6682675)(q[2]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[2], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-6.1993617)(q[2]),
    cirq.rz(-0.6682675)(q[0]),
    cirq.ry(np.pi / 2)(q[2]),
    cirq.CNOT(q[1], q[0]),
    cirq.rz(-2.4733252)(q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(np.pi)(q[0]),
    cirq.CNOT(q[1], q[0]),
    cirq.ry(1.0108711)(q[0]),
    cirq.rz(-1.5288845)(q[1]),
    cirq.rz(0.90252883)(q[0]),
    cirq.ry(np.pi / 2)(q[1]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2'),
    cirq.measure(q[3], key='meas3'),
    cirq.measure(q[4], key='meas4'),
    cirq.measure(q[5], key='meas5'),
    cirq.measure(q[6], key='meas6')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)