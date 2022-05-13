import numpy as np
from qiskit.algorithms.linear_solvers.numpy_linear_solver import NumPyLinearSolver
from qiskit.algorithms.linear_solvers.hhl import HHL
from qiskit.compiler import transpile
import sys
import os
import qiskit

with open("../../SUPPORTED_GATES",'r') as file:
    VALID_GATES = eval(file.read())


k= int(sys.argv[1])

matrix = np.random.rand(2**k,2**k)
matrix = matrix + matrix.conj().T
vector = np.random.randint(low=0,high=2,size=2**k)

#Call HHL function for Qiskit - Easiest method.
circuit = HHL().construct_circuit(matrix,vector)
circuit.measure_all()
gg = transpile(circuit,basis_gates=VALID_GATES)

if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open("qasm/" + "hhl_" + str(gg.num_qubits) + ".qasm","w")
qasm_file.write(gg.qasm())
qasm_file.close()