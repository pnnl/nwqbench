# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite 
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 04/19/2021.
# ----------------------------------------------------------------------

import numpy as np
from qiskit import QuantumCircuit
from qiskit import execute, Aer
import os
import sys
import random
import math

if len(sys.argv) != 2:
    print ("python ghz_state.py n_qubits")
    exit(1)

n_qubits = int(sys.argv[1])

def F_gate(qc,i,j,n,k):
    theta = math.acos(math.sqrt(1./(n-k+1)))
    qc.ry(-theta,j)
    qc.cz(i,j)
    qc.ry(theta,j)

qc = QuantumCircuit(n_qubits,n_qubits)
n = n_qubits

qc.x(n-1)

for i in range(0,n-1):
    F_gate(qc,n-1-i,n-2-i,n,i+1)

for i in range(0,n-1):
    qc.cx(n-2-i,n-1-i)

qc.measure_all()
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/w_state_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc,simulator,shots=1000)
result = job.result()
counts = result.get_counts(qc)
print (counts)


