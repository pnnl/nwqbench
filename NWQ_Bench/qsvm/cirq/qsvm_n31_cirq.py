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
    cirq.H(q[30]),
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    # Export to cirq WARNING: unknown gate "p".,
    cirq.CNOT(q[0], q[1]),
    cirq.rz(1.0658475)(q[1]),
    cirq.CNOT(q[0], q[1]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(1.3469339)(q[2]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[2], q[3]),
    cirq.rz(2.9431296)(q[3]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(1.3326363)(q[4]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[4], q[5]),
    cirq.rz(1.1709364)(q[5]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[5], q[6]),
    cirq.rz(1.2578675)(q[6]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[6], q[7]),
    cirq.rz(2.0841463)(q[7]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[7], q[8]),
    cirq.rz(2.8192125)(q[8]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[8], q[9]),
    cirq.rz(0.98827017)(q[9]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[9], q[10]),
    cirq.rz(2.2201964)(q[10]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[10], q[11]),
    cirq.rz(1.7733241)(q[11]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[11], q[12]),
    cirq.rz(1.7470422)(q[12]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[12], q[13]),
    cirq.rz(2.965117)(q[13]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[13], q[14]),
    cirq.rz(0.69517847)(q[14]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[14], q[15]),
    cirq.rz(1.2866319)(q[15]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[15], q[16]),
    cirq.rz(1.8933975)(q[16]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[16], q[17]),
    cirq.rz(2.3583777)(q[17]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[17], q[18]),
    cirq.rz(2.2971814)(q[18]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[18], q[19]),
    cirq.rz(0.39448556)(q[19]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[19], q[20]),
    cirq.rz(0.75803471)(q[20]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[20], q[21]),
    cirq.rz(1.2243158)(q[21]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[21], q[22]),
    cirq.rz(2.5995999)(q[22]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[22], q[23]),
    cirq.rz(0.48579881)(q[23]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[23], q[24]),
    cirq.rz(2.4938932)(q[24]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[24], q[25]),
    cirq.rz(1.7565685)(q[25]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[25], q[26]),
    cirq.rz(2.812822)(q[26]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[26], q[27]),
    cirq.rz(1.442048)(q[27]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[27], q[28]),
    cirq.rz(1.1471001)(q[28]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[28], q[29]),
    cirq.rz(2.3181764)(q[29]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[29], q[30]),
    cirq.rz(1.0436577)(q[30]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[29], q[30]),
    cirq.rz(0.40805402)(q[30]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[28], q[29]),
    cirq.rz(0.84629311)(q[30]),
    cirq.rz(0.63924876)(q[29]),
    cirq.H(q[30]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[27], q[28]),
    cirq.rz(0.35765156)(q[29]),
    cirq.rz(0.83292732)(q[28]),
    cirq.H(q[29]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[26], q[27]),
    cirq.rz(0.006021643)(q[28]),
    cirq.rz(3.0760052)(q[27]),
    cirq.H(q[28]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.rz(0.6624743)(q[27]),
    cirq.rz(1.7315814)(q[26]),
    cirq.H(q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[25]),
    cirq.rz(2.9799951)(q[26]),
    cirq.rz(2.0133102)(q[25]),
    cirq.H(q[26]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[23], q[24]),
    cirq.rz(1.5385888)(q[25]),
    cirq.rz(2.6979026)(q[24]),
    cirq.H(q[25]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.rz(2.7021749)(q[24]),
    cirq.rz(1.1750932)(q[23]),
    cirq.H(q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[22]),
    cirq.rz(1.1539891)(q[23]),
    cirq.rz(1.2464143)(q[22]),
    cirq.H(q[23]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[20], q[21]),
    cirq.rz(1.4555561)(q[22]),
    cirq.rz(0.35141671)(q[21]),
    cirq.H(q[22]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.rz(0.36734002)(q[21]),
    cirq.rz(1.4009585)(q[20]),
    cirq.H(q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[19]),
    cirq.rz(1.4228222)(q[20]),
    cirq.rz(2.2241807)(q[19]),
    cirq.H(q[20]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[17], q[18]),
    cirq.rz(0.73442112)(q[19]),
    cirq.rz(0.48047704)(q[18]),
    cirq.H(q[19]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.rz(2.7364046)(q[18]),
    cirq.rz(0.62984233)(q[17]),
    cirq.H(q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[16]),
    cirq.rz(0.91873974)(q[17]),
    cirq.rz(0.68643378)(q[16]),
    cirq.H(q[17]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[14], q[15]),
    cirq.rz(1.2648829)(q[16]),
    cirq.rz(0.28424805)(q[15]),
    cirq.H(q[16]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.rz(0.80399553)(q[15]),
    cirq.rz(1.658587)(q[14]),
    cirq.H(q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[13]),
    cirq.rz(1.7682214)(q[14]),
    cirq.rz(0.95546462)(q[13]),
    cirq.H(q[14]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[11], q[12]),
    cirq.rz(2.2442394)(q[13]),
    cirq.rz(0.65522563)(q[12]),
    cirq.H(q[13]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.rz(2.0498984)(q[12]),
    cirq.rz(0.46021301)(q[11]),
    cirq.H(q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[10]),
    cirq.rz(2.4504383)(q[11]),
    cirq.rz(3.0181417)(q[10]),
    cirq.H(q[11]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[8], q[9]),
    cirq.rz(2.5382655)(q[10]),
    cirq.rz(2.0692088)(q[9]),
    cirq.H(q[10]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.rz(0.38961937)(q[9]),
    cirq.rz(2.4235063)(q[8]),
    cirq.H(q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[7]),
    cirq.rz(2.6333973)(q[8]),
    cirq.rz(0.85766872)(q[7]),
    cirq.H(q[8]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[5], q[6]),
    cirq.rz(1.7651461)(q[7]),
    cirq.rz(0.55108119)(q[6]),
    cirq.H(q[7]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.rz(0.11153918)(q[6]),
    cirq.rz(2.8027743)(q[5]),
    cirq.H(q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[4]),
    cirq.rz(0.80637318)(q[5]),
    cirq.rz(2.4302997)(q[4]),
    cirq.H(q[5]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[2], q[3]),
    cirq.rz(2.6169361)(q[4]),
    cirq.rz(2.7425702)(q[3]),
    cirq.H(q[4]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.rz(0.76340334)(q[3]),
    cirq.rz(1.4251612)(q[2]),
    cirq.H(q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[1]),
    cirq.rz(2.8449641)(q[2]),
    cirq.rz(0.9591349)(q[1]),
    cirq.H(q[2]),
    cirq.CNOT(q[0], q[1]),
    cirq.rz(0.24056166)(q[0]),
    cirq.rz(0.29896747)(q[1]),
    cirq.H(q[0]),
    cirq.H(q[1]),
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
    cirq.measure(q[30], key='meas30')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14', 'meas15', 'meas16', 'meas17', 'meas18', 'meas19', 'meas20', 'meas21', 'meas22', 'meas23', 'meas24', 'meas25', 'meas26', 'meas27', 'meas28', 'meas29', 'meas30']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)