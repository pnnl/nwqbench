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

n = int(sys.argv[1])
pi = math.pi

def diffuse(qc):
    for j in range(0,n):
        qc.h(j)
    for j in range(0,n):
        qc.x(j)
    for j in range(0,n-1):
        qc.reset(2*n+1+j)
    qc.ccx(1,0,2*n+1)
    for j in range(1,n-1):
        qc.ccx(2*n+1+j-1,j+1,2*n+1+j)
    qc.z(2*n+1+n-2)
    for j in range(n-2,0,-1):
        qc.ccx(2*n+1+j-1,j+1,2*n+1+j)
    qc.ccx(1,0,2*n+1)
    for j in range(0,n):
        qc.x(j)
    for j in range(0,n):
        qc.h(j)

def EQxMark(qc,tF):
    for j in range(0,n):
        if j!=1:
            qc.x(n+j)
    for j in range(0,n-1):
        qc.reset(2*n+1+j)
    qc.ccx(n+1,n, 2*n+1)
    for j in range(1,n-1):
        qc.ccx(2*n+1+j-1,n+j+1,2*n+1+j)
    if tF != 0:
        qc.cx(2*n+1+n-2, 2*n)
    else:
        qc.z(2*n+1+n-2)
    for j in range(n-2,0,-1):
        qc.ccx(2*n+1+j-1, n+j+1, 2*n+1+j)
    qc.ccx(n+1, n, 2*n+1)
    for j in range(0,n):
        if j !=1 :
            qc.x(n+j)

def Sqr(qc):
    for i in range(0,((n-1)//2)+1):
        k = i*2
        qc.cx(i,n+k)
    for i in range(((n+1)//2),n):
        k = 2*i-n;
        qc.cx(i,n+k)
        qc.cx(i,n+k+1)

n_qubits = 2*n+1+n-1

qc = QuantumCircuit(n_qubits,2*n+1)
N = 2**n
nstep = math.floor((pi/4)*math.sqrt(N))

for i in range(0,n):
    qc.h(i)
for istep in range(1,nstep+1):
    Sqr(qc)
    EQxMark(qc,0)
    Sqr(qc)
    diffuse(qc)
  
Sqr(qc)
EQxMark(qc,1);

#qc.measure_all()

qc.measure([2*n],[n*2])
qc.measure([i for i in range(2*n)],[i for i in range(2*n)])

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/square_root_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

# simulator = Aer.get_backend('qasm_simulator')
# job = execute(qc,simulator,shots=1000)
# result = job.result()
# counts = result.get_counts(qc)
# print (counts)


