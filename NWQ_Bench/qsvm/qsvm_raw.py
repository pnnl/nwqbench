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
import matplotlib.pyplot as plt
import sys
import os

if len(sys.argv) < 2:
    print("Use from CLI with python filename n_qubits")
    exit()

k = int(sys.argv[1])

class QSVM():
    def __init__(self,qubit_count):
        self.qubit_count = qubit_count
        self.quantum_register = qiskit.circuit.QuantumRegister(self.qubit_count)
        self.classical_register = qiskit.circuit.ClassicalRegister(self.qubit_count)
        self.circuit = qiskit.circuit.QuantumCircuit(self.quantum_register,self.classical_register)
        self.hadamard_circuit()
        self.phase_addition()
        self.hadamard_circuit()
        self.circuit.measure_all()
        self.circuit.draw(output='mpl')
        try:
            plt.tight_layout()
            if not os.path.isdir("circuit_svg"):
                os.mkdir("circuit_svg")
            plt.tight_layout()
            plt.savefig(f"circuit_svg/qsvn_n{k}.svg")
        except:
            print("Figure too large - Can't save")


    def hadamard_circuit(self):
        for qubit in self.quantum_register:
            self.circuit.h(qubit)

    def phase_addition(self):
        for qubit in self.quantum_register:
            self.circuit.p(np.random.rand()*np.pi,qubit)
        for cqubit,aqubit in zip(self.quantum_register[:-1],self.quantum_register[1:]):
            self.circuit.cx(cqubit,aqubit)
            self.circuit.rz(np.random.rand()*np.pi,aqubit)
            self.circuit.cx(cqubit,aqubit)
        iterables =  list(self.quantum_register).copy()
        iterables.reverse()
        l1 = iterables[:-1]
        l2 = iterables[1:]
        for a1, a2 in zip(l1,l2):
            self.circuit.cx(a2,a1)
            self.circuit.rz(np.random.rand()*np.pi,a1)
            self.circuit.cx(a2,a1)
        for qubit in self.quantum_register:
            self.circuit.rz(np.random.rand()*np.pi,qubit)

circuit = QSVM(k)
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/qsvm_n{k}.qasm","w")
qasm_file.write(circuit.circuit.qasm())
qasm_file.close()
