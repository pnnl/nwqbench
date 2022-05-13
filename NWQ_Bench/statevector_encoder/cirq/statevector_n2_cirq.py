import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

circuit = cirq.Circuit(
    # Export to cirq WARNING: unknown gate "u".    # Export to cirq WARNING: unknown gate "u".    cirq.CNOT(q[0], q[1]),
    # Export to cirq WARNING: unknown gate "u".,
    # Export to cirq WARNING: unknown gate "u".,
    cirq.CNOT(q[0], q[1]),
    # Export to cirq WARNING: unknown gate "u".,
    # Export to cirq WARNING: unknown gate "u".,
    cirq.CNOT(q[0], q[1]),
    # Export to cirq WARNING: unknown gate "u".,
    # Export to cirq WARNING: unknown gate "u".,
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)