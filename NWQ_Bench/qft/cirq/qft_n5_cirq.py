import cirq
import numpy as np
from functools import reduce

def u1(p_lambda):
    return cirq.MatrixGate(np.array([[1, 0], [0, np.exp(1j*p_lambda)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    u1(np.pi / 4)(q[1]),
    u1(np.pi / 8)(q[2]),
    u1(np.pi / 16)(q[3]),
    u1(np.pi / 32)(q[4]),
    cirq.CNOT(q[1], q[0]),
    u1(-np.pi / 4)(q[0]),
    cirq.CNOT(q[1], q[0]),
    u1(np.pi / 4)(q[0]),
    cirq.H(q[1]),
    cirq.CNOT(q[2], q[0]),
    u1(-np.pi / 8)(q[0]),
    cirq.CNOT(q[2], q[0]),
    u1(np.pi / 8)(q[0]),
    u1(np.pi / 4)(q[2]),
    cirq.CNOT(q[2], q[1]),
    u1(-np.pi / 4)(q[1]),
    cirq.CNOT(q[2], q[1]),
    u1(np.pi / 4)(q[1]),
    cirq.H(q[2]),
    cirq.CNOT(q[3], q[0]),
    u1(-np.pi / 16)(q[0]),
    cirq.CNOT(q[3], q[0]),
    u1(np.pi / 16)(q[0]),
    u1(np.pi / 8)(q[3]),
    cirq.CNOT(q[3], q[1]),
    u1(-np.pi / 8)(q[1]),
    cirq.CNOT(q[3], q[1]),
    u1(np.pi / 8)(q[1]),
    u1(np.pi / 4)(q[3]),
    cirq.CNOT(q[3], q[2]),
    u1(-np.pi / 4)(q[2]),
    cirq.CNOT(q[3], q[2]),
    u1(np.pi / 4)(q[2]),
    cirq.H(q[3]),
    cirq.CNOT(q[4], q[0]),
    u1(-np.pi / 32)(q[0]),
    cirq.CNOT(q[4], q[0]),
    u1(np.pi / 32)(q[0]),
    u1(np.pi / 16)(q[4]),
    cirq.CNOT(q[4], q[1]),
    u1(-np.pi / 16)(q[1]),
    cirq.CNOT(q[4], q[1]),
    u1(np.pi / 16)(q[1]),
    u1(np.pi / 8)(q[4]),
    cirq.CNOT(q[4], q[2]),
    u1(-np.pi / 8)(q[2]),
    cirq.CNOT(q[4], q[2]),
    u1(np.pi / 8)(q[2]),
    u1(np.pi / 4)(q[4]),
    cirq.CNOT(q[4], q[3]),
    u1(-np.pi / 4)(q[3]),
    cirq.CNOT(q[4], q[3]),
    u1(np.pi / 4)(q[3]),
    cirq.H(q[4]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2'),
    cirq.measure(q[3], key='meas3'),
    cirq.measure(q[4], key='meas4')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)