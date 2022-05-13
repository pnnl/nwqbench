# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite 
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 05/21/2021.
# ----------------------------------------------------------------------

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
#from qiskit import execute, Aer
import sys
import math
import random
import os

def generate_astring(nqubits, prob=1.0):
    answer = []
    for i in range(nqubits):
        if random.random() <= prob:
            answer.append("1")
        else:
            answer.append("0")
    return "".join(answer)


def gen_bv(qc, qr, cr, n_qubits):
    hiddenString = generate_astring(n_qubits-1, 0.5)
    for i in range(n_qubits-1):
        qc.h(qr[i])
    qc.x(qr[n_qubits-1])
    qc.h(qr[n_qubits-1])
    qc.barrier()
    hiddenString = hiddenString[::-1]
    for i in range(len(hiddenString)):
        if hiddenString[i] == "1":
            qc.cx(qr[i], qr[n_qubits-1])
    hiddenString = hiddenString[::-1]
    qc.barrier()
    for i in range(n_qubits-1):
        qc.h(qr[i])
    for i in range(n_qubits-1):
        qc.measure(qr[i], cr[i])

n_qubits = int(sys.argv[1])

qr = QuantumRegister(n_qubits)
cr = ClassicalRegister(n_qubits)
qc = QuantumCircuit(qr,cr)

gen_bv(qc, qr, cr, n_qubits)

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/bv_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)

