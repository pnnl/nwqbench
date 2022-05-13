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
import os
import random

nCoins = int(sys.argv[1])
n_qubits = nCoins + 1

random.seed(555)

def gen_cc(qc, qr, cr, nCoins):
    indexOfFalseCoin = random.randint(0,nCoins-1)

    for i in range(nCoins):
        qc.h(qr[i])
    for i in range(nCoins):
        qc.cx(qr[i],qr[nCoins])
    qc.measure(qr[nCoins],cr[nCoins])

    qc.x(qr[nCoins]).c_if(cr,0)
    qc.h(qr[nCoins]).c_if(cr,0)

    for i in range(nCoins):
        qc.h(qr[i]).c_if(cr, 2**nCoins)
    qc.barrier()

    qc.cx(qr[indexOfFalseCoin], qr[nCoins]).c_if(cr,0)
    qc.barrier()

    for i in range(nCoins):
        qc.h(qr[i]).c_if(cr,0)

    for i in range(nCoins):
        qc.measure(qr[i], cr[i])


qr = QuantumRegister(n_qubits)
cr = ClassicalRegister(n_qubits)
qc = QuantumCircuit(qr,cr)

gen_cc(qc, qr, cr, nCoins)


if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/cc_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)


