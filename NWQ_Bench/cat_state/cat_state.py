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
import random
import os
import math

n = int(sys.argv[1])

def catN(qc):
    qc.h(0)
    for i in range(1,n):
        qc.cx(i-1,i)

def unCatN(qc):
    for i in range(n-1,0,-1):
        qc.cx(i-1,i)
    qc.h(0)


qc = QuantumCircuit(n,n)
catN(qc)

qc.measure_all()
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/cat_state_n" + str(n) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)





