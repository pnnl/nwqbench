import qiskit
import sys
import os
import numpy as np

k = int(sys.argv[1])
#k=2


def state_preparation(circuit: qiskit.QuantumCircuit, qubits: qiskit.QuantumRegister,cbits):
    # Prepare 3-bit code accross 3 quits ( I.e |111> + |000> )
    assert len(qubits)==5
    circuit.h(qubits[0])
    circuit.cnot(qubits[0],qubits[1])
    circuit.cnot(qubits[1],qubits[2])
    # Now we do the error test
    circuit.cnot(qubits[0],qubits[3])
    circuit.cnot(qubits[1],qubits[3])
    circuit.cnot(qubits[1],qubits[4])
    circuit.cnot(qubits[1],qubits[4])
    circuit.measure(qubits[3],cbits[0])
    circuit.measure(qubits[4],cbits[1])

if __name__ == "__main__":
    print("Generating Circuit...")
    qubits = qiskit.QuantumRegister(5*k)
    cbits = qiskit.ClassicalRegister(2*k)
    circuit = qiskit.QuantumCircuit(qubits,cbits)
    for i in range(0,len(qubits),5):
        cbit_index = i%4
        state_preparation(circuit,qubits[i:i+5],cbits[cbit_index*2:(cbit_index*2)+2])


#simulator = qiskit.Aer.get_backend('aer_simulator')
#circ = qiskit.compiler.transpile(circuit, simulator)

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/qec_5qubit_x_" + str(k*5) + ".qasm","w")
qasm_file.write(circuit.qasm())
qasm_file.close()