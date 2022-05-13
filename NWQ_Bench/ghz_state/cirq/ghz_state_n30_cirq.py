import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(30)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[28], q[29]),
    cirq.measure(q[0], key='meas0'),
    cirq.measure(q[1], key='meas1'),
    cirq.measure(q[2], key='meas2'),
    cirq.measure(q[3], key='meas3'),
    cirq.measure(q[4], key='meas4'),
    cirq.measure(q[5], key='meas5'),
    cirq.measure(q[6], key='meas6'),
    cirq.measure(q[7], key='meas7'),
    cirq.measure(q[8], key='meas8'),
    cirq.measure(q[9], key='meas9'),
    cirq.measure(q[10], key='meas10'),
    cirq.measure(q[11], key='meas11'),
    cirq.measure(q[12], key='meas12'),
    cirq.measure(q[13], key='meas13'),
    cirq.measure(q[14], key='meas14'),
    cirq.measure(q[15], key='meas15'),
    cirq.measure(q[16], key='meas16'),
    cirq.measure(q[17], key='meas17'),
    cirq.measure(q[18], key='meas18'),
    cirq.measure(q[19], key='meas19'),
    cirq.measure(q[20], key='meas20'),
    cirq.measure(q[21], key='meas21'),
    cirq.measure(q[22], key='meas22'),
    cirq.measure(q[23], key='meas23'),
    cirq.measure(q[24], key='meas24'),
    cirq.measure(q[25], key='meas25'),
    cirq.measure(q[26], key='meas26'),
    cirq.measure(q[27], key='meas27'),
    cirq.measure(q[28], key='meas28'),
    cirq.measure(q[29], key='meas29')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14', 'meas15', 'meas16', 'meas17', 'meas18', 'meas19', 'meas20', 'meas21', 'meas22', 'meas23', 'meas24', 'meas25', 'meas26', 'meas27', 'meas28', 'meas29']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)