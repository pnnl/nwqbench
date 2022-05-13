import numpy as np
from qiskit import BasicAer
from qiskit.aqua import QuantumInstance, aqua_globals
from qiskit.aqua.algorithms import VQC
from qiskit.aqua.components.optimizers import SPSA
from qiskit.circuit.library import TwoLocal, ZZFeatureMap
from qiskit.aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
import sys
import matplotlib.pyplot as plt
seed = 10599
aqua_globals.random_seed = seed



feature_dim = int(sys.argv[1])

k = 5

data = np.random.rand(10,k) * np.pi

train = data[0:5]
test = data[5:]
target = np.ones(10).astype('int')
target[:5] = 0
target = target
train_label = target[:5]
target_label = target[5:]
np.random.shuffle(target)

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
train_data  = {}
test_data = {}
for label,value in zip(train_label,train):
    if text[label] not in train_data:
        train_data[text[label]] = []
    train_data[text[label]].append(value)

for label,value in zip(target_label,test):
    if text[label] not in test_data:
        test_data[text[label]] = []
    test_data[text[label]].append(value)


for key in train_data.keys():
    train_data[key] = np.array(train_data[key])

for key in test_data.keys():
    test_data[key] = np.array(test_data[key])


def feature_mapper(data):
    t = 1
    for datapoint in data.flatten():
        t *= np.pi-datapoint



feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=1,entanglement='linear')
var_form = TwoLocal(feature_dim, ['ry', 'rz'], 'cz', reps=3)
optimizer = SPSA(maxiter=1, c0=4.0, skip_calibration=True)
vqc = VQC(optimizer, feature_map, var_form, train_data,test_data)

backend = BasicAer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=10, seed_simulator=seed, seed_transpiler=seed)

result = vqc.run(quantum_instance)

circuit = vqc.construct_circuit(test_data['A'][0],vqc.optimal_params,measurement=True)
qasm_file = open(f"vqc_n{feature_dim}.qasm","w")
qasm_file.write(circuit.decompose().qasm())
circuit.decompose().draw(output='mpl')
plt.show()
qasm_file.close()