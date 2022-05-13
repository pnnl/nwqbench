import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(25)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(0.93346815)(q[1]),
    cirq.ry(0.82988213)(q[2]),
    cirq.ry(1.181111)(q[3]),
    cirq.ry(1.802503)(q[4]),
    cirq.ry(2.969805)(q[5]),
    cirq.ry(1.5765553)(q[6]),
    cirq.ry(1.8340893)(q[7]),
    cirq.ry(2.741925)(q[8]),
    cirq.ry(1.5106361)(q[9]),
    cirq.ry(0.76354036)(q[10]),
    cirq.ry(0.15484631)(q[11]),
    cirq.ry(1.9311432)(q[12]),
    cirq.ry(0.69057517)(q[13]),
    cirq.ry(0.74294505)(q[14]),
    cirq.ry(0.79338648)(q[15]),
    cirq.ry(1.9075145)(q[16]),
    cirq.ry(2.5852457)(q[17]),
    cirq.ry(1.5388629)(q[18]),
    cirq.ry(0.8484669)(q[19]),
    cirq.ry(1.9789905)(q[20]),
    cirq.ry(1.177473)(q[21]),
    cirq.ry(0.46112786)(q[22]),
    cirq.ry(0.17065064)(q[23]),
    cirq.ry(1.8262873)(q[24]),
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