import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(17)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.CNOT(q[0], q[3]),
    cirq.CNOT(q[0], q[6]),
    cirq.H(q[0]),
    cirq.H(q[3]),
    cirq.H(q[6]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[0], q[2]),
    cirq.CNOT(q[3], q[5]),
    cirq.CNOT(q[6], q[8]),
    cirq.CNOT(q[0], q[9]),
    cirq.CNOT(q[1], q[9]),
    cirq.CNOT(q[1], q[10]),
    cirq.CNOT(q[2], q[10]),
    cirq.CNOT(q[3], q[11]),
    cirq.CNOT(q[4], q[11]),
    cirq.CNOT(q[4], q[12]),
    cirq.CNOT(q[5], q[12]),
    cirq.CNOT(q[6], q[13]),
    cirq.CNOT(q[7], q[13]),
    cirq.CNOT(q[7], q[14]),
    cirq.CNOT(q[8], q[14]),
    cirq.measure(q[9], key='c00'),
    cirq.measure(q[10], key='c01'),
    cirq.measure(q[11], key='c02'),
    cirq.measure(q[12], key='c03'),
    cirq.measure(q[13], key='c04'),
    cirq.measure(q[14], key='c05'),
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.H(q[5]),
    cirq.H(q[6]),
    cirq.H(q[7]),
    cirq.H(q[8]),
    cirq.CNOT(q[0], q[15]),
    cirq.CNOT(q[3], q[16]),
    cirq.CNOT(q[1], q[15]),
    cirq.CNOT(q[4], q[16]),
    cirq.CNOT(q[2], q[15]),
    cirq.CNOT(q[5], q[16]),
    cirq.CNOT(q[3], q[15]),
    cirq.CNOT(q[6], q[16]),
    cirq.CNOT(q[4], q[15]),
    cirq.CNOT(q[7], q[16]),
    cirq.CNOT(q[5], q[15]),
    cirq.CNOT(q[8], q[16]),
    cirq.measure(q[15], key='c06'),
    cirq.measure(q[16], key='c07'),
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.H(q[5]),
    cirq.H(q[6]),
    cirq.H(q[7])
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)