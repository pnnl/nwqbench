import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.rx(-3.8535372)(q[1]),
    cirq.rx(-4.2592974)(q[2]),
    cirq.rx(0.76934517)(q[3]),
    cirq.rx(5.2757681)(q[4]),
    cirq.rx(-4.3555394)(q[5]),
    cirq.rx(-1.1088457)(q[6]),
    cirq.rx(0.60673656)(q[7]),
    cirq.rx(3.1760628)(q[8]),
    cirq.CSWAP(q[0], q[1], q[5]),
    cirq.CSWAP(q[0], q[2], q[6]),
    cirq.CSWAP(q[0], q[3], q[7]),
    cirq.CSWAP(q[0], q[4], q[8]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)