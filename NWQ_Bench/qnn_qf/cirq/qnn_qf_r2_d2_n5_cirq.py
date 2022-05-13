import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

circuit = cirq.Circuit(
    cirq.ry(0.74112722)(q[0]),
    cirq.ry(1.1897021)(q[1]),
    cirq.ry(1.6820708)(q[2]),
    cirq.ry(0.95224137).controlled().on(q[0], q[1]),
    cirq.ry(0.68008628).controlled().on(q[1], q[2]),
    cirq.ry(1.9511137).controlled().on(q[2], q[0]),
    cirq.ry(0.75913465)(q[0]),
    cirq.ry(2.0517674)(q[1]),
    cirq.ry(2.3983248)(q[2]),
    cirq.ry(1.3839028).controlled().on(q[0], q[1]),
    cirq.ry(2.7005981).controlled().on(q[1], q[2]),
    cirq.ry(1.1385292).controlled().on(q[2], q[0]),
    cirq.ry(2.3976709)(q[0]),
    cirq.ry(1.7424099)(q[1]),
    cirq.ry(2.352948)(q[2]),
    cirq.ry(3.0359317).controlled().on(q[0], q[3]),
    cirq.ry(2.5548187).controlled().on(q[1], q[3]),
    cirq.ry(0.52892069).controlled().on(q[2], q[3]),
    cirq.ry(2.9779363).controlled().on(q[0], q[4]),
    cirq.ry(0.52004459).controlled().on(q[1], q[4]),
    cirq.ry(0.22143418).controlled().on(q[2], q[4]),
    cirq.measure(q[3], key='c0'),
    cirq.measure(q[4], key='c1')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c0', 'c1']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)