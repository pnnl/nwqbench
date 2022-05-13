import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

circuit = cirq.Circuit(
    cirq.ry(2.1506626)(q[0]),
    cirq.ry(1.4482467)(q[1]),
    cirq.ry(2.3705663)(q[2]),
    cirq.ry(1.9765769)(q[3]),
    cirq.ry(0.62383312)(q[4]),
    cirq.ry(2.8280429)(q[5]),
    cirq.ry(2.120318)(q[6]),
    cirq.ry(2.1798952)(q[7]),
    cirq.ry(0.7320994)(q[8]),
    cirq.ry(1.4714046)(q[9]),
    cirq.ry(1.3094267)(q[10]),
    cirq.ry(2.5935193)(q[11]),
    cirq.ry(1.8626523)(q[12]),
    cirq.ry(2.2725045)(q[13]),
    cirq.ry(1.4573817)(q[14]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2'),
    cirq.measure(q[3], key='meas3'),
    cirq.measure(q[4], key='meas4'),
    cirq.measure(q[5], key='meas5'),
    cirq.measure(q[6], key='meas6'),
    cirq.measure(q[7], key='meas7'),
    cirq.measure(q[8], key='meas8'),
    cirq.measure(q[9], key='meas9'),
    cirq.measure(q[10], key='meas10'),
    cirq.measure(q[11], key='meas11'),
    cirq.measure(q[12], key='meas12'),
    cirq.measure(q[13], key='meas13'),
    cirq.measure(q[14], key='meas14')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)