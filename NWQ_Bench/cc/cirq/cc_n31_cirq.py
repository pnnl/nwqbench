import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(31)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.H(q[1]),
    cirq.H(q[2]),
    cirq.H(q[3]),
    cirq.H(q[4]),
    cirq.H(q[5]),
    cirq.H(q[6]),
    cirq.H(q[7]),
    cirq.H(q[8]),
    cirq.H(q[9]),
    cirq.H(q[10]),
    cirq.H(q[11]),
    cirq.H(q[12]),
    cirq.H(q[13]),
    cirq.H(q[14]),
    cirq.H(q[15]),
    cirq.H(q[16]),
    cirq.H(q[17]),
    cirq.H(q[18]),
    cirq.H(q[19]),
    cirq.H(q[20]),
    cirq.H(q[21]),
    cirq.H(q[22]),
    cirq.H(q[23]),
    cirq.H(q[24]),
    cirq.H(q[25]),
    cirq.H(q[26]),
    cirq.H(q[27]),
    cirq.H(q[28]),
    cirq.H(q[29]),
    cirq.CNOT(q[0], q[30]),
    cirq.CNOT(q[1], q[30]),
    cirq.CNOT(q[2], q[30]),
    cirq.CNOT(q[3], q[30]),
    cirq.CNOT(q[4], q[30]),
    cirq.CNOT(q[5], q[30]),
    cirq.CNOT(q[6], q[30]),
    cirq.CNOT(q[7], q[30]),
    cirq.CNOT(q[8], q[30]),
    cirq.CNOT(q[9], q[30]),
    cirq.CNOT(q[10], q[30]),
    cirq.CNOT(q[11], q[30]),
    cirq.CNOT(q[12], q[30]),
    cirq.CNOT(q[13], q[30]),
    cirq.CNOT(q[14], q[30]),
    cirq.CNOT(q[15], q[30]),
    cirq.CNOT(q[16], q[30]),
    cirq.CNOT(q[17], q[30]),
    cirq.CNOT(q[18], q[30]),
    cirq.CNOT(q[19], q[30]),
    cirq.CNOT(q[20], q[30]),
    cirq.CNOT(q[21], q[30]),
    cirq.CNOT(q[22], q[30]),
    cirq.CNOT(q[23], q[30]),
    cirq.CNOT(q[24], q[30]),
    cirq.CNOT(q[25], q[30]),
    cirq.CNOT(q[26], q[30]),
    cirq.CNOT(q[27], q[30]),
    cirq.CNOT(q[28], q[30]),
    cirq.CNOT(q[29], q[30]),
    cirq.measure(q[30], key='c030'),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.X(q[30]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[30]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[0]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[1]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[2]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[3]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[4]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[5]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[6]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[7]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[8]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[9]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[10]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[11]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[12]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[13]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[14]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[15]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[16]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[17]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[18]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[19]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[20]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[21]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[22]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[23]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[24]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[25]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[26]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[27]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[28]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[29]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.CNOT(q[6], q[30]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[0]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[1]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[2]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[3]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[4]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[5]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[6]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[7]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[8]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[9]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[10]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[11]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[12]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[13]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[14]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[15]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[16]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[17]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[18]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[19]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[20]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[21]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[22]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[23]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[24]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[25]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[26]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[27]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[28]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[29]),
    cirq.measure(q[0], key='c00'),
    cirq.measure(q[1], key='c01'),
    cirq.measure(q[2], key='c02'),
    cirq.measure(q[3], key='c03'),
    cirq.measure(q[4], key='c04'),
    cirq.measure(q[5], key='c05'),
    cirq.measure(q[6], key='c06'),
    cirq.measure(q[7], key='c07'),
    cirq.measure(q[8], key='c08'),
    cirq.measure(q[9], key='c09'),
    cirq.measure(q[10], key='c010'),
    cirq.measure(q[11], key='c011'),
    cirq.measure(q[12], key='c012'),
    cirq.measure(q[13], key='c013'),
    cirq.measure(q[14], key='c014'),
    cirq.measure(q[15], key='c015'),
    cirq.measure(q[16], key='c016'),
    cirq.measure(q[17], key='c017'),
    cirq.measure(q[18], key='c018'),
    cirq.measure(q[19], key='c019'),
    cirq.measure(q[20], key='c020'),
    cirq.measure(q[21], key='c021'),
    cirq.measure(q[22], key='c022'),
    cirq.measure(q[23], key='c023'),
    cirq.measure(q[24], key='c024'),
    cirq.measure(q[25], key='c025'),
    cirq.measure(q[26], key='c026'),
    cirq.measure(q[27], key='c027'),
    cirq.measure(q[28], key='c028'),
    cirq.measure(q[29], key='c029')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c030', 'c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c010', 'c011', 'c012', 'c013', 'c014', 'c015', 'c016', 'c017', 'c018', 'c019', 'c020', 'c021', 'c022', 'c023', 'c024', 'c025', 'c026', 'c027', 'c028', 'c029', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)