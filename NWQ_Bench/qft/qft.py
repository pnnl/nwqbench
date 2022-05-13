# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite 
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 05/21/2021.
# ----------------------------------------------------------------------


import numpy as np
from qiskit import QuantumCircuit
#from qiskit import execute, Aer
import sys
import math
import os

n_qubits = int(sys.argv[1])

def cu1(qc, l, a, b):
    qc.u1(l/2, a)
    qc.cx(a, b)
    qc.u1(-l/2, b)
    qc.cx(a, b)
    qc.u1(l/2, b)

def qft(qc, n):
    for j in range(n):
        for k in range(j):
            cu1(qc, math.pi/float(2**(j-k)), j, k)
        qc.h(j)

qc = QuantumCircuit(n_qubits, n_qubits)
qft(qc,n_qubits)

qc.measure_all()

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/qft_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)
