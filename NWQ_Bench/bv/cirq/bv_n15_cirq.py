import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.H(q[5]),
    cirq.H(q[6]),
    cirq.H(q[7]),
    cirq.H(q[8]),
    cirq.H(q[9]),
    cirq.H(q[10]),
    cirq.H(q[11]),
    cirq.H(q[12]),
    cirq.H(q[13]),
    cirq.X(q[14]),
    cirq.H(q[14]),
    cirq.CNOT(q[0], q[14]),
    cirq.H(q[0]),
    cirq.CNOT(q[1], q[14]),
    cirq.H(q[1]),
    cirq.CNOT(q[2], q[14]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.CNOT(q[4], q[14]),
    cirq.H(q[4]),
    cirq.H(q[5]),
    cirq.CNOT(q[6], q[14]),
    cirq.H(q[6]),
    cirq.H(q[7]),
    cirq.H(q[8]),
    cirq.CNOT(q[9], q[14]),
    cirq.H(q[9]),
    cirq.CNOT(q[10], q[14]),
    cirq.H(q[10]),
    cirq.H(q[11]),
    cirq.H(q[12]),
    cirq.CNOT(q[13], q[14]),
    cirq.H(q[13]),
    cirq.measure(q[0], key='c00'),
    cirq.measure(q[1], key='c01'),
    cirq.measure(q[2], key='c02'),
    cirq.measure(q[3], key='c03'),
    cirq.measure(q[4], key='c04'),
    cirq.measure(q[5], key='c05'),
    cirq.measure(q[6], key='c06'),
    cirq.measure(q[7], key='c07'),
    cirq.measure(q[8], key='c08'),
    cirq.measure(q[9], key='c09'),
    cirq.measure(q[10], key='c010'),
    cirq.measure(q[11], key='c011'),
    cirq.measure(q[12], key='c012'),
    cirq.measure(q[13], key='c013')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c010', 'c011', 'c012', 'c013', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)