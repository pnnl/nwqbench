import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(25)]

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
    cirq.measure(q[14], key='c05'),
    cirq.H(q[15]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[18]),
    cirq.CNOT(q[16], q[18]),
    cirq.CNOT(q[16], q[19]),
    cirq.CNOT(q[16], q[19]),
    cirq.measure(q[18], key='c06'),
    cirq.measure(q[19], key='c07'),
    cirq.H(q[20]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[20], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CNOT(q[21], q[24]),
    cirq.CNOT(q[21], q[24]),
    cirq.measure(q[23], key='c00'),
    cirq.measure(q[24], key='c01')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c00', 'c01']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)