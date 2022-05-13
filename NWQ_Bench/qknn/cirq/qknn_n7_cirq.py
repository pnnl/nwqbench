import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(0.21315685)(q[1]),
    cirq.ry(0.13443125)(q[2]),
    cirq.ry(2.5425711)(q[3]),
    cirq.ry(1.3995784)(q[4]),
    cirq.ry(1.8805686)(q[5]),
    cirq.ry(2.0339493)(q[6]),
    cirq.CSWAP(q[0], q[1], q[4]),
    cirq.CSWAP(q[0], q[2], q[5]),
    cirq.CSWAP(q[0], q[3], q[6]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)