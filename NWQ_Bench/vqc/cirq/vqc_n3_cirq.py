import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.rz(0.84751467)(q[0]),
    cirq.rz(1.3067611)(q[1]),
    cirq.rz(2.5281551)(q[2]),
    cirq.CNOT(q[0], q[1]),
    cirq.rz(2.012692)(q[1]),
    cirq.CNOT(q[0], q[1]),
    cirq.ry(1.3211686)(q[0]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(1.0058728)(q[0]),
    cirq.rz(3.1257781)(q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.ry(2.2279618)(q[1]),
    cirq.ry(0.33699867)(q[2]),
    cirq.rz(1.2746996)(q[1]),
    cirq.rz(1.0712587)(q[2]),
    cirq.CZ(q[0], q[1]),
    cirq.CZ(q[0], q[2]),
    cirq.ry(2.2934377)(q[0]),
    cirq.CZ(q[1], q[2]),
    cirq.rz(1.4841367)(q[0]),
    cirq.ry(1.9225664)(q[1]),
    cirq.ry(1.7857658)(q[2]),
    cirq.rz(2.4225378)(q[1]),
    cirq.rz(1.3689008)(q[2]),
    cirq.CZ(q[0], q[1]),
    cirq.CZ(q[0], q[2]),
    cirq.ry(0.59639646)(q[0]),
    cirq.CZ(q[1], q[2]),
    cirq.rz(1.2541083)(q[0]),
    cirq.ry(2.2665371)(q[1]),
    cirq.ry(0.026092831)(q[2]),
    cirq.rz(2.4037987)(q[1]),
    cirq.rz(1.8096955)(q[2]),
    cirq.CZ(q[0], q[1]),
    cirq.CZ(q[0], q[2]),
    cirq.ry(0.24001234)(q[0]),
    cirq.CZ(q[1], q[2]),
    cirq.rz(2.484556)(q[0]),
    cirq.ry(2.4622526)(q[1]),
    cirq.ry(1.9069715)(q[2]),
    cirq.rz(0.444765)(q[1]),
    cirq.rz(1.099548)(q[2]),
    cirq.CZ(q[0], q[1]),
    cirq.CZ(q[0], q[2]),
    cirq.CZ(q[1], q[2]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)