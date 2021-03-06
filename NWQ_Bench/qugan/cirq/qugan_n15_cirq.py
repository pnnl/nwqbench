import cirq
import numpy as np
from functools import reduce

def u2(p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[1/np.sqrt(2), -np.exp(1j*p_lambda)*1/np.sqrt(2)], [np.exp(1j*p_phi)*1/np.sqrt(2), np.exp(1j*p_lambda+1j*p_phi)*1/np.sqrt(2)]]))

def u3(p_theta, p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[np.cos(p_theta/2), -np.exp(1j*p_lambda)*np.sin(p_theta/2)], [np.exp(1j*p_phi)*np.sin(p_theta/2), np.exp(1j*p_lambda+1j*p_phi)*np.cos(p_theta/2)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

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
    cirq.rx(np.pi / 2)(q[9]),
    cirq.rx(np.pi / 2)(q[10]),
    cirq.rx(np.pi / 2)(q[11]),
    cirq.rx(np.pi / 2)(q[12]),
    cirq.rx(np.pi / 2)(q[13]),
    cirq.rx(np.pi / 2)(q[14]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[8], q[9]),
    cirq.rz(1.2664125)(q[2]),
    cirq.rz(2.5810673)(q[9]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[8], q[9]),
    cirq.rx(-np.pi / 2)(q[1]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[8]),
    cirq.rx(-np.pi / 2)(q[9]),
    u3(0, 0, 0)(q[2]),
    u3(0, 0, 0)(q[9]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[8], q[9]),
    u3(-1.4487767, 0, 0)(q[2]),
    u3(-1.4950504, 0, 0)(q[9]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[8], q[9]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[9]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[9], q[10]),
    cirq.rz(0.74055553)(q[3]),
    cirq.rz(3.1218766)(q[10]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[9], q[10]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[9]),
    cirq.rx(-np.pi / 2)(q[10]),
    u3(0, 0, 0)(q[3]),
    u3(0, 0, 0)(q[10]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[9], q[10]),
    u3(-1.1646899, 0, 0)(q[3]),
    u3(-0.50052913, 0, 0)(q[10]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[9], q[10]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[10]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[10], q[11]),
    cirq.rz(2.3559741)(q[4]),
    cirq.rz(2.1470863)(q[11]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[10], q[11]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[4]),
    cirq.rx(-np.pi / 2)(q[10]),
    cirq.rx(-np.pi / 2)(q[11]),
    u3(0, 0, 0)(q[4]),
    u3(0, 0, 0)(q[11]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[10], q[11]),
    u3(-1.4174572, 0, 0)(q[4]),
    u3(-1.4210772, 0, 0)(q[11]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[10], q[11]),
    cirq.rx(np.pi / 2)(q[4]),
    cirq.rx(np.pi / 2)(q[11]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[11], q[12]),
    cirq.rz(1.5874395)(q[5]),
    cirq.rz(1.0572746)(q[12]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[11], q[12]),
    cirq.rx(-np.pi / 2)(q[4]),
    cirq.rx(-np.pi / 2)(q[5]),
    cirq.rx(-np.pi / 2)(q[11]),
    cirq.rx(-np.pi / 2)(q[12]),
    u3(0, 0, 0)(q[5]),
    u3(0, 0, 0)(q[12]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[11], q[12]),
    u3(-1.0930352, 0, 0)(q[5]),
    u3(-0.84439209, 0, 0)(q[12]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[11], q[12]),
    cirq.rx(np.pi / 2)(q[5]),
    cirq.rx(np.pi / 2)(q[12]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[12], q[13]),
    cirq.rz(3.1129243)(q[6]),
    cirq.rz(2.7825006)(q[13]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[12], q[13]),
    cirq.rx(-np.pi / 2)(q[5]),
    cirq.rx(-np.pi / 2)(q[6]),
    cirq.rx(-np.pi / 2)(q[12]),
    cirq.rx(-np.pi / 2)(q[13]),
    u3(0, 0, 0)(q[6]),
    u3(0, 0, 0)(q[13]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[12], q[13]),
    u3(-1.2005866, 0, 0)(q[6]),
    u3(-0.23144456, 0, 0)(q[13]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[12], q[13]),
    cirq.rx(np.pi / 2)(q[6]),
    cirq.rx(np.pi / 2)(q[13]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[13], q[14]),
    cirq.rz(1.1256105)(q[7]),
    cirq.rz(2.7848897)(q[14]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[13], q[14]),
    cirq.rx(-np.pi / 2)(q[6]),
    cirq.rx(-np.pi / 2)(q[7]),
    cirq.rx(-np.pi / 2)(q[13]),
    cirq.rx(-np.pi / 2)(q[14]),
    u3(0, 0, 0)(q[7]),
    u3(0, 0, 0)(q[14]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[13], q[14]),
    u3(-1.4893347, 0, 0)(q[7]),
    u3(-0.58159699, 0, 0)(q[14]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[8], q[1]),
    cirq.CCX(q[0], q[1], q[8]),
    cirq.CNOT(q[8], q[1]),
    cirq.CNOT(q[9], q[2]),
    cirq.CCX(q[0], q[2], q[9]),
    cirq.CNOT(q[9], q[2]),
    cirq.CNOT(q[10], q[3]),
    cirq.CCX(q[0], q[3], q[10]),
    cirq.CNOT(q[10], q[3]),
    cirq.CNOT(q[11], q[4]),
    cirq.CCX(q[0], q[4], q[11]),
    cirq.CNOT(q[11], q[4]),
    cirq.CNOT(q[12], q[5]),
    cirq.CCX(q[0], q[5], q[12]),
    cirq.CNOT(q[12], q[5]),
    cirq.CNOT(q[13], q[6]),
    cirq.CCX(q[0], q[6], q[13]),
    cirq.CNOT(q[13], q[6]),
    cirq.CNOT(q[14], q[7]),
    cirq.CCX(q[0], q[7], q[14]),
    u2(np.pi, np.pi)(q[0]),
    cirq.CNOT(q[14], q[7]),
    cirq.measure(q[8], key='c00'),
    cirq.measure(q[9], key='c01'),
    cirq.measure(q[10], key='c02'),
    cirq.measure(q[11], key='c03'),
    cirq.measure(q[12], key='c04'),
    cirq.measure(q[13], key='c05'),
    cirq.measure(q[14], key='c06')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)