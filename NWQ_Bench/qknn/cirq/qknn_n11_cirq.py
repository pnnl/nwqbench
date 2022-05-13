import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(2.8008902)(q[1]),
    cirq.ry(0.69545835)(q[2]),
    cirq.ry(0.099936864)(q[3]),
    cirq.ry(3.078129)(q[4]),
    cirq.ry(0.68494174)(q[5]),
    cirq.ry(0.53728786)(q[6]),
    cirq.ry(3.0576215)(q[7]),
    cirq.ry(0.26289246)(q[8]),
    cirq.ry(1.1357725)(q[9]),
    cirq.ry(0.98289791)(q[10]),
    cirq.CSWAP(q[0], q[1], q[6]),
    cirq.CSWAP(q[0], q[2], q[7]),
    cirq.CSWAP(q[0], q[3], q[8]),
    cirq.CSWAP(q[0], q[4], q[9]),
    cirq.CSWAP(q[0], q[5], q[10]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)