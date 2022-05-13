import qiskit
import sys
import os
import numpy
import pathlib
import matplotlib.pyplot as plt
import pickle

if __name__ == '__main__':
    print("Starting Program...")
    path = str(pathlib.Path().absolute())
    print(path)
    path += "/NWQ_Bench"
    files = []
    sim = qiskit.Aer.get_backend('qasm_simulator')

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.qasm' in file and 'binary_welded' not in file:
                files.append(os.path.join(r, file))
    for file in files:
        with open(file,'r') as f:
            print(f)
            circuit = qiskit.circuit.QuantumCircuit.from_qasm_file(file)
            result = qiskit.execute(circuit,sim,shots=10000).result().get_counts()
            file_name = file.strip('.qasm')
            file_name = file_name + '_results'
            with open(file_name+'.pickle', 'wb') as handle:
                pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
