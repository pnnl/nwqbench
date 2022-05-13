# ----------------------------------------------------------------------
# NWQBench: Northwest Quantum Proxy Application Suite
# ----------------------------------------------------------------------
# Ang Li, Samuel Stein, James Ang.
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 04/19/2021.
# ----------------------------------------------------------------------

import numpy as np
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
import sys
import random
import math
from math import pi,log
import matplotlib.pyplot as plt
import os


if len(sys.argv) < 4:
    print("Format to generate a circuit is 'python file_name n_qubits n_readouts n_layers")
    exit()

n = int(sys.argv[1])
k = int(sys.argv[2])
depth = int(sys.argv[3])


def rand():
    return np.random.rand()*pi

def RY(circ,network_qubits):
    """performs RY on all initial states"""
    for i in range(network_qubits):
        circ.ry(rand(),i)


def CRY(circ,network_qubits):
    """performs controlled ry chain on all qubits, creates cycle.
        i.e. cry from qubit 5->1, 1->2, etc."""
    for i in range(network_qubits):
        # if last state, conrol first qubit, ignore ancilla
        if i == network_qubits-1:
            circ.cry(rand(),i,0)
            continue
        circ.cry(rand(), i, i+1)

def entangle_output_neuron(circ,network_qubits,target_qubits):
    start_index = network_qubits
    for i in range(target_qubits):
        for j in range(network_qubits):
            circ.cry(rand(),j,start_index)
        start_index +=1

def measure_output_neurons(circ,network_qubits,target_qubits):
    start_index = network_qubits
    for i in range(target_qubits):
        circ.measure(start_index,i)
        start_index+=1

def create_qnn(circ,network_qubits,target_qubits,depth):
    for _ in range(depth):
        RY(circ,network_qubits)
        CRY(circ,network_qubits)
    RY(circ,network_qubits)
    entangle_output_neuron(circ,network_qubits,target_qubits)
    measure_output_neurons(circ,network_qubits,target_qubits)
    return circ


qubits = QuantumRegister(n)
cbits = ClassicalRegister(k)
circ = QuantumCircuit(n,k)
network_qubits = n-k
network = create_qnn(circ,network_qubits,k,2)
network.draw(output='mpl')
if not os.path.isdir("circuit_svg"):
    os.mkdir("circuit_svg")
try:
    plt.savefig(f"circuit_svg/qnn_qf_r"+str(k)+"_d"+str(depth)+"_n"+str(n)+".svg")
except:
    pass
if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/qnn_qf_r"+str(k)+"_d"+str(depth)+"_n"+str(n)+".qasm","w")
qasm_file.write(network.qasm())
qasm_file.close()

