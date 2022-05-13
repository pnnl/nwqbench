import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

circuit = cirq.Circuit(
    cirq.ry(2.1506626)(q[0]),
    cirq.ry(1.4482467)(q[1]),
    cirq.ry(2.3705663)(q[2]),
    cirq.ry(1.9765769)(q[3]),
    cirq.ry(0.62383312)(q[4]),
    cirq.ry(2.8280429)(q[5]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2'),
    cirq.measure(q[3], key='meas3'),
    cirq.measure(q[4], key='meas4'),
    cirq.measure(q[5], key='meas5')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)