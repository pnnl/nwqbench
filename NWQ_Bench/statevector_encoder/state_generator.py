# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 04/19/2021.
# ----------------------------------------------------------------------

import qiskit
import numpy as np
import sys
import os


rng = np.random.default_rng(seed=42)
k = 10
#k = int(sys.argv[1])
data = rng.random((1,2**k))
print(data)
def toQuantumData(data):
    input_vec = data.copy().ravel()
    vec_len = input_vec.shape[0]
    input_matrix = np.zeros((vec_len, vec_len),dtype='complex128')
    input_matrix[0] = input_vec
    input_matrix = np.complex128(input_matrix.transpose(0, 1))
    u, s, v = np.linalg.svd(input_matrix)
    output_matrix = np.dot(u, v)
    output_matrix = output_matrix
    output_data = output_matrix[0, :].reshape(1,data.shape[0],data.shape[1] )
    return output_data


def toQuantumMatrix(data):
    input_vec = data.copy().ravel()
    vec_len = input_vec.shape[0]
    input_matrix = np.zeros((vec_len, vec_len),dtype='complex128')
    input_matrix[0] = input_vec
    input_matrix = np.complex128(input_matrix.transpose(0, 1))
    u, s, v = np.linalg.svd(input_matrix)
    output_matrix = np.dot(u, v)
    #output_matrix = output_matrix[:,0]
    #output_matrix = output_matrix.reshape((self.filter_shape[0],self.filter_shape[1]))
    return output_matrix.T

state = toQuantumMatrix(data)
dat = toQuantumData(data)
register = qiskit.QuantumRegister(k)
circuit = qiskit.QuantumCircuit(register)
print(dat)
circuit.append(qiskit.extensions.UnitaryGate(state),register)
circuit.measure_all()

new_circuit = circuit
while True:
    old_circuit = new_circuit
    new_circuit = new_circuit.decompose()
    if old_circuit == new_circuit:
        break

svsim = qiskit.Aer.get_backend('statevector_simulator')
qobj= qiskit.assemble(circuit)
result = svsim.run(qobj).result()
out_state = result.get_statevector()

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/statevector_n{k}.qasm","w")
qasm_file.write(new_circuit.qasm())
qasm_file.close()
