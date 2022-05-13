import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(0.27466857)(q[1]),
    cirq.ry(0.9919349)(q[2]),
    cirq.ry(0.1085488)(q[3]),
    cirq.ry(2.6658346)(q[4]),
    cirq.ry(2.6766281)(q[5]),
    cirq.ry(0.24565172)(q[6]),
    cirq.ry(2.9270122)(q[7]),
    cirq.ry(0.16299404)(q[8]),
    cirq.ry(2.3066568)(q[9]),
    cirq.ry(1.5632304)(q[10]),
    cirq.ry(0.523205)(q[11]),
    cirq.ry(0.80548265)(q[12]),
    cirq.ry(1.994984)(q[13]),
    cirq.ry(2.6026488)(q[14]),
    cirq.CSWAP(q[0], q[1], q[8]),
    cirq.CSWAP(q[0], q[2], q[9]),
    cirq.CSWAP(q[0], q[3], q[10]),
    cirq.CSWAP(q[0], q[4], q[11]),
    cirq.CSWAP(q[0], q[5], q[12]),
    cirq.CSWAP(q[0], q[6], q[13]),
    cirq.CSWAP(q[0], q[7], q[14]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)