import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[3], q[4]),
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