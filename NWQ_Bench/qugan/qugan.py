# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 04/19/2021.
# ----------------------------------------------------------------------
# Paper: https://arxiv.org/pdf/2010.09036.pdf

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

if k%2 == 0 or k < 3:
    print("System requires an odd number of qubits greater than 3")
    exit()

class QuGAN():
    def __init__(self,qubit_count):
        self.qubit_count = qubit_count
        self.quantum_register = qiskit.circuit.QuantumRegister(self.qubit_count)
        self.classical_register = qiskit.circuit.ClassicalRegister((self.qubit_count-1)//2)
        self.circuit = qiskit.circuit.QuantumCircuit(self.quantum_register,self.classical_register)
        self.data_load()
        self.swap_test()
        self.generate_samples()
        try:
            self.circuit.draw(output='mpl')
            plt.tight_layout()
            if not os.path.isdir("circuit_svg"):
                os.mkdir("circuit_svg")
            try:
                plt.savefig(f"circuit_svg/qugan_n{k}.svg")
            except:
                pass
        except:
            pass

    def data_load(self):
        for qubit in list(self.quantum_register)[1:]:
            self.circuit.ry(np.random.rand()*np.pi,qubit)
        qubit_list = list(self.quantum_register)[1:]
        s1 = qubit_list[:len(qubit_list)//2]
        s1_a,s1_b= s1[:-1],s1[1:]
        s2 = qubit_list[len(qubit_list)//2:]
        s2_a,s2_b= s2[:-1],s2[1:]
        for qa,qb in zip(s1_a,s1_b):
            self.circuit.ryy(np.random.rand()*np.pi,qa,qb)
            self.circuit.cry(np.random.rand()*np.pi,qa,qb)
        for qa,qb in zip(s2_a,s2_b):
            self.circuit.ryy(np.random.rand()*np.pi,qa,qb)
            self.circuit.cry(np.random.rand()*np.pi,qa,qb)


    def swap_test(self):
        self.circuit.h(0)
        qubit_list = list(self.quantum_register)[1:]
        q1 = qubit_list[:len(qubit_list)//2]
        q2 = qubit_list[len(qubit_list)//2:]
        for q_1,q_2 in zip(q1,q2):
            self.circuit.cswap(self.quantum_register[0],q_1,q_2)
        self.circuit.h(0)

    def generate_samples(self):
        qubit_list = list(self.quantum_register)[1:]
        s2 = qubit_list[len(qubit_list)//2:]
        print(s2)
        print(list(self.classical_register))
        for q,c in zip(s2,list(self.classical_register)):
            self.circuit.measure(q,c)

circuit = QuGAN(k)

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/qugan_n{k}.qasm","w")
qasm_file.write(circuit.circuit.qasm())
qasm_file.close()
