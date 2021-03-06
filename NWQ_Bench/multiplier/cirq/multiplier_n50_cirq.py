import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(50)]

circuit = cirq.Circuit(
    cirq.X(q[32]),
    cirq.X(q[34]),
    cirq.X(q[35]),
    cirq.X(q[43]),
    cirq.X(q[46]),
    cirq.CCX(q[40], q[30], q[1]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[40], q[31], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CCX(q[40], q[32], q[7]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[40], q[33], q[10]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[40], q[34], q[13]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[40], q[35], q[16]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[40], q[36], q[19]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[40], q[37], q[22]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[40], q[38], q[25]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[40], q[39], q[28]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[40], q[30], q[1]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[40], q[31], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[40], q[32], q[7]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[40], q[33], q[10]),
    cirq.CCX(q[40], q[34], q[13]),
    cirq.CCX(q[40], q[35], q[16]),
    cirq.CCX(q[40], q[36], q[19]),
    cirq.CCX(q[40], q[37], q[22]),
    cirq.CCX(q[40], q[38], q[25]),
    cirq.CCX(q[40], q[39], q[28]),
    cirq.CCX(q[41], q[30], q[4]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CCX(q[41], q[31], q[7]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[41], q[32], q[10]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[41], q[33], q[13]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[41], q[34], q[16]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[41], q[35], q[19]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[41], q[36], q[22]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[41], q[37], q[25]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[41], q[38], q[28]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[41], q[30], q[4]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CCX(q[41], q[31], q[7]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[41], q[32], q[10]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[41], q[33], q[13]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[41], q[34], q[16]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[41], q[35], q[19]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[41], q[36], q[22]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[41], q[37], q[25]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[41], q[38], q[28]),
    cirq.CCX(q[42], q[30], q[7]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[42], q[31], q[10]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[42], q[32], q[13]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[42], q[33], q[16]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[42], q[34], q[19]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[42], q[35], q[22]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[42], q[36], q[25]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[42], q[37], q[28]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[42], q[30], q[7]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[42], q[31], q[10]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[42], q[32], q[13]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[42], q[33], q[16]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[42], q[34], q[19]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CCX(q[42], q[35], q[22]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[42], q[36], q[25]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CCX(q[42], q[37], q[28]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[43], q[30], q[10]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[43], q[31], q[13]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[43], q[32], q[16]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[43], q[33], q[19]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[43], q[34], q[22]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[43], q[35], q[25]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[43], q[36], q[28]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[43], q[30], q[10]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[43], q[31], q[13]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[43], q[32], q[16]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[43], q[33], q[19]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[43], q[34], q[22]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[43], q[35], q[25]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[43], q[36], q[28]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CCX(q[44], q[30], q[13]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[44], q[31], q[16]),
    cirq.CNOT(q[3], q[5]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[44], q[32], q[19]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[44], q[33], q[22]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[44], q[34], q[25]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[44], q[35], q[28]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[44], q[30], q[13]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[44], q[31], q[16]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[44], q[32], q[19]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[44], q[33], q[22]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[44], q[34], q[25]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CCX(q[44], q[35], q[28]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[45], q[30], q[16]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[45], q[31], q[19]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[45], q[32], q[22]),
    cirq.CNOT(q[6], q[8]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[45], q[33], q[25]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[45], q[34], q[28]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[45], q[30], q[16]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[45], q[31], q[19]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[45], q[32], q[22]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[45], q[33], q[25]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[45], q[34], q[28]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CCX(q[46], q[30], q[19]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[46], q[31], q[22]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[46], q[32], q[25]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[46], q[33], q[28]),
    cirq.CNOT(q[9], q[11]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[46], q[30], q[19]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CCX(q[46], q[31], q[22]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[46], q[32], q[25]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[46], q[33], q[28]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[47], q[30], q[22]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[47], q[31], q[25]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[47], q[32], q[28]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[47], q[30], q[22]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CCX(q[47], q[31], q[25]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[47], q[32], q[28]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[48], q[30], q[25]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[48], q[31], q[28]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[48], q[30], q[25]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CCX(q[48], q[31], q[28]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[49], q[30], q[28]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CNOT(q[27], q[29]),
    cirq.CCX(q[24], q[26], q[27]),
    cirq.CCX(q[49], q[30], q[28]),
    cirq.CNOT(q[25], q[26]),
    cirq.CCX(q[25], q[26], q[27]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[24], q[26]),
    cirq.CCX(q[21], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CCX(q[22], q[23], q[24]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[21], q[23]),
    cirq.CCX(q[18], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CCX(q[19], q[20], q[21]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[18], q[20]),
    cirq.CCX(q[15], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CCX(q[16], q[17], q[18]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[15], q[17]),
    cirq.CCX(q[12], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CCX(q[13], q[14], q[15]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[12], q[14]),
    cirq.CCX(q[9], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CCX(q[10], q[11], q[12]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[9], q[11]),
    cirq.CCX(q[6], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CCX(q[7], q[8], q[9]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[6], q[8]),
    cirq.CCX(q[3], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CCX(q[4], q[5], q[6]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[3], q[5]),
    cirq.CCX(q[0], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CCX(q[1], q[2], q[3]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[0], q[2]),
    cirq.measure(q[2], key='c00'),
    cirq.measure(q[5], key='c01'),
    cirq.measure(q[8], key='c02'),
    cirq.measure(q[11], key='c03'),
    cirq.measure(q[14], key='c04'),
    cirq.measure(q[17], key='c05'),
    cirq.measure(q[20], key='c06'),
    cirq.measure(q[23], key='c07'),
    cirq.measure(q[26], key='c08'),
    cirq.measure(q[29], key='c09')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', ]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)