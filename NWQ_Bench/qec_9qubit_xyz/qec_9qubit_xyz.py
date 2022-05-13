import qiskit
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
# https://arxiv.org/pdf/0905.2794.pdf?source=post_page---------------------------
k = int(sys.argv[1])
#k=2


def state_preparation(circuit: qiskit.QuantumCircuit, qubits: qiskit.QuantumRegister,cbits):
    # Prepare 3-bit code accross 3 quits ( I.e |111> + |000> )
    assert len(qubits)==9
    circuit.h(qubits[0])
    circuit.cnot(qubits[0],qubits[3])
    circuit.cnot(qubits[0],qubits[6])
    circuit.h(qubits[0])
    circuit.h(qubits[3])
    circuit.h(qubits[6])
    # Now we do the error test
    circuit.cnot(qubits[0],qubits[1])
    circuit.cnot(qubits[0],qubits[2])
    circuit.cnot(qubits[3],qubits[4])
    circuit.cnot(qubits[3],qubits[5])
    circuit.cnot(qubits[6],qubits[7])
    circuit.cnot(qubits[6],qubits[8])


def z_error_detection(circuit: qiskit.QuantumCircuit, qubits: qiskit.QuantumRegister,
                      ancilla_qubits: qiskit.QuantumRegister,cbits: qiskit.ClassicalRegister):
    for anc_state,state_l in zip(range(0,8,2),range(0,9,3)):
        circuit.cnot(qubits[state_l], ancilla_qubits[anc_state])
        circuit.cnot(qubits[state_l+1], ancilla_qubits[anc_state])
        circuit.cnot(qubits[state_l+1], ancilla_qubits[anc_state+1])
        circuit.cnot(qubits[state_l+2], ancilla_qubits[anc_state+1])
    for indx in range(6):
        circuit.measure(ancilla_qubits[indx], cbits[indx])


def x_error_detection(circuit: qiskit.QuantumCircuit, qbts: qiskit.QuantumRegister,
                      ancilla_qubits: qiskit.QuantumRegister, cbts: qiskit.ClassicalRegister):
    for qb in qbts:
        circuit.h(qb)
    for i in range(6):
        circuit.cnot(qbts[i],ancilla_qubits[6])
        circuit.cnot(qbts[i+3],ancilla_qubits[7])
    circuit.measure(ancilla_qubits[6],cbts[6])
    circuit.measure(ancilla_qubits[7],cbts[7])
    for i in range(8):
        circuit.h(qbts[i])


if __name__ == "__main__":
    print("Generating Circuit...")
    qubits = qiskit.QuantumRegister(9*k)
    ancilla_qubits = qiskit.QuantumRegister(8*k)
    cbits = qiskit.ClassicalRegister(8*k)
    circuit = qiskit.QuantumCircuit(qubits,cbits)
    circuit.add_register(ancilla_qubits)
    for i,j,k in zip(range(0,len(qubits),9),range(0,len(ancilla_qubits),8),range(0,len(cbits),8)):
        state_preparation(circuit,qubits[i:i+9],cbits[k:k+8])
        z_error_detection(circuit,qubits[i:i+9], ancilla_qubits[j:j+8],cbits[k:k+8])
        x_error_detection(circuit,qubits[i:i+9], ancilla_qubits[j:j+8],cbits[k:k+8])
    #simulator = qiskit.Aer.get_backend('aer_simulator')
    #circuit.draw(output='mpl')
    #plt.show()
    #circ = qiskit.compiler.transpile(circuit, simulator)
    #result = simulator.run(circ).result()
    #counts = result.get_counts(circ)



if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/qec_9qubit_x_" + str(len(qubits)+len(ancilla_qubits)) + ".qasm","w")
qasm_file.write(circuit.qasm())
qasm_file.close()