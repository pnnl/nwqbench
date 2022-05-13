import numpy as np
from qiskit import BasicAer
from qiskit.visualization import plot_histogram
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Grover
from qiskit.aqua.components.oracles import LogicalExpressionOracle, TruthTableOracle
import matplotlib.pyplot as plt
import qiskit
import sys
import os
import numpy as np

#k = int(sys.argv[1])
k=3

def random_bool():
    z = np.random.randint(0,2)
    if z == 0:
        z = -1
    return z

def sat_line(n_qubits):
    text = ''
    for i in range(n_qubits):
        text+= f"{(i+1)*random_bool()} "
    text+= "0"
    return text

def input_3sat_generation(n_qubits):
    input_3sat = f'''
    c example DIMACS-CNF 3-SAT
    p cnf {n_qubits} 1
    {sat_line(n_qubits)}
    '''
    return input_3sat

input_3sat = input_3sat_generation(k)

oracle = LogicalExpressionOracle(input_3sat)
grover = Grover(oracle)
backend = BasicAer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)
new_circuit = grover.construct_circuit()
cbits = qiskit.ClassicalRegister(k)
new_circuit.add_register(cbits)
for i in range(3):
    new_circuit.measure(new_circuit.qubits[i],cbits[i])
while True:
    old_circuit = new_circuit
    new_circuit = new_circuit.decompose()
    if old_circuit == new_circuit:
        break


if not os.path.isdir("qasm"):
    os.mkdir("qasm")
qasm_file = open(f"qasm/grover_search_n{new_circuit.num_qubits}","w")
qasm_file.write(new_circuit.qasm())
qasm_file.close()

# qasm_sim = qiskit.Aer.get_backend('aer_simulator')
# qobj = qiskit.compiler.assemble(new_circuit, backend=qasm_sim,shots=1024)
# job = qasm_sim.run(qobj).result().get_counts()
# plot_histogram(result['measurement'])
# plot_histogram(job)
# plt.show()