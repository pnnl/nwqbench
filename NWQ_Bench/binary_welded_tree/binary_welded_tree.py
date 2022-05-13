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
import math
import os

n = int(sys.argv[1])
dt = 57.295
s_ = 100

def controlled_expZ(qc, a, b):
    qc.rz(-2*dt,a)
    qc.cx(b,a)
    qc.rz(2*dt,a)

def PARSENODEROOT(qc):
    for i in range(0,n+1):
        qc.reset(3*n+16+i)
    for index in range(n,0,-1):
        qc.x(3*n+16+index)
        qc.ccx(3*n+16+index-1,3*n+16+index,index)
        qc.x(3*n+16+index)
        qc.cx(3*n+16+index,3*n+16+index-1)

    qc.x(3*n+16+0)
    qc.cx(3*n+16+0, 2*n+5)
    qc.cx(3*n+16+0, 2*n+6)
    qc.x(3*n+16+0)
    
    for index in range(1,n+1):
        qc.cx(3*n+16+index,3*n+16+index-1)
        qc.x(3*n+16+index)
        qc.ccx(3*n+16+index-1,3*n+16+index,index)
        qc.x(3*n+16+index)

def PARSENODEEVEN(qc):
    for i in range(0,n+1):
        qc.reset(3*n+16+i)
    for index in range(n,1,-1):
        qc.x(3*n+16+n)
        qc.ccx(3*n+16+index-1,3*n+16+n,index)
        if index % 2 == 0:
            qc.ccx(2*n+6,3*n+16+n,index)
        qc.x(3*n+16+n)
        qc.cx(3*n+16+index-1, 3*n+16+n)
    for index in range(1,n+1):
        qc.cx(3*n+16+index-1, 3*n+16+n)
        qc.x(3*n+16+n)
        qc.ccx(3*n+16+index-1,3*n+16+n,index)
        qc.x(3*n+16+n)
    
def TESTISPARENT(qc,color,really):
    if really == 0:
        qc.x(2*n+5)
        qc.ccx(2*n+7,2*n+5,2*n+9)
        qc.x(2*n+5)
    if color == 3:
        qc.ccx(2*n+9,2*n+6,0)
    elif color == 2:
        qc.x(0)
        qc.ccx(2*n+9,2*n+6,0)
        qc.x(0)

    if color == 1:
        qc.x(2*n+6)
        qc.ccx(2*n+7,2*n+6,0)
        qc.x(2*n+6)
    elif color == 0:
        qc.x(2*n+6)
        qc.x(0)
        qc.ccx(2*n+7,2*n+6,0)
        qc.x(0)
        qc.x(2*n+6)
    qc.x(2*n+5)
    qc.ccx(2*n+7,2*n+5,2*n+9)
    qc.x(2*n+5)

def TESTISCHILD(qc,color):
    if color == 3 or color == 2:
        qc.x(2*n+6)
        qc.cx(2*n+6, 2*n+8)
        qc.x(2*n+6)
    elif color == 1 or color == 0:
        qc.cx(2*n+6, 2*n+8)
    if color == 1 or color == 3:
        qc.x(2*n+10)

def SETPARENT(qc):
    for index in range(0,n):
        qc.ccx(n+2+index,2*n+7,index+1)
    qc.ccx(n+2+n+1,2*n+7,n+1)

def CADDNUMCLEAR(qc):
    for index in range(n-1,0,-1):
        qc.ccx(3*n+16+index,index,3*n+16+index-1)

def CADDNUM(qc):
    for i in range(0,n):
        qc.reset(3*n+16+i)
    qc.ccx(n+2+0,0,3*n+14)
    for index in range(1,n):
        qc.ccx(n+2+index,index,3*n+14)
        qc.ccx(n+2+index,3*n+16+index-1,3*n+14)
        qc.ccx(3*n+16+index,3*n+16+index-1,index)
    CADDNUMCLEAR(qc)
    

def CSUBNUMCLEAR(qc):
    for index in range(n-1,0,-1):
        qc.x(index)
        qc.ccx(3*n+16+index,index,3*n+16+index-1)
        qc.x(index)

def CSUBNUM(qc):
    for i in range(0,n):
        qc.reset(3*n+16+i)
    qc.ccx(n+2+0,0,3*n+14)
    for index in range(1,n):
        qc.ccx(n+2+index,index,3*n+14)
        qc.ccx(n+2+index,3*n+16+index-1,3*n+14)
        qc.x(index)
        qc.ccx(3*n+16+index,3*n+16+index-1,index)
        qc.x(index)
    CSUBNUMCLEAR(qc)


def DOWELD1(qc):
    qc.reset(3*n+15)
    for index in range(0,n):
        qc.ccx(3*n+15,3*n+13,2*n+11+index)
        qc.ccx(n+2+index,3*n+15,index)
    qc.ccx(n+2+n,n,3*n+13)

def DOWELD0(qc):
    qc.x(n+1)
    qc.ccx(3*n+14,3*n+13,n+1)
    qc.x(n+1)
    CADDNUM(qc)
    qc.cx(3*n+13, 3*n+14)
    CSUBNUM(qc)
    qc.ccx(3*n+14,3*n+13,n+1)

def SETWELD(qc):
    qc.x(2*n+10)
    qc.ccx(3*n+13, 2*n+10,3*n+12)
    qc.x(2*n+10)
    DOWELD0(qc)
    qc.cx(3*n+12, 3*n+13)
    DOWELD1(qc)
    qc.ccx(3*n+13, 2*n+10,3*n+12)
    qc.ccx(n+2+n+1,n+1,3*n+12)
    qc.cx(3*n+12, n+2+n)
    qc.cx(3*n+12, n+2+n+1)

def SETCHILDINTREE(qc):
    qc.ccx(n+2+0,3*n+12,2*n+10)
    for index in range(1,n+1):
        qc.ccx(n+2+index,3*n+12, index-1)
    qc.ccx(n+2+n+1, 3*n+12, n+1)

def SETCHILD(qc):
    qc.ccx(3*n+12, 2*n+8,n)
    SETWELD(qc)
    qc.cx(2*n+8, 3*n+12)
    SETCHILDINTREE(qc)
    qc.x(n)
    qc.ccx(3*n+12, 2*n+8, n)
    qc.x(n)

def W(qc,q1,q2):
    qc.cx(q2,q1)
    qc.x(q2)
    qc.sdg(q2)
    qc.h(q2)
    qc.tdg(q2)
    qc.cx(q1,q2)
    qc.t(q2)
    qc.h(q2)
    qc.s(q2)
    qc.x(q2)
    qc.cx(q2,q1)

def TIMESTEP(qc):
    qc.reset(3*n+11)
    for i in range(0,n+2):
        W(qc,i,n+2+i)
    for j in range(0,n+2):
        qc.x(n+2+j)
        qc.ccx(3*n+11,j,n+2+j)
        qc.x(n+2+j)
    qc.x(2*n+4)
    controlled_expZ(qc,3*n+11,2*n+4)
    qc.x(2*n+4)
    for j in range(n+1,-1,-1):
        qc.x(n+2+j)
        qc.ccx(3*n+11,j,n+2+j)
        qc.x(n+2+j)
    for i in range(0,n+2):
        W(qc,i,n+2+i)

def ORACLE(qc,color):
    PARSENODEROOT(qc)
    PARSENODEEVEN(qc)
    TESTISPARENT(qc,color,1)
    TESTISCHILD(qc,color)
    SETPARENT(qc)
    SETCHILD(qc)
  
    qc.x(2*n+7)
    qc.x(2*n+8)
    qc.ccx(2*n+4,2*n+7,2*n+8)
    qc.x(2*n+8)
    qc.x(2*n+7)
  
    TESTISCHILD(qc,color)
    TESTISPARENT(qc,color,0)
    PARSENODEEVEN(qc)
    PARSENODEROOT(qc)

n_qubits = 4*n+17
qc = QuantumCircuit(n_qubits, n_qubits)
qc.reset(2*n+4)
qc.reset(0)
qc.x(0)
qc.reset(n+2)

for j in range(1,n+2):
    qc.reset(j)
    qc.reset(n+2+j)

for i in range(1,s_+1):
    for color in range(0,4):
        ORACLE(qc,color)
        TIMESTEP(qc)
        ORACLE(qc,color)

qc.measure_all()

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/binary_welded_tree_n" + str(n_qubits) + ".qasm","w")
qasm_file.write(qc.qasm())
qasm_file.close()

#simulator = Aer.get_backend('qasm_simulator')
#job = execute(qc,simulator,shots=10)
#result = job.result()
#counts = result.get_counts(qc)
#print (counts)



