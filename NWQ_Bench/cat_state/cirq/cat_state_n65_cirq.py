import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(65)]

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
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[30], q[31]),
    cirq.CNOT(q[31], q[32]),
    cirq.CNOT(q[32], q[33]),
    cirq.CNOT(q[33], q[34]),
    cirq.CNOT(q[34], q[35]),
    cirq.CNOT(q[35], q[36]),
    cirq.CNOT(q[36], q[37]),
    cirq.CNOT(q[37], q[38]),
    cirq.CNOT(q[38], q[39]),
    cirq.CNOT(q[39], q[40]),
    cirq.CNOT(q[40], q[41]),
    cirq.CNOT(q[41], q[42]),
    cirq.CNOT(q[42], q[43]),
    cirq.CNOT(q[43], q[44]),
    cirq.CNOT(q[44], q[45]),
    cirq.CNOT(q[45], q[46]),
    cirq.CNOT(q[46], q[47]),
    cirq.CNOT(q[47], q[48]),
    cirq.CNOT(q[48], q[49]),
    cirq.CNOT(q[49], q[50]),
    cirq.CNOT(q[50], q[51]),
    cirq.CNOT(q[51], q[52]),
    cirq.CNOT(q[52], q[53]),
    cirq.CNOT(q[53], q[54]),
    cirq.CNOT(q[54], q[55]),
    cirq.CNOT(q[55], q[56]),
    cirq.CNOT(q[56], q[57]),
    cirq.CNOT(q[57], q[58]),
    cirq.CNOT(q[58], q[59]),
    cirq.CNOT(q[59], q[60]),
    cirq.CNOT(q[60], q[61]),
    cirq.CNOT(q[61], q[62]),
    cirq.CNOT(q[62], q[63]),
    cirq.CNOT(q[63], q[64]),
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
    cirq.measure(q[29], key='meas29'),
    cirq.measure(q[30], key='meas30'),
    cirq.measure(q[31], key='meas31'),
    cirq.measure(q[32], key='meas32'),
    cirq.measure(q[33], key='meas33'),
    cirq.measure(q[34], key='meas34'),
    cirq.measure(q[35], key='meas35'),
    cirq.measure(q[36], key='meas36'),
    cirq.measure(q[37], key='meas37'),
    cirq.measure(q[38], key='meas38'),
    cirq.measure(q[39], key='meas39'),
    cirq.measure(q[40], key='meas40'),
    cirq.measure(q[41], key='meas41'),
    cirq.measure(q[42], key='meas42'),
    cirq.measure(q[43], key='meas43'),
    cirq.measure(q[44], key='meas44'),
    cirq.measure(q[45], key='meas45'),
    cirq.measure(q[46], key='meas46'),
    cirq.measure(q[47], key='meas47'),
    cirq.measure(q[48], key='meas48'),
    cirq.measure(q[49], key='meas49'),
    cirq.measure(q[50], key='meas50'),
    cirq.measure(q[51], key='meas51'),
    cirq.measure(q[52], key='meas52'),
    cirq.measure(q[53], key='meas53'),
    cirq.measure(q[54], key='meas54'),
    cirq.measure(q[55], key='meas55'),
    cirq.measure(q[56], key='meas56'),
    cirq.measure(q[57], key='meas57'),
    cirq.measure(q[58], key='meas58'),
    cirq.measure(q[59], key='meas59'),
    cirq.measure(q[60], key='meas60'),
    cirq.measure(q[61], key='meas61'),
    cirq.measure(q[62], key='meas62'),
    cirq.measure(q[63], key='meas63'),
    cirq.measure(q[64], key='meas64')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14', 'meas15', 'meas16', 'meas17', 'meas18', 'meas19', 'meas20', 'meas21', 'meas22', 'meas23', 'meas24', 'meas25', 'meas26', 'meas27', 'meas28', 'meas29', 'meas30', 'meas31', 'meas32', 'meas33', 'meas34', 'meas35', 'meas36', 'meas37', 'meas38', 'meas39', 'meas40', 'meas41', 'meas42', 'meas43', 'meas44', 'meas45', 'meas46', 'meas47', 'meas48', 'meas49', 'meas50', 'meas51', 'meas52', 'meas53', 'meas54', 'meas55', 'meas56', 'meas57', 'meas58', 'meas59', 'meas60', 'meas61', 'meas62', 'meas63', 'meas64']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)