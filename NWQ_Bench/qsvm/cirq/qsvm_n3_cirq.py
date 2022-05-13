import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    cirq.CNOT(q[0], q[1]),
    cirq.rz(0.42211821)(q[1]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(1.9338127)(q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(1.3191528)(q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[1]),
    cirq.rz(0.045029159)(q[2]),
    cirq.rz(1.4449089)(q[1]),
    cirq.H(q[2]),
    cirq.CNOT(q[0], q[1]),
    cirq.rz(2.8656361)(q[0]),
    cirq.rz(1.8271938)(q[1]),
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)