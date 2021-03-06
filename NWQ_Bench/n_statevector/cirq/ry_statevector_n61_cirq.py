import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(61)]

circuit = cirq.Circuit(
    cirq.ry(2.1506626)(q[0]),
    cirq.ry(1.4482467)(q[1]),
    cirq.ry(2.3705663)(q[2]),
    cirq.ry(1.9765769)(q[3]),
    cirq.ry(0.62383312)(q[4]),
    cirq.ry(2.8280429)(q[5]),
    cirq.ry(2.120318)(q[6]),
    cirq.ry(2.1798952)(q[7]),
    cirq.ry(0.7320994)(q[8]),
    cirq.ry(1.4714046)(q[9]),
    cirq.ry(1.3094267)(q[10]),
    cirq.ry(2.5935193)(q[11]),
    cirq.ry(1.8626523)(q[12]),
    cirq.ry(2.2725045)(q[13]),
    cirq.ry(1.4573817)(q[14]),
    cirq.ry(0.99378383)(q[15]),
    cirq.ry(1.6801839)(q[16]),
    cirq.ry(0.51077586)(q[17]),
    cirq.ry(2.2853262)(q[18]),
    cirq.ry(1.8372675)(q[19]),
    cirq.ry(2.1131759)(q[20]),
    cirq.ry(1.2755787)(q[21]),
    cirq.ry(2.7975419)(q[22]),
    cirq.ry(2.4755003)(q[23]),
    cirq.ry(2.161285)(q[24]),
    cirq.ry(0.91382352)(q[25]),
    cirq.ry(1.5041891)(q[26]),
    cirq.ry(0.42170479)(q[27]),
    cirq.ry(0.80734219)(q[28]),
    cirq.ry(1.9456087)(q[29]),
    cirq.ry(2.0823405)(q[30]),
    cirq.ry(2.7791103)(q[31]),
    cirq.ry(1.2149868)(q[32]),
    cirq.ry(1.3087262)(q[33]),
    cirq.ry(1.5098703)(q[34]),
    cirq.ry(0.90070537)(q[35]),
    cirq.ry(0.73749253)(q[36]),
    cirq.ry(1.522187)(q[37]),
    cirq.ry(0.99299763)(q[38]),
    cirq.ry(1.9173177)(q[39]),
    cirq.ry(1.4447668)(q[40]),
    cirq.ry(2.2987674)(q[41]),
    cirq.ry(1.9828917)(q[42]),
    cirq.ry(1.1861118)(q[43]),
    cirq.ry(2.2976471)(q[44]),
    cirq.ry(2.2262623)(q[45]),
    cirq.ry(1.3438089)(q[46]),
    cirq.ry(1.1336633)(q[47]),
    cirq.ry(1.9444195)(q[48]),
    cirq.ry(0.76628041)(q[49]),
    cirq.ry(0.9270657)(q[50]),
    cirq.ry(0.17181861)(q[51]),
    cirq.ry(2.181994)(q[52]),
    cirq.ry(1.9067839)(q[53]),
    cirq.ry(1.9936131)(q[54]),
    cirq.ry(2.1669431)(q[55]),
    cirq.ry(1.4885351)(q[56]),
    cirq.ry(1.7087155)(q[57]),
    cirq.ry(0.76640879)(q[58]),
    cirq.ry(0.69048084)(q[59]),
    cirq.ry(1.9143189)(q[60]),
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
    cirq.measure(q[60], key='meas60')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14', 'meas15', 'meas16', 'meas17', 'meas18', 'meas19', 'meas20', 'meas21', 'meas22', 'meas23', 'meas24', 'meas25', 'meas26', 'meas27', 'meas28', 'meas29', 'meas30', 'meas31', 'meas32', 'meas33', 'meas34', 'meas35', 'meas36', 'meas37', 'meas38', 'meas39', 'meas40', 'meas41', 'meas42', 'meas43', 'meas44', 'meas45', 'meas46', 'meas47', 'meas48', 'meas49', 'meas50', 'meas51', 'meas52', 'meas53', 'meas54', 'meas55', 'meas56', 'meas57', 'meas58', 'meas59', 'meas60']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)