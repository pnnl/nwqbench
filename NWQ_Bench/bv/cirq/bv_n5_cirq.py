import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.X(q[4]),
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[4]),
    cirq.CNOT(q[2], q[4]),
    cirq.H(q[2]),
    cirq.CNOT(q[3], q[4]),
    cirq.H(q[3]),
    cirq.measure(q[0], key='c00'),
    cirq.measure(q[1], key='c01'),
    cirq.measure(q[2], key='c02'),
    cirq.measure(q[3], key='c03')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)