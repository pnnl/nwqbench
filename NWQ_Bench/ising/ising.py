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
import os
import random

N = int(sys.argv[1])
Bx = 2.0
total_T = 15.0
M = 1
random.seed(555)

Bz = [random.uniform(-2.0,2.0) for i in range(0,N)]
J = [random.uniform(-2.0,2.0) for i in range(0,N)]

def CZ(qc,q1,q2,phi):
   qc.rz(0.5*phi,q2)
   qc.cx(q1,q2)
   qc.rz(-0.5*phi,q2)
   qc.cx(q1,q2)

def ZcrossZ(qc,q1,q2,phi):
    qc.rz(phi,q1)
    qc.rz(-phi,q2)
    CZ(qc,q1,q2,-2.0*phi)

def initialize(qc):
    for i in range(0,N):
        qc.h(i)

def red_hamiltonian(qc,m):
    for i in range(0,N-1,2):
        phi = J[i]*(2.0*m-1)/M
        ZcrossZ(qc,i,i+1,phi)

def black_hamiltonian(qc,m):
    for i in range(1,N-1,2):
        phi = J[i]*(2.0*m-1)/M
        ZcrossZ(qc,i,i+1,phi)

def Bz_hamiltonian(qc,m):
    for i in range(0,N):
        theta1 = (1.0 - (2.0*m-1.0)/M) * -2.0 * Bx * total_T / M
        theta2 = (1.0 - (2.0*m-1.0)/M) * -2.0 * Bz[i] * total_T / M
        qc.h(i)
        qc.rz(theta1,i)
        qc.h(i)
        qc.rz(theta2,i)

qc = QuantumCircuit(N, N)
initialize(qc)
for i in range (1,M+1):
    red_hamiltonian(qc,i)
    black_hamiltonian(qc,i)
    Bz_hamiltonian(qc,i)

qc.measure_all()
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/ising_n" + str(N) + ".qasm","w")

qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)  


