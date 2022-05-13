import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[3]),
    cirq.CNOT(q[1], q[3]),
    cirq.CNOT(q[1], q[4]),
    cirq.CNOT(q[1], q[4]),
    cirq.measure(q[3], key='c00'),
    cirq.measure(q[4], key='c01'),
    cirq.H(q[5]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[5], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CNOT(q[6], q[9]),
    cirq.CNOT(q[6], q[9]),
    cirq.measure(q[8], key='c02'),
    cirq.measure(q[9], key='c03'),
    cirq.H(q[10]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[10], q[13]),
    cirq.CNOT(q[11], q[13]),
    cirq.CNOT(q[11], q[14]),
    cirq.CNOT(q[11], q[14]),
    cirq.measure(q[13], key='c04'),
    cirq.measure(q[14], key='c05')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)