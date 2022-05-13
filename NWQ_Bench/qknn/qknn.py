# Paper: https://arxiv.org/pdf/2003.09187.pdf
import qiskit
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from itertools import permutations
import os

if len(sys.argv) < 2:
    print("Use from CLI with python filename n_qubits")
    exit()

k = int(sys.argv[1])

if k%2 == 0 or k<3:
    print("System requires an odd number of qubits greater than 3")
    exit()

class QKNN():
    def __init__(self,qubit_count):
        self.qubit_count = qubit_count
        self.quantum_register = qiskit.circuit.QuantumRegister(self.qubit_count)
        self.classical_register = qiskit.circuit.ClassicalRegister(1)
        self.circuit = qiskit.circuit.QuantumCircuit(self.quantum_register,self.classical_register)
        self.data_load()
        self.swap_test()
        self.circuit.measure(self.quantum_register[0],self.classical_register[0])
        self.circuit.draw(output='mpl')
        if not os.path.isdir("circuit_svg"):
            os.mkdir("circuit_svg")
        plt.tight_layout()
        plt.savefig(f"circuit_svg/qknn_n{k}.svg")



    def data_load(self):
        for qubit in list(self.quantum_register)[1:]:
            self.circuit.ry(np.random.rand()*np.pi,qubit)

    def swap_test(self):
        self.circuit.h(0)
        qubit_list = list(self.quantum_register)[1:]
        q1 = qubit_list[:len(qubit_list)//2]
        q2 = qubit_list[len(qubit_list)//2:]
        for q_1,q_2 in zip(q1,q2):
            self.circuit.cswap(self.quantum_register[0],q_1,q_2)
        self.circuit.h(0)


circuit = QKNN(k)
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/qknn_n{k}.qasm","w")
qasm_file.write(circuit.circuit.qasm())
qasm_file.close()
