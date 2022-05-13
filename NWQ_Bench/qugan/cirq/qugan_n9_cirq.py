import cirq
import numpy as np
from functools import reduce

def u2(p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[1/np.sqrt(2), -np.exp(1j*p_lambda)*1/np.sqrt(2)], [np.exp(1j*p_phi)*1/np.sqrt(2), np.exp(1j*p_lambda+1j*p_phi)*1/np.sqrt(2)]]))

def u3(p_theta, p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[np.cos(p_theta/2), -np.exp(1j*p_lambda)*np.sin(p_theta/2)], [np.exp(1j*p_phi)*np.sin(p_theta/2), np.exp(1j*p_lambda+1j*p_phi)*np.cos(p_theta/2)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

circuit = cirq.Circuit(
    u2(np.pi, np.pi)(q[0]),
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    cirq.rx(np.pi / 2)(q[1]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[4]),
    cirq.rx(np.pi / 2)(q[5]),
    cirq.rx(np.pi / 2)(q[6]),
    cirq.rx(np.pi / 2)(q[7]),
    cirq.rx(np.pi / 2)(q[8]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[5], q[6]),
    cirq.rz(1.724517)(q[2]),
    cirq.rz(0.91774004)(q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[5], q[6]),
    cirq.rx(-np.pi / 2)(q[1]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[5]),
    cirq.rx(-np.pi / 2)(q[6]),
    u3(0, 0, 0)(q[2]),
    u3(0, 0, 0)(q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[5], q[6]),
    u3(-1.4866231, 0, 0)(q[2]),
    u3(-1.0598507, 0, 0)(q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[5], q[6]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[6]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[6], q[7]),
    cirq.rz(3.0154695)(q[3]),
    cirq.rz(0.29075759)(q[7]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[6], q[7]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[6]),
    cirq.rx(-np.pi / 2)(q[7]),
    u3(0, 0, 0)(q[3]),
    u3(0, 0, 0)(q[7]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[6], q[7]),
    u3(-1.0993885, 0, 0)(q[3]),
    u3(-0.97412798, 0, 0)(q[7]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[6], q[7]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[7]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[7], q[8]),
    cirq.rz(2.8434888)(q[4]),
    cirq.rz(2.3712238)(q[8]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[7], q[8]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[4]),
    cirq.rx(-np.pi / 2)(q[7]),
    cirq.rx(-np.pi / 2)(q[8]),
    u3(0, 0, 0)(q[4]),
    u3(0, 0, 0)(q[8]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[7], q[8]),
    u3(-0.26495473, 0, 0)(q[4]),
    u3(-1.0987503, 0, 0)(q[8]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[5], q[1]),
    cirq.CCX(q[0], q[1], q[5]),
    cirq.CNOT(q[5], q[1]),
    cirq.CNOT(q[6], q[2]),
    cirq.CCX(q[0], q[2], q[6]),
    cirq.CNOT(q[6], q[2]),
    cirq.CNOT(q[7], q[3]),
    cirq.CCX(q[0], q[3], q[7]),
    cirq.CNOT(q[7], q[3]),
    cirq.CNOT(q[8], q[4]),
    cirq.CCX(q[0], q[4], q[8]),
    u2(np.pi, np.pi)(q[0]),
    cirq.CNOT(q[8], q[4]),
    cirq.measure(q[5], key='c00'),
    cirq.measure(q[6], key='c01'),
    cirq.measure(q[7], key='c02'),
    cirq.measure(q[8], key='c03')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)