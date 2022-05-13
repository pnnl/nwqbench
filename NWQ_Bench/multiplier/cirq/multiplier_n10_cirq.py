import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

circuit = cirq.Circuit(
    cirq.X(q[6]),
    cirq.X(q[9]),
    cirq.CCX(q[8], q[6], q[1]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[8], q[7], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[8], q[6], q[1]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[8], q[7], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[9], q[6], q[4]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[9], q[6], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.measure(q[2], key='c00'),
    cirq.measure(q[5], key='c01')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)