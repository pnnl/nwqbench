# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite 
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 04/19/2021.
# ----------------------------------------------------------------------

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import sys
import os
import random
import math

def swapTest(qc, qr):
    qc.h(qr[0])
    n_swap = len(qr)//2
    for i in range(n_swap):
        qc.cswap(qr[0],qr[i+1],qr[i+n_swap+1])
    qc.h(qr[0])

def init(qc, qr):
    for i in range(1,len(qr)//2+1):
        ro = random.uniform(-2.0,2.0)*math.pi
        qc.rx(ro+random.random(), qr[i])
        qc.rx(ro+random.random(), qr[i+len(qr)//2])

n = int(sys.argv[1])
n_qubits = 2*n+1
random.seed(555)


qr = QuantumRegister(n_qubits)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr,cr)

init(qc,qr)
swapTest(qc,qr)

qc.measure(0,cr)
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/swap_test_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=1000)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)
 

