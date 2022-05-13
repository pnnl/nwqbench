import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(2.2439274)(q[1]),
    cirq.ry(0.38780286)(q[2]),
    cirq.ry(2.8663306)(q[3]),
    cirq.ry(2.209665)(q[4]),
    cirq.CSWAP(q[0], q[1], q[3]),
    cirq.CSWAP(q[0], q[2], q[4]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)