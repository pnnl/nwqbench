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
#from qiskit import execute, Aer
import sys
import os
import random
import math

if len(sys.argv) != 2:
    print ("python ghz_state.py n_qubits")
    exit(1)

n_qubits = int(sys.argv[1])

def cx_chain(qc,n):
    for i in range(0,n-1):
        qc.cx(i,i+1)


qc = QuantumCircuit(n_qubits,n_qubits)

qc.h(0)
cx_chain(qc,n_qubits)
qc.measure_all()

qiskit.

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/ghz_state_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)



