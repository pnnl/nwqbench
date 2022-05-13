import qiskit
import numpy as np
import sys
import os

k = int(sys.argv[1])
rng = np.random.default_rng(seed=42)
data = rng.random((1,k))

def toQuantumData(data):
    t_data = data.ravel()
    rotations = np.zeros((1,len(t_data)))
    rotations = 2*np.arcsin(np.sqrt(t_data))
    return rotations

dat = toQuantumData(data)
register = qiskit.QuantumRegister(k)
circuit = qiskit.QuantumCircuit(register)

for i,rotation in enumerate(dat):
    circuit.ry(rotation,register[i])
circuit.measure_all()
print(circuit)

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/ry_statevector_n{k}.qasm","w")
qasm_file.write(circuit.qasm())
qasm_file.close()
