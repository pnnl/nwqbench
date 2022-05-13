import cirq
import numpy as np
from functools import reduce

def u2(p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[1/np.sqrt(2), -np.exp(1j*p_lambda)*1/np.sqrt(2)], [np.exp(1j*p_phi)*1/np.sqrt(2), np.exp(1j*p_lambda+1j*p_phi)*1/np.sqrt(2)]]))

def u3(p_theta, p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[np.cos(p_theta/2), -np.exp(1j*p_lambda)*np.sin(p_theta/2)], [np.exp(1j*p_phi)*np.sin(p_theta/2), np.exp(1j*p_lambda+1j*p_phi)*np.cos(p_theta/2)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    u2(np.pi, np.pi)(q[0]),
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    cirq.rx(np.pi / 2)(q[1]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(0.16702648)(q[2]),
    cirq.rz(2.8732151)(q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[3], q[4]),
    cirq.rx(-np.pi / 2)(q[1]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[4]),
    u3(0, 0, 0)(q[2]),
    u3(0, 0, 0)(q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[3], q[4]),
    u3(-1.0109876, 0, 0)(q[2]),
    u3(-0.33986129, 0, 0)(q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[3], q[1]),
    cirq.CCX(q[0], q[1], q[3]),
    cirq.CNOT(q[3], q[1]),
    cirq.CNOT(q[4], q[2]),
    cirq.CCX(q[0], q[2], q[4]),
    u2(np.pi, np.pi)(q[0]),
    cirq.CNOT(q[4], q[2]),
    cirq.measure(q[3], key='c00'),
    cirq.measure(q[4], key='c01')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)