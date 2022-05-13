import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

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
    cirq.CNOT(q[0], q[10]),
    cirq.CNOT(q[1], q[10]),
    cirq.CNOT(q[2], q[10]),
    cirq.CNOT(q[3], q[10]),
    cirq.CNOT(q[4], q[10]),
    cirq.CNOT(q[5], q[10]),
    cirq.CNOT(q[6], q[10]),
    cirq.CNOT(q[7], q[10]),
    cirq.CNOT(q[8], q[10]),
    cirq.CNOT(q[9], q[10]),
    cirq.measure(q[10], key='c010'),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.X(q[10]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[10]),
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
    cirq.CNOT(q[3], q[10]),
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
    cirq.measure(q[0], key='c00'),
    cirq.measure(q[1], key='c01'),
    cirq.measure(q[2], key='c02'),
    cirq.measure(q[3], key='c03'),
    cirq.measure(q[4], key='c04'),
    cirq.measure(q[5], key='c05'),
    cirq.measure(q[6], key='c06'),
    cirq.measure(q[7], key='c07'),
    cirq.measure(q[8], key='c08'),
    cirq.measure(q[9], key='c09')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c010', 'c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)