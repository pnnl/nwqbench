import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

circuit = cirq.Circuit(
    cirq.ry(3.0199575)(q[0]),
    cirq.ry(0.6849634)(q[1]),
    cirq.ry(0.19966078)(q[2]),
    cirq.ry(2.4255556)(q[3]),
    cirq.ry(0.17965019)(q[4]),
    cirq.ry(0.21137635)(q[5]),
    cirq.ry(2.1169674)(q[6]),
    cirq.ry(0.81479306).controlled().on(q[0], q[1]),
    cirq.ry(1.0362017).controlled().on(q[1], q[2]),
    cirq.ry(0.95144891).controlled().on(q[2], q[3]),
    cirq.ry(0.37686864).controlled().on(q[3], q[4]),
    cirq.ry(0.59838775).controlled().on(q[4], q[5]),
    cirq.ry(1.8460888).controlled().on(q[5], q[6]),
    cirq.ry(0.10341369).controlled().on(q[6], q[0]),
    cirq.ry(1.0081277)(q[0]),
    cirq.ry(1.8153793)(q[1]),
    cirq.ry(0.60519057)(q[2]),
    cirq.ry(2.9301845)(q[3]),
    cirq.ry(2.2280573)(q[4]),
    cirq.ry(2.5004374)(q[5]),
    cirq.ry(1.5186301)(q[6]),
    cirq.ry(2.516851).controlled().on(q[0], q[1]),
    cirq.ry(2.9520785).controlled().on(q[1], q[2]),
    cirq.ry(1.8930492).controlled().on(q[2], q[3]),
    cirq.ry(2.7177606).controlled().on(q[3], q[4]),
    cirq.ry(2.4212721).controlled().on(q[4], q[5]),
    cirq.ry(0.45559183).controlled().on(q[5], q[6]),
    cirq.ry(0.25042298).controlled().on(q[6], q[0]),
    cirq.ry(2.9043619)(q[0]),
    cirq.ry(0.66974428)(q[1]),
    cirq.ry(2.753528)(q[2]),
    cirq.ry(0.23933046)(q[3]),
    cirq.ry(0.46614657)(q[4]),
    cirq.ry(0.0071772368)(q[5]),
    cirq.ry(3.0222646)(q[6]),
    cirq.ry(2.933675).controlled().on(q[0], q[7]),
    cirq.ry(0.29781348).controlled().on(q[1], q[7]),
    cirq.ry(1.0732682).controlled().on(q[2], q[7]),
    cirq.ry(0.99333707).controlled().on(q[3], q[7]),
    cirq.ry(2.2163495).controlled().on(q[4], q[7]),
    cirq.ry(0.041894959).controlled().on(q[5], q[7]),
    cirq.ry(0.20076766).controlled().on(q[6], q[7]),
    cirq.ry(0.92724922).controlled().on(q[0], q[8]),
    cirq.ry(0.69812999).controlled().on(q[1], q[8]),
    cirq.ry(0.12907076).controlled().on(q[2], q[8]),
    cirq.ry(0.079440692).controlled().on(q[3], q[8]),
    cirq.ry(0.42589212).controlled().on(q[4], q[8]),
    cirq.ry(0.65326438).controlled().on(q[5], q[8]),
    cirq.ry(1.726853).controlled().on(q[6], q[8]),
    cirq.measure(q[7], key='c0'),
    cirq.measure(q[8], key='c1')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c0', 'c1']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)