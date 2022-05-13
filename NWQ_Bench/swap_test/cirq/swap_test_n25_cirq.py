import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(25)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.rx(-3.6924814)(q[1]),
    cirq.rx(5.4291652)(q[2]),
    cirq.rx(1.3594796)(q[3]),
    cirq.rx(-5.9123043)(q[4]),
    cirq.rx(-0.13186279)(q[5]),
    cirq.rx(-4.3869008)(q[6]),
    cirq.rx(4.9830092)(q[7]),
    cirq.rx(-1.4181518)(q[8]),
    cirq.rx(3.9058792)(q[9]),
    cirq.rx(2.1483107)(q[10]),
    cirq.rx(-1.552265)(q[11]),
    cirq.rx(3.5437778)(q[12]),
    cirq.rx(-3.2923147)(q[13]),
    cirq.rx(5.6875289)(q[14]),
    cirq.rx(1.2065807)(q[15]),
    cirq.rx(-6.0041031)(q[16]),
    cirq.rx(0.50271205)(q[17]),
    cirq.rx(-4.1172873)(q[18]),
    cirq.rx(4.8261369)(q[19]),
    cirq.rx(-1.5885531)(q[20]),
    cirq.rx(3.2780951)(q[21]),
    cirq.rx(2.2125048)(q[22]),
    cirq.rx(-2.1338861)(q[23]),
    cirq.rx(2.9294436)(q[24]),
    cirq.CSWAP(q[0], q[1], q[13]),
    cirq.CSWAP(q[0], q[2], q[14]),
    cirq.CSWAP(q[0], q[3], q[15]),
    cirq.CSWAP(q[0], q[4], q[16]),
    cirq.CSWAP(q[0], q[5], q[17]),
    cirq.CSWAP(q[0], q[6], q[18]),
    cirq.CSWAP(q[0], q[7], q[19]),
    cirq.CSWAP(q[0], q[8], q[20]),
    cirq.CSWAP(q[0], q[9], q[21]),
    cirq.CSWAP(q[0], q[10], q[22]),
    cirq.CSWAP(q[0], q[11], q[23]),
    cirq.CSWAP(q[0], q[12], q[24]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)