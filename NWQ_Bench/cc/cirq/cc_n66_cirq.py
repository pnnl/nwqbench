import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(66)]

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
    cirq.H(q[31]),
    cirq.H(q[32]),
    cirq.H(q[33]),
    cirq.H(q[34]),
    cirq.H(q[35]),
    cirq.H(q[36]),
    cirq.H(q[37]),
    cirq.H(q[38]),
    cirq.H(q[39]),
    cirq.H(q[40]),
    cirq.H(q[41]),
    cirq.H(q[42]),
    cirq.H(q[43]),
    cirq.H(q[44]),
    cirq.H(q[45]),
    cirq.H(q[46]),
    cirq.H(q[47]),
    cirq.H(q[48]),
    cirq.H(q[49]),
    cirq.H(q[50]),
    cirq.H(q[51]),
    cirq.H(q[52]),
    cirq.H(q[53]),
    cirq.H(q[54]),
    cirq.H(q[55]),
    cirq.H(q[56]),
    cirq.H(q[57]),
    cirq.H(q[58]),
    cirq.H(q[59]),
    cirq.H(q[60]),
    cirq.H(q[61]),
    cirq.H(q[62]),
    cirq.H(q[63]),
    cirq.H(q[64]),
    cirq.CNOT(q[0], q[65]),
    cirq.CNOT(q[1], q[65]),
    cirq.CNOT(q[2], q[65]),
    cirq.CNOT(q[3], q[65]),
    cirq.CNOT(q[4], q[65]),
    cirq.CNOT(q[5], q[65]),
    cirq.CNOT(q[6], q[65]),
    cirq.CNOT(q[7], q[65]),
    cirq.CNOT(q[8], q[65]),
    cirq.CNOT(q[9], q[65]),
    cirq.CNOT(q[10], q[65]),
    cirq.CNOT(q[11], q[65]),
    cirq.CNOT(q[12], q[65]),
    cirq.CNOT(q[13], q[65]),
    cirq.CNOT(q[14], q[65]),
    cirq.CNOT(q[15], q[65]),
    cirq.CNOT(q[16], q[65]),
    cirq.CNOT(q[17], q[65]),
    cirq.CNOT(q[18], q[65]),
    cirq.CNOT(q[19], q[65]),
    cirq.CNOT(q[20], q[65]),
    cirq.CNOT(q[21], q[65]),
    cirq.CNOT(q[22], q[65]),
    cirq.CNOT(q[23], q[65]),
    cirq.CNOT(q[24], q[65]),
    cirq.CNOT(q[25], q[65]),
    cirq.CNOT(q[26], q[65]),
    cirq.CNOT(q[27], q[65]),
    cirq.CNOT(q[28], q[65]),
    cirq.CNOT(q[29], q[65]),
    cirq.CNOT(q[30], q[65]),
    cirq.CNOT(q[31], q[65]),
    cirq.CNOT(q[32], q[65]),
    cirq.CNOT(q[33], q[65]),
    cirq.CNOT(q[34], q[65]),
    cirq.CNOT(q[35], q[65]),
    cirq.CNOT(q[36], q[65]),
    cirq.CNOT(q[37], q[65]),
    cirq.CNOT(q[38], q[65]),
    cirq.CNOT(q[39], q[65]),
    cirq.CNOT(q[40], q[65]),
    cirq.CNOT(q[41], q[65]),
    cirq.CNOT(q[42], q[65]),
    cirq.CNOT(q[43], q[65]),
    cirq.CNOT(q[44], q[65]),
    cirq.CNOT(q[45], q[65]),
    cirq.CNOT(q[46], q[65]),
    cirq.CNOT(q[47], q[65]),
    cirq.CNOT(q[48], q[65]),
    cirq.CNOT(q[49], q[65]),
    cirq.CNOT(q[50], q[65]),
    cirq.CNOT(q[51], q[65]),
    cirq.CNOT(q[52], q[65]),
    cirq.CNOT(q[53], q[65]),
    cirq.CNOT(q[54], q[65]),
    cirq.CNOT(q[55], q[65]),
    cirq.CNOT(q[56], q[65]),
    cirq.CNOT(q[57], q[65]),
    cirq.CNOT(q[58], q[65]),
    cirq.CNOT(q[59], q[65]),
    cirq.CNOT(q[60], q[65]),
    cirq.CNOT(q[61], q[65]),
    cirq.CNOT(q[62], q[65]),
    cirq.CNOT(q[63], q[65]),
    cirq.CNOT(q[64], q[65]),
    cirq.measure(q[65], key='c065'),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.X(q[65]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[65]),
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
    cirq.H(q[30]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[31]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[32]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[33]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[34]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[35]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[36]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[37]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[38]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[39]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[40]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[41]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[42]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[43]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[44]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[45]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[46]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[47]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[48]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[49]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[50]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[51]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[52]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[53]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[54]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[55]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[56]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[57]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[58]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[59]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[60]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[61]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[62]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[63]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[64]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.CNOT(q[24], q[65]),
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
    cirq.H(q[30]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[31]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[32]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[33]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[34]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[35]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[36]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[37]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[38]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[39]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[40]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[41]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[42]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[43]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[44]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[45]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[46]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[47]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[48]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[49]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[50]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[51]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[52]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[53]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[54]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[55]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[56]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[57]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[58]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[59]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[60]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[61]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[62]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[63]),
    # Export to cirq WARNING: classical control not implemented yet.
    cirq.H(q[64]),
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
    cirq.measure(q[29], key='c029'),
    cirq.measure(q[30], key='c030'),
    cirq.measure(q[31], key='c031'),
    cirq.measure(q[32], key='c032'),
    cirq.measure(q[33], key='c033'),
    cirq.measure(q[34], key='c034'),
    cirq.measure(q[35], key='c035'),
    cirq.measure(q[36], key='c036'),
    cirq.measure(q[37], key='c037'),
    cirq.measure(q[38], key='c038'),
    cirq.measure(q[39], key='c039'),
    cirq.measure(q[40], key='c040'),
    cirq.measure(q[41], key='c041'),
    cirq.measure(q[42], key='c042'),
    cirq.measure(q[43], key='c043'),
    cirq.measure(q[44], key='c044'),
    cirq.measure(q[45], key='c045'),
    cirq.measure(q[46], key='c046'),
    cirq.measure(q[47], key='c047'),
    cirq.measure(q[48], key='c048'),
    cirq.measure(q[49], key='c049'),
    cirq.measure(q[50], key='c050'),
    cirq.measure(q[51], key='c051'),
    cirq.measure(q[52], key='c052'),
    cirq.measure(q[53], key='c053'),
    cirq.measure(q[54], key='c054'),
    cirq.measure(q[55], key='c055'),
    cirq.measure(q[56], key='c056'),
    cirq.measure(q[57], key='c057'),
    cirq.measure(q[58], key='c058'),
    cirq.measure(q[59], key='c059'),
    cirq.measure(q[60], key='c060'),
    cirq.measure(q[61], key='c061'),
    cirq.measure(q[62], key='c062'),
    cirq.measure(q[63], key='c063'),
    cirq.measure(q[64], key='c064')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c065', 'c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c010', 'c011', 'c012', 'c013', 'c014', 'c015', 'c016', 'c017', 'c018', 'c019', 'c020', 'c021', 'c022', 'c023', 'c024', 'c025', 'c026', 'c027', 'c028', 'c029', 'c030', 'c031', 'c032', 'c033', 'c034', 'c035', 'c036', 'c037', 'c038', 'c039', 'c040', 'c041', 'c042', 'c043', 'c044', 'c045', 'c046', 'c047', 'c048', 'c049', 'c050', 'c051', 'c052', 'c053', 'c054', 'c055', 'c056', 'c057', 'c058', 'c059', 'c060', 'c061', 'c062', 'c063', 'c064', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)