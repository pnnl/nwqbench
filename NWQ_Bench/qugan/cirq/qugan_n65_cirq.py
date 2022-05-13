import cirq
import numpy as np
from functools import reduce

def u2(p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[1/np.sqrt(2), -np.exp(1j*p_lambda)*1/np.sqrt(2)], [np.exp(1j*p_phi)*1/np.sqrt(2), np.exp(1j*p_lambda+1j*p_phi)*1/np.sqrt(2)]]))

def u3(p_theta, p_phi, p_lambda):
    return cirq.MatrixGate(np.array([[np.cos(p_theta/2), -np.exp(1j*p_lambda)*np.sin(p_theta/2)], [np.exp(1j*p_phi)*np.sin(p_theta/2), np.exp(1j*p_lambda+1j*p_phi)*np.cos(p_theta/2)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(65)]

circuit = cirq.Circuit(
    u2(np.pi, np.pi)(q[0]),
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    # Export to cirq WARNING: unknown gate "r".,
    cirq.rx(np.pi / 2)(q[1]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[4]),
    cirq.rx(np.pi / 2)(q[5]),
    cirq.rx(np.pi / 2)(q[6]),
    cirq.rx(np.pi / 2)(q[7]),
    cirq.rx(np.pi / 2)(q[8]),
    cirq.rx(np.pi / 2)(q[9]),
    cirq.rx(np.pi / 2)(q[10]),
    cirq.rx(np.pi / 2)(q[11]),
    cirq.rx(np.pi / 2)(q[12]),
    cirq.rx(np.pi / 2)(q[13]),
    cirq.rx(np.pi / 2)(q[14]),
    cirq.rx(np.pi / 2)(q[15]),
    cirq.rx(np.pi / 2)(q[16]),
    cirq.rx(np.pi / 2)(q[17]),
    cirq.rx(np.pi / 2)(q[18]),
    cirq.rx(np.pi / 2)(q[19]),
    cirq.rx(np.pi / 2)(q[20]),
    cirq.rx(np.pi / 2)(q[21]),
    cirq.rx(np.pi / 2)(q[22]),
    cirq.rx(np.pi / 2)(q[23]),
    cirq.rx(np.pi / 2)(q[24]),
    cirq.rx(np.pi / 2)(q[25]),
    cirq.rx(np.pi / 2)(q[26]),
    cirq.rx(np.pi / 2)(q[27]),
    cirq.rx(np.pi / 2)(q[28]),
    cirq.rx(np.pi / 2)(q[29]),
    cirq.rx(np.pi / 2)(q[30]),
    cirq.rx(np.pi / 2)(q[31]),
    cirq.rx(np.pi / 2)(q[32]),
    cirq.rx(np.pi / 2)(q[33]),
    cirq.rx(np.pi / 2)(q[34]),
    cirq.rx(np.pi / 2)(q[35]),
    cirq.rx(np.pi / 2)(q[36]),
    cirq.rx(np.pi / 2)(q[37]),
    cirq.rx(np.pi / 2)(q[38]),
    cirq.rx(np.pi / 2)(q[39]),
    cirq.rx(np.pi / 2)(q[40]),
    cirq.rx(np.pi / 2)(q[41]),
    cirq.rx(np.pi / 2)(q[42]),
    cirq.rx(np.pi / 2)(q[43]),
    cirq.rx(np.pi / 2)(q[44]),
    cirq.rx(np.pi / 2)(q[45]),
    cirq.rx(np.pi / 2)(q[46]),
    cirq.rx(np.pi / 2)(q[47]),
    cirq.rx(np.pi / 2)(q[48]),
    cirq.rx(np.pi / 2)(q[49]),
    cirq.rx(np.pi / 2)(q[50]),
    cirq.rx(np.pi / 2)(q[51]),
    cirq.rx(np.pi / 2)(q[52]),
    cirq.rx(np.pi / 2)(q[53]),
    cirq.rx(np.pi / 2)(q[54]),
    cirq.rx(np.pi / 2)(q[55]),
    cirq.rx(np.pi / 2)(q[56]),
    cirq.rx(np.pi / 2)(q[57]),
    cirq.rx(np.pi / 2)(q[58]),
    cirq.rx(np.pi / 2)(q[59]),
    cirq.rx(np.pi / 2)(q[60]),
    cirq.rx(np.pi / 2)(q[61]),
    cirq.rx(np.pi / 2)(q[62]),
    cirq.rx(np.pi / 2)(q[63]),
    cirq.rx(np.pi / 2)(q[64]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[33], q[34]),
    cirq.rz(2.1326225)(q[2]),
    cirq.rz(2.5992881)(q[34]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[33], q[34]),
    cirq.rx(-np.pi / 2)(q[1]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[33]),
    cirq.rx(-np.pi / 2)(q[34]),
    u3(0, 0, 0)(q[2]),
    u3(0, 0, 0)(q[34]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[33], q[34]),
    u3(-0.1238051, 0, 0)(q[2]),
    u3(-1.3204729, 0, 0)(q[34]),
    cirq.CNOT(q[1], q[2]),
    cirq.CNOT(q[33], q[34]),
    cirq.rx(np.pi / 2)(q[2]),
    cirq.rx(np.pi / 2)(q[34]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[34], q[35]),
    cirq.rz(0.60955675)(q[3]),
    cirq.rz(3.0840557)(q[35]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[34], q[35]),
    cirq.rx(-np.pi / 2)(q[2]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[34]),
    cirq.rx(-np.pi / 2)(q[35]),
    u3(0, 0, 0)(q[3]),
    u3(0, 0, 0)(q[35]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[34], q[35]),
    u3(-0.073350091, 0, 0)(q[3]),
    u3(-0.56985898, 0, 0)(q[35]),
    cirq.CNOT(q[2], q[3]),
    cirq.CNOT(q[34], q[35]),
    cirq.rx(np.pi / 2)(q[3]),
    cirq.rx(np.pi / 2)(q[35]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[35], q[36]),
    cirq.rz(0.07095891)(q[4]),
    cirq.rz(2.1600561)(q[36]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[35], q[36]),
    cirq.rx(-np.pi / 2)(q[3]),
    cirq.rx(-np.pi / 2)(q[4]),
    cirq.rx(-np.pi / 2)(q[35]),
    cirq.rx(-np.pi / 2)(q[36]),
    u3(0, 0, 0)(q[4]),
    u3(0, 0, 0)(q[36]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[35], q[36]),
    u3(-1.070064, 0, 0)(q[4]),
    u3(-0.64846351, 0, 0)(q[36]),
    cirq.CNOT(q[3], q[4]),
    cirq.CNOT(q[35], q[36]),
    cirq.rx(np.pi / 2)(q[4]),
    cirq.rx(np.pi / 2)(q[36]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[36], q[37]),
    cirq.rz(1.9285273)(q[5]),
    cirq.rz(2.5527338)(q[37]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[36], q[37]),
    cirq.rx(-np.pi / 2)(q[4]),
    cirq.rx(-np.pi / 2)(q[5]),
    cirq.rx(-np.pi / 2)(q[36]),
    cirq.rx(-np.pi / 2)(q[37]),
    u3(0, 0, 0)(q[5]),
    u3(0, 0, 0)(q[37]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[36], q[37]),
    u3(-1.3040954, 0, 0)(q[5]),
    u3(-0.81334021, 0, 0)(q[37]),
    cirq.CNOT(q[4], q[5]),
    cirq.CNOT(q[36], q[37]),
    cirq.rx(np.pi / 2)(q[5]),
    cirq.rx(np.pi / 2)(q[37]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[37], q[38]),
    cirq.rz(1.3094099)(q[6]),
    cirq.rz(1.5159622)(q[38]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[37], q[38]),
    cirq.rx(-np.pi / 2)(q[5]),
    cirq.rx(-np.pi / 2)(q[6]),
    cirq.rx(-np.pi / 2)(q[37]),
    cirq.rx(-np.pi / 2)(q[38]),
    u3(0, 0, 0)(q[6]),
    u3(0, 0, 0)(q[38]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[37], q[38]),
    u3(-1.4618621, 0, 0)(q[6]),
    u3(-0.58187016, 0, 0)(q[38]),
    cirq.CNOT(q[5], q[6]),
    cirq.CNOT(q[37], q[38]),
    cirq.rx(np.pi / 2)(q[6]),
    cirq.rx(np.pi / 2)(q[38]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[38], q[39]),
    cirq.rz(1.2025341)(q[7]),
    cirq.rz(0.93954697)(q[39]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[38], q[39]),
    cirq.rx(-np.pi / 2)(q[6]),
    cirq.rx(-np.pi / 2)(q[7]),
    cirq.rx(-np.pi / 2)(q[38]),
    cirq.rx(-np.pi / 2)(q[39]),
    u3(0, 0, 0)(q[7]),
    u3(0, 0, 0)(q[39]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[38], q[39]),
    u3(-1.5655627, 0, 0)(q[7]),
    u3(-1.0287651, 0, 0)(q[39]),
    cirq.CNOT(q[6], q[7]),
    cirq.CNOT(q[38], q[39]),
    cirq.rx(np.pi / 2)(q[7]),
    cirq.rx(np.pi / 2)(q[39]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[39], q[40]),
    cirq.rz(0.56055484)(q[8]),
    cirq.rz(1.2783898)(q[40]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[39], q[40]),
    cirq.rx(-np.pi / 2)(q[7]),
    cirq.rx(-np.pi / 2)(q[8]),
    cirq.rx(-np.pi / 2)(q[39]),
    cirq.rx(-np.pi / 2)(q[40]),
    u3(0, 0, 0)(q[8]),
    u3(0, 0, 0)(q[40]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[39], q[40]),
    u3(-0.2789862, 0, 0)(q[8]),
    u3(-0.1967155, 0, 0)(q[40]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[39], q[40]),
    cirq.rx(np.pi / 2)(q[8]),
    cirq.rx(np.pi / 2)(q[40]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[40], q[41]),
    cirq.rz(0.55424183)(q[9]),
    cirq.rz(2.4964547)(q[41]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[40], q[41]),
    cirq.rx(-np.pi / 2)(q[8]),
    cirq.rx(-np.pi / 2)(q[9]),
    cirq.rx(-np.pi / 2)(q[40]),
    cirq.rx(-np.pi / 2)(q[41]),
    u3(0, 0, 0)(q[9]),
    u3(0, 0, 0)(q[41]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[40], q[41]),
    u3(-1.3743, 0, 0)(q[9]),
    u3(-1.1285759, 0, 0)(q[41]),
    cirq.CNOT(q[8], q[9]),
    cirq.CNOT(q[40], q[41]),
    cirq.rx(np.pi / 2)(q[9]),
    cirq.rx(np.pi / 2)(q[41]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[41], q[42]),
    cirq.rz(1.6434892)(q[10]),
    cirq.rz(1.5511031)(q[42]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[41], q[42]),
    cirq.rx(-np.pi / 2)(q[9]),
    cirq.rx(-np.pi / 2)(q[10]),
    cirq.rx(-np.pi / 2)(q[41]),
    cirq.rx(-np.pi / 2)(q[42]),
    u3(0, 0, 0)(q[10]),
    u3(0, 0, 0)(q[42]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[41], q[42]),
    u3(-1.2492124, 0, 0)(q[10]),
    u3(-0.89482599, 0, 0)(q[42]),
    cirq.CNOT(q[9], q[10]),
    cirq.CNOT(q[41], q[42]),
    cirq.rx(np.pi / 2)(q[10]),
    cirq.rx(np.pi / 2)(q[42]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[42], q[43]),
    cirq.rz(2.0672045)(q[11]),
    cirq.rz(1.0795082)(q[43]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[42], q[43]),
    cirq.rx(-np.pi / 2)(q[10]),
    cirq.rx(-np.pi / 2)(q[11]),
    cirq.rx(-np.pi / 2)(q[42]),
    cirq.rx(-np.pi / 2)(q[43]),
    u3(0, 0, 0)(q[11]),
    u3(0, 0, 0)(q[43]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[42], q[43]),
    u3(-0.34878789, 0, 0)(q[11]),
    u3(-1.0050012, 0, 0)(q[43]),
    cirq.CNOT(q[10], q[11]),
    cirq.CNOT(q[42], q[43]),
    cirq.rx(np.pi / 2)(q[11]),
    cirq.rx(np.pi / 2)(q[43]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[43], q[44]),
    cirq.rz(1.2355332)(q[12]),
    cirq.rz(2.2331017)(q[44]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[43], q[44]),
    cirq.rx(-np.pi / 2)(q[11]),
    cirq.rx(-np.pi / 2)(q[12]),
    cirq.rx(-np.pi / 2)(q[43]),
    cirq.rx(-np.pi / 2)(q[44]),
    u3(0, 0, 0)(q[12]),
    u3(0, 0, 0)(q[44]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[43], q[44]),
    u3(-1.2619787, 0, 0)(q[12]),
    u3(-0.2325188, 0, 0)(q[44]),
    cirq.CNOT(q[11], q[12]),
    cirq.CNOT(q[43], q[44]),
    cirq.rx(np.pi / 2)(q[12]),
    cirq.rx(np.pi / 2)(q[44]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[44], q[45]),
    cirq.rz(1.8357102)(q[13]),
    cirq.rz(2.9179752)(q[45]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[44], q[45]),
    cirq.rx(-np.pi / 2)(q[12]),
    cirq.rx(-np.pi / 2)(q[13]),
    cirq.rx(-np.pi / 2)(q[44]),
    cirq.rx(-np.pi / 2)(q[45]),
    u3(0, 0, 0)(q[13]),
    u3(0, 0, 0)(q[45]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[44], q[45]),
    u3(-1.0663474, 0, 0)(q[13]),
    u3(-0.8736573, 0, 0)(q[45]),
    cirq.CNOT(q[12], q[13]),
    cirq.CNOT(q[44], q[45]),
    cirq.rx(np.pi / 2)(q[13]),
    cirq.rx(np.pi / 2)(q[45]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[45], q[46]),
    cirq.rz(2.0101551)(q[14]),
    cirq.rz(1.9797768)(q[46]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[45], q[46]),
    cirq.rx(-np.pi / 2)(q[13]),
    cirq.rx(-np.pi / 2)(q[14]),
    cirq.rx(-np.pi / 2)(q[45]),
    cirq.rx(-np.pi / 2)(q[46]),
    u3(0, 0, 0)(q[14]),
    u3(0, 0, 0)(q[46]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[45], q[46]),
    u3(-0.02833167, 0, 0)(q[14]),
    u3(-0.92648115, 0, 0)(q[46]),
    cirq.CNOT(q[13], q[14]),
    cirq.CNOT(q[45], q[46]),
    cirq.rx(np.pi / 2)(q[14]),
    cirq.rx(np.pi / 2)(q[46]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[46], q[47]),
    cirq.rz(2.5928222)(q[15]),
    cirq.rz(2.0603188)(q[47]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[46], q[47]),
    cirq.rx(-np.pi / 2)(q[14]),
    cirq.rx(-np.pi / 2)(q[15]),
    cirq.rx(-np.pi / 2)(q[46]),
    cirq.rx(-np.pi / 2)(q[47]),
    u3(0, 0, 0)(q[15]),
    u3(0, 0, 0)(q[47]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[46], q[47]),
    u3(-1.3303132, 0, 0)(q[15]),
    u3(-0.24767259, 0, 0)(q[47]),
    cirq.CNOT(q[14], q[15]),
    cirq.CNOT(q[46], q[47]),
    cirq.rx(np.pi / 2)(q[15]),
    cirq.rx(np.pi / 2)(q[47]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[47], q[48]),
    cirq.rz(1.280053)(q[16]),
    cirq.rz(2.3201302)(q[48]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[47], q[48]),
    cirq.rx(-np.pi / 2)(q[15]),
    cirq.rx(-np.pi / 2)(q[16]),
    cirq.rx(-np.pi / 2)(q[47]),
    cirq.rx(-np.pi / 2)(q[48]),
    u3(0, 0, 0)(q[16]),
    u3(0, 0, 0)(q[48]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[47], q[48]),
    u3(-1.5226708, 0, 0)(q[16]),
    u3(-0.26555996, 0, 0)(q[48]),
    cirq.CNOT(q[15], q[16]),
    cirq.CNOT(q[47], q[48]),
    cirq.rx(np.pi / 2)(q[16]),
    cirq.rx(np.pi / 2)(q[48]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[48], q[49]),
    cirq.rz(2.3336259)(q[17]),
    cirq.rz(2.2480372)(q[49]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[48], q[49]),
    cirq.rx(-np.pi / 2)(q[16]),
    cirq.rx(-np.pi / 2)(q[17]),
    cirq.rx(-np.pi / 2)(q[48]),
    cirq.rx(-np.pi / 2)(q[49]),
    u3(0, 0, 0)(q[17]),
    u3(0, 0, 0)(q[49]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[48], q[49]),
    u3(-0.83796289, 0, 0)(q[17]),
    u3(-1.3917255, 0, 0)(q[49]),
    cirq.CNOT(q[16], q[17]),
    cirq.CNOT(q[48], q[49]),
    cirq.rx(np.pi / 2)(q[17]),
    cirq.rx(np.pi / 2)(q[49]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[49], q[50]),
    cirq.rz(1.5555978)(q[18]),
    cirq.rz(0.36410389)(q[50]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[49], q[50]),
    cirq.rx(-np.pi / 2)(q[17]),
    cirq.rx(-np.pi / 2)(q[18]),
    cirq.rx(-np.pi / 2)(q[49]),
    cirq.rx(-np.pi / 2)(q[50]),
    u3(0, 0, 0)(q[18]),
    u3(0, 0, 0)(q[50]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[49], q[50]),
    u3(-1.5067029, 0, 0)(q[18]),
    u3(-1.4631176, 0, 0)(q[50]),
    cirq.CNOT(q[17], q[18]),
    cirq.CNOT(q[49], q[50]),
    cirq.rx(np.pi / 2)(q[18]),
    cirq.rx(np.pi / 2)(q[50]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[50], q[51]),
    cirq.rz(2.0293988)(q[19]),
    cirq.rz(2.9267501)(q[51]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[50], q[51]),
    cirq.rx(-np.pi / 2)(q[18]),
    cirq.rx(-np.pi / 2)(q[19]),
    cirq.rx(-np.pi / 2)(q[50]),
    cirq.rx(-np.pi / 2)(q[51]),
    u3(0, 0, 0)(q[19]),
    u3(0, 0, 0)(q[51]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[50], q[51]),
    u3(-1.1411507, 0, 0)(q[19]),
    u3(-0.46225096, 0, 0)(q[51]),
    cirq.CNOT(q[18], q[19]),
    cirq.CNOT(q[50], q[51]),
    cirq.rx(np.pi / 2)(q[19]),
    cirq.rx(np.pi / 2)(q[51]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[51], q[52]),
    cirq.rz(3.0228648)(q[20]),
    cirq.rz(2.2840095)(q[52]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[51], q[52]),
    cirq.rx(-np.pi / 2)(q[19]),
    cirq.rx(-np.pi / 2)(q[20]),
    cirq.rx(-np.pi / 2)(q[51]),
    cirq.rx(-np.pi / 2)(q[52]),
    u3(0, 0, 0)(q[20]),
    u3(0, 0, 0)(q[52]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[51], q[52]),
    u3(-1.5538562, 0, 0)(q[20]),
    u3(-1.4028767, 0, 0)(q[52]),
    cirq.CNOT(q[19], q[20]),
    cirq.CNOT(q[51], q[52]),
    cirq.rx(np.pi / 2)(q[20]),
    cirq.rx(np.pi / 2)(q[52]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[52], q[53]),
    cirq.rz(2.8828939)(q[21]),
    cirq.rz(0.12864404)(q[53]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[52], q[53]),
    cirq.rx(-np.pi / 2)(q[20]),
    cirq.rx(-np.pi / 2)(q[21]),
    cirq.rx(-np.pi / 2)(q[52]),
    cirq.rx(-np.pi / 2)(q[53]),
    u3(0, 0, 0)(q[21]),
    u3(0, 0, 0)(q[53]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[52], q[53]),
    u3(-0.42818033, 0, 0)(q[21]),
    u3(-1.2328002, 0, 0)(q[53]),
    cirq.CNOT(q[20], q[21]),
    cirq.CNOT(q[52], q[53]),
    cirq.rx(np.pi / 2)(q[21]),
    cirq.rx(np.pi / 2)(q[53]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[53], q[54]),
    cirq.rz(1.6567731)(q[22]),
    cirq.rz(0.28632795)(q[54]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[53], q[54]),
    cirq.rx(-np.pi / 2)(q[21]),
    cirq.rx(-np.pi / 2)(q[22]),
    cirq.rx(-np.pi / 2)(q[53]),
    cirq.rx(-np.pi / 2)(q[54]),
    u3(0, 0, 0)(q[22]),
    u3(0, 0, 0)(q[54]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[53], q[54]),
    u3(-0.8630194, 0, 0)(q[22]),
    u3(-0.61298445, 0, 0)(q[54]),
    cirq.CNOT(q[21], q[22]),
    cirq.CNOT(q[53], q[54]),
    cirq.rx(np.pi / 2)(q[22]),
    cirq.rx(np.pi / 2)(q[54]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[54], q[55]),
    cirq.rz(1.2531216)(q[23]),
    cirq.rz(1.5912115)(q[55]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[54], q[55]),
    cirq.rx(-np.pi / 2)(q[22]),
    cirq.rx(-np.pi / 2)(q[23]),
    cirq.rx(-np.pi / 2)(q[54]),
    cirq.rx(-np.pi / 2)(q[55]),
    u3(0, 0, 0)(q[23]),
    u3(0, 0, 0)(q[55]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[54], q[55]),
    u3(-0.20983154, 0, 0)(q[23]),
    u3(-0.72834728, 0, 0)(q[55]),
    cirq.CNOT(q[22], q[23]),
    cirq.CNOT(q[54], q[55]),
    cirq.rx(np.pi / 2)(q[23]),
    cirq.rx(np.pi / 2)(q[55]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[55], q[56]),
    cirq.rz(0.44813225)(q[24]),
    cirq.rz(3.0019755)(q[56]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[55], q[56]),
    cirq.rx(-np.pi / 2)(q[23]),
    cirq.rx(-np.pi / 2)(q[24]),
    cirq.rx(-np.pi / 2)(q[55]),
    cirq.rx(-np.pi / 2)(q[56]),
    u3(0, 0, 0)(q[24]),
    u3(0, 0, 0)(q[56]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[55], q[56]),
    u3(-0.18094276, 0, 0)(q[24]),
    u3(-0.68235224, 0, 0)(q[56]),
    cirq.CNOT(q[23], q[24]),
    cirq.CNOT(q[55], q[56]),
    cirq.rx(np.pi / 2)(q[24]),
    cirq.rx(np.pi / 2)(q[56]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[56], q[57]),
    cirq.rz(0.082978172)(q[25]),
    cirq.rz(3.1057103)(q[57]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[56], q[57]),
    cirq.rx(-np.pi / 2)(q[24]),
    cirq.rx(-np.pi / 2)(q[25]),
    cirq.rx(-np.pi / 2)(q[56]),
    cirq.rx(-np.pi / 2)(q[57]),
    u3(0, 0, 0)(q[25]),
    u3(0, 0, 0)(q[57]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[56], q[57]),
    u3(-0.28335569, 0, 0)(q[25]),
    u3(-0.40333772, 0, 0)(q[57]),
    cirq.CNOT(q[24], q[25]),
    cirq.CNOT(q[56], q[57]),
    cirq.rx(np.pi / 2)(q[25]),
    cirq.rx(np.pi / 2)(q[57]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[57], q[58]),
    cirq.rz(0.334982)(q[26]),
    cirq.rz(0.89718806)(q[58]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[57], q[58]),
    cirq.rx(-np.pi / 2)(q[25]),
    cirq.rx(-np.pi / 2)(q[26]),
    cirq.rx(-np.pi / 2)(q[57]),
    cirq.rx(-np.pi / 2)(q[58]),
    u3(0, 0, 0)(q[26]),
    u3(0, 0, 0)(q[58]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[57], q[58]),
    u3(-1.3337842, 0, 0)(q[26]),
    u3(-0.91118801, 0, 0)(q[58]),
    cirq.CNOT(q[25], q[26]),
    cirq.CNOT(q[57], q[58]),
    cirq.rx(np.pi / 2)(q[26]),
    cirq.rx(np.pi / 2)(q[58]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[58], q[59]),
    cirq.rz(2.7250419)(q[27]),
    cirq.rz(2.3662803)(q[59]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[58], q[59]),
    cirq.rx(-np.pi / 2)(q[26]),
    cirq.rx(-np.pi / 2)(q[27]),
    cirq.rx(-np.pi / 2)(q[58]),
    cirq.rx(-np.pi / 2)(q[59]),
    u3(0, 0, 0)(q[27]),
    u3(0, 0, 0)(q[59]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[58], q[59]),
    u3(-0.90962314, 0, 0)(q[27]),
    u3(-0.28325665, 0, 0)(q[59]),
    cirq.CNOT(q[26], q[27]),
    cirq.CNOT(q[58], q[59]),
    cirq.rx(np.pi / 2)(q[27]),
    cirq.rx(np.pi / 2)(q[59]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[59], q[60]),
    cirq.rz(0.3558715)(q[28]),
    cirq.rz(0.90177392)(q[60]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[59], q[60]),
    cirq.rx(-np.pi / 2)(q[27]),
    cirq.rx(-np.pi / 2)(q[28]),
    cirq.rx(-np.pi / 2)(q[59]),
    cirq.rx(-np.pi / 2)(q[60]),
    u3(0, 0, 0)(q[28]),
    u3(0, 0, 0)(q[60]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[59], q[60]),
    u3(-0.71850312, 0, 0)(q[28]),
    u3(-0.69136665, 0, 0)(q[60]),
    cirq.CNOT(q[27], q[28]),
    cirq.CNOT(q[59], q[60]),
    cirq.rx(np.pi / 2)(q[28]),
    cirq.rx(np.pi / 2)(q[60]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[60], q[61]),
    cirq.rz(0.31873261)(q[29]),
    cirq.rz(0.14310722)(q[61]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[60], q[61]),
    cirq.rx(-np.pi / 2)(q[28]),
    cirq.rx(-np.pi / 2)(q[29]),
    cirq.rx(-np.pi / 2)(q[60]),
    cirq.rx(-np.pi / 2)(q[61]),
    u3(0, 0, 0)(q[29]),
    u3(0, 0, 0)(q[61]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[60], q[61]),
    u3(-1.4297983, 0, 0)(q[29]),
    u3(-1.1465328, 0, 0)(q[61]),
    cirq.CNOT(q[28], q[29]),
    cirq.CNOT(q[60], q[61]),
    cirq.rx(np.pi / 2)(q[29]),
    cirq.rx(np.pi / 2)(q[61]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[61], q[62]),
    cirq.rz(0.35919566)(q[30]),
    cirq.rz(3.0513977)(q[62]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[61], q[62]),
    cirq.rx(-np.pi / 2)(q[29]),
    cirq.rx(-np.pi / 2)(q[30]),
    cirq.rx(-np.pi / 2)(q[61]),
    cirq.rx(-np.pi / 2)(q[62]),
    u3(0, 0, 0)(q[30]),
    u3(0, 0, 0)(q[62]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[61], q[62]),
    u3(-1.2279201, 0, 0)(q[30]),
    u3(-0.40787137, 0, 0)(q[62]),
    cirq.CNOT(q[29], q[30]),
    cirq.CNOT(q[61], q[62]),
    cirq.rx(np.pi / 2)(q[30]),
    cirq.rx(np.pi / 2)(q[62]),
    cirq.CNOT(q[30], q[31]),
    cirq.CNOT(q[62], q[63]),
    cirq.rz(0.44237778)(q[31]),
    cirq.rz(1.4919719)(q[63]),
    cirq.CNOT(q[30], q[31]),
    cirq.CNOT(q[62], q[63]),
    cirq.rx(-np.pi / 2)(q[30]),
    cirq.rx(-np.pi / 2)(q[31]),
    cirq.rx(-np.pi / 2)(q[62]),
    cirq.rx(-np.pi / 2)(q[63]),
    u3(0, 0, 0)(q[31]),
    u3(0, 0, 0)(q[63]),
    cirq.CNOT(q[30], q[31]),
    cirq.CNOT(q[62], q[63]),
    u3(-1.5152635, 0, 0)(q[31]),
    u3(-1.0966814, 0, 0)(q[63]),
    cirq.CNOT(q[30], q[31]),
    cirq.CNOT(q[62], q[63]),
    cirq.rx(np.pi / 2)(q[31]),
    cirq.rx(np.pi / 2)(q[63]),
    cirq.CNOT(q[31], q[32]),
    cirq.CNOT(q[63], q[64]),
    cirq.rz(2.9660002)(q[32]),
    cirq.rz(0.90310564)(q[64]),
    cirq.CNOT(q[31], q[32]),
    cirq.CNOT(q[63], q[64]),
    cirq.rx(-np.pi / 2)(q[31]),
    cirq.rx(-np.pi / 2)(q[32]),
    cirq.rx(-np.pi / 2)(q[63]),
    cirq.rx(-np.pi / 2)(q[64]),
    u3(0, 0, 0)(q[32]),
    u3(0, 0, 0)(q[64]),
    cirq.CNOT(q[31], q[32]),
    cirq.CNOT(q[63], q[64]),
    u3(-0.8690639, 0, 0)(q[32]),
    u3(-1.3558226, 0, 0)(q[64]),
    cirq.CNOT(q[31], q[32]),
    cirq.CNOT(q[63], q[64]),
    cirq.CNOT(q[33], q[1]),
    cirq.CCX(q[0], q[1], q[33]),
    cirq.CNOT(q[33], q[1]),
    cirq.CNOT(q[34], q[2]),
    cirq.CCX(q[0], q[2], q[34]),
    cirq.CNOT(q[34], q[2]),
    cirq.CNOT(q[35], q[3]),
    cirq.CCX(q[0], q[3], q[35]),
    cirq.CNOT(q[35], q[3]),
    cirq.CNOT(q[36], q[4]),
    cirq.CCX(q[0], q[4], q[36]),
    cirq.CNOT(q[36], q[4]),
    cirq.CNOT(q[37], q[5]),
    cirq.CCX(q[0], q[5], q[37]),
    cirq.CNOT(q[37], q[5]),
    cirq.CNOT(q[38], q[6]),
    cirq.CCX(q[0], q[6], q[38]),
    cirq.CNOT(q[38], q[6]),
    cirq.CNOT(q[39], q[7]),
    cirq.CCX(q[0], q[7], q[39]),
    cirq.CNOT(q[39], q[7]),
    cirq.CNOT(q[40], q[8]),
    cirq.CCX(q[0], q[8], q[40]),
    cirq.CNOT(q[40], q[8]),
    cirq.CNOT(q[41], q[9]),
    cirq.CCX(q[0], q[9], q[41]),
    cirq.CNOT(q[41], q[9]),
    cirq.CNOT(q[42], q[10]),
    cirq.CCX(q[0], q[10], q[42]),
    cirq.CNOT(q[42], q[10]),
    cirq.CNOT(q[43], q[11]),
    cirq.CCX(q[0], q[11], q[43]),
    cirq.CNOT(q[43], q[11]),
    cirq.CNOT(q[44], q[12]),
    cirq.CCX(q[0], q[12], q[44]),
    cirq.CNOT(q[44], q[12]),
    cirq.CNOT(q[45], q[13]),
    cirq.CCX(q[0], q[13], q[45]),
    cirq.CNOT(q[45], q[13]),
    cirq.CNOT(q[46], q[14]),
    cirq.CCX(q[0], q[14], q[46]),
    cirq.CNOT(q[46], q[14]),
    cirq.CNOT(q[47], q[15]),
    cirq.CCX(q[0], q[15], q[47]),
    cirq.CNOT(q[47], q[15]),
    cirq.CNOT(q[48], q[16]),
    cirq.CCX(q[0], q[16], q[48]),
    cirq.CNOT(q[48], q[16]),
    cirq.CNOT(q[49], q[17]),
    cirq.CCX(q[0], q[17], q[49]),
    cirq.CNOT(q[49], q[17]),
    cirq.CNOT(q[50], q[18]),
    cirq.CCX(q[0], q[18], q[50]),
    cirq.CNOT(q[50], q[18]),
    cirq.CNOT(q[51], q[19]),
    cirq.CCX(q[0], q[19], q[51]),
    cirq.CNOT(q[51], q[19]),
    cirq.CNOT(q[52], q[20]),
    cirq.CCX(q[0], q[20], q[52]),
    cirq.CNOT(q[52], q[20]),
    cirq.CNOT(q[53], q[21]),
    cirq.CCX(q[0], q[21], q[53]),
    cirq.CNOT(q[53], q[21]),
    cirq.CNOT(q[54], q[22]),
    cirq.CCX(q[0], q[22], q[54]),
    cirq.CNOT(q[54], q[22]),
    cirq.CNOT(q[55], q[23]),
    cirq.CCX(q[0], q[23], q[55]),
    cirq.CNOT(q[55], q[23]),
    cirq.CNOT(q[56], q[24]),
    cirq.CCX(q[0], q[24], q[56]),
    cirq.CNOT(q[56], q[24]),
    cirq.CNOT(q[57], q[25]),
    cirq.CCX(q[0], q[25], q[57]),
    cirq.CNOT(q[57], q[25]),
    cirq.CNOT(q[58], q[26]),
    cirq.CCX(q[0], q[26], q[58]),
    cirq.CNOT(q[58], q[26]),
    cirq.CNOT(q[59], q[27]),
    cirq.CCX(q[0], q[27], q[59]),
    cirq.CNOT(q[59], q[27]),
    cirq.CNOT(q[60], q[28]),
    cirq.CCX(q[0], q[28], q[60]),
    cirq.CNOT(q[60], q[28]),
    cirq.CNOT(q[61], q[29]),
    cirq.CCX(q[0], q[29], q[61]),
    cirq.CNOT(q[61], q[29]),
    cirq.CNOT(q[62], q[30]),
    cirq.CCX(q[0], q[30], q[62]),
    cirq.CNOT(q[62], q[30]),
    cirq.CNOT(q[63], q[31]),
    cirq.CCX(q[0], q[31], q[63]),
    cirq.CNOT(q[63], q[31]),
    cirq.CNOT(q[64], q[32]),
    cirq.CCX(q[0], q[32], q[64]),
    u2(np.pi, np.pi)(q[0]),
    cirq.CNOT(q[64], q[32]),
    cirq.measure(q[33], key='c00'),
    cirq.measure(q[34], key='c01'),
    cirq.measure(q[35], key='c02'),
    cirq.measure(q[36], key='c03'),
    cirq.measure(q[37], key='c04'),
    cirq.measure(q[38], key='c05'),
    cirq.measure(q[39], key='c06'),
    cirq.measure(q[40], key='c07'),
    cirq.measure(q[41], key='c08'),
    cirq.measure(q[42], key='c09'),
    cirq.measure(q[43], key='c010'),
    cirq.measure(q[44], key='c011'),
    cirq.measure(q[45], key='c012'),
    cirq.measure(q[46], key='c013'),
    cirq.measure(q[47], key='c014'),
    cirq.measure(q[48], key='c015'),
    cirq.measure(q[49], key='c016'),
    cirq.measure(q[50], key='c017'),
    cirq.measure(q[51], key='c018'),
    cirq.measure(q[52], key='c019'),
    cirq.measure(q[53], key='c020'),
    cirq.measure(q[54], key='c021'),
    cirq.measure(q[55], key='c022'),
    cirq.measure(q[56], key='c023'),
    cirq.measure(q[57], key='c024'),
    cirq.measure(q[58], key='c025'),
    cirq.measure(q[59], key='c026'),
    cirq.measure(q[60], key='c027'),
    cirq.measure(q[61], key='c028'),
    cirq.measure(q[62], key='c029'),
    cirq.measure(q[63], key='c030'),
    cirq.measure(q[64], key='c031')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['c00', 'c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c010', 'c011', 'c012', 'c013', 'c014', 'c015', 'c016', 'c017', 'c018', 'c019', 'c020', 'c021', 'c022', 'c023', 'c024', 'c025', 'c026', 'c027', 'c028', 'c029', 'c030', 'c031']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)