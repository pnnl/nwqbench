import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(41)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.ry(0.50072778)(q[1]),
    cirq.ry(1.0905048)(q[2]),
    cirq.ry(0.96912599)(q[3]),
    cirq.ry(2.0864011)(q[4]),
    cirq.ry(2.7911299)(q[5]),
    cirq.ry(2.3880772)(q[6]),
    cirq.ry(2.2261445)(q[7]),
    cirq.ry(0.22184773)(q[8]),
    cirq.ry(2.7212956)(q[9]),
    cirq.ry(1.9315409)(q[10]),
    cirq.ry(2.3227224)(q[11]),
    cirq.ry(2.0549615)(q[12]),
    cirq.ry(1.3219394)(q[13]),
    cirq.ry(0.54140268)(q[14]),
    cirq.ry(1.8966163)(q[15]),
    cirq.ry(1.0842249)(q[16]),
    cirq.ry(1.3174914)(q[17]),
    cirq.ry(0.073000976)(q[18]),
    cirq.ry(1.3129869)(q[19]),
    cirq.ry(1.6354905)(q[20]),
    cirq.ry(0.8695423)(q[21]),
    cirq.ry(0.64843691)(q[22]),
    cirq.ry(2.9542704)(q[23]),
    cirq.ry(0.70479938)(q[24]),
    cirq.ry(1.8734066)(q[25]),
    cirq.ry(0.62818487)(q[26]),
    cirq.ry(1.9826479)(q[27]),
    cirq.ry(1.6334053)(q[28]),
    cirq.ry(0.73244297)(q[29]),
    cirq.ry(2.7419252)(q[30]),
    cirq.ry(0.42221128)(q[31]),
    cirq.ry(1.1315377)(q[32]),
    cirq.ry(0.6363216)(q[33]),
    cirq.ry(1.8338719)(q[34]),
    cirq.ry(1.3875238)(q[35]),
    cirq.ry(2.9311037)(q[36]),
    cirq.ry(0.54880829)(q[37]),
    cirq.ry(0.86364103)(q[38]),
    cirq.ry(1.0224812)(q[39]),
    cirq.ry(0.44227803)(q[40]),
    cirq.CSWAP(q[0], q[1], q[21]),
    cirq.CSWAP(q[0], q[2], q[22]),
    cirq.CSWAP(q[0], q[3], q[23]),
    cirq.CSWAP(q[0], q[4], q[24]),
    cirq.CSWAP(q[0], q[5], q[25]),
    cirq.CSWAP(q[0], q[6], q[26]),
    cirq.CSWAP(q[0], q[7], q[27]),
    cirq.CSWAP(q[0], q[8], q[28]),
    cirq.CSWAP(q[0], q[9], q[29]),
    cirq.CSWAP(q[0], q[10], q[30]),
    cirq.CSWAP(q[0], q[11], q[31]),
    cirq.CSWAP(q[0], q[12], q[32]),
    cirq.CSWAP(q[0], q[13], q[33]),
    cirq.CSWAP(q[0], q[14], q[34]),
    cirq.CSWAP(q[0], q[15], q[35]),
    cirq.CSWAP(q[0], q[16], q[36]),
    cirq.CSWAP(q[0], q[17], q[37]),
    cirq.CSWAP(q[0], q[18], q[38]),
    cirq.CSWAP(q[0], q[19], q[39]),
    cirq.CSWAP(q[0], q[20], q[40]),
    cirq.H(q[0]),
    cirq.measure(q[0], key='c00')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)