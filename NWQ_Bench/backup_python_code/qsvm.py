# Paper link : https://arxiv.org/pdf/1804.11326.pdf

import numpy as np
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
import sys
import random
import math
from math import pi,log
import qiskit
import matplotlib.pyplot as plt
from qiskit.aqua.algorithms import QSVM
from qiskit.aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
from qiskit.ml.datasets import ad_hoc_data, sample_ad_hoc_data
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from qiskit.ml.datasets import breast_cancer
from qiskit.ml.datasets import breast_cancer

feature_dim = int(sys.argv[1])

k = 5

data = np.random.rand(100,k) * np.pi

train = data[0:50]
test = data[50:]
target = np.ones(100).astype('int')
target[:50] = 0
target = target
train_label = target[:50]
target_label = target[50:]
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


feature_map = qiskit.circuit.library.ZZFeatureMap(feature_dimension=feature_dim, reps=1,entanglement='linear')
qsvm = QSVM(feature_map, train_data, test_data)
circuit = qsvm.construct_circuit(train_data['A'][0],train_data['B'][1],measurement=True)
circuit.decompose().draw(output='mpl')
plt.show()
qasm_file = open(f"qsvm_{feature_dim}.qasm","w")
qasm_file.write(circuit().qasm())
qasm_file.close()