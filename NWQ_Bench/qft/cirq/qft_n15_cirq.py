import cirq
import numpy as np
from functools import reduce

def u1(p_lambda):
    return cirq.MatrixGate(np.array([[1, 0], [0, np.exp(1j*p_lambda)]]))

q = [cirq.NamedQubit('q' + str(i)) for i in range(15)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    u1(np.pi / 4)(q[1]),
    u1(np.pi / 8)(q[2]),
    u1(np.pi / 16)(q[3]),
    u1(np.pi / 32)(q[4]),
    u1(np.pi / 64)(q[5]),
    u1(np.pi / 128)(q[6]),
    u1(np.pi / 256)(q[7]),
    u1(np.pi / 512)(q[8]),
    u1(np.pi / 1024)(q[9]),
    u1(np.pi / 2048)(q[10]),
    u1(np.pi / 4096)(q[11]),
    u1(np.pi / 8192)(q[12]),
    u1(np.pi / 16384)(q[13]),
    u1(np.pi / 32768)(q[14]),
    cirq.CNOT(q[1], q[0]),
    u1(-np.pi / 4)(q[0]),
    cirq.CNOT(q[1], q[0]),
    u1(np.pi / 4)(q[0]),
    cirq.H(q[1]),
    cirq.CNOT(q[2], q[0]),
    u1(-np.pi / 8)(q[0]),
    cirq.CNOT(q[2], q[0]),
    u1(np.pi / 8)(q[0]),
    u1(np.pi / 4)(q[2]),
    cirq.CNOT(q[2], q[1]),
    u1(-np.pi / 4)(q[1]),
    cirq.CNOT(q[2], q[1]),
    u1(np.pi / 4)(q[1]),
    cirq.H(q[2]),
    cirq.CNOT(q[3], q[0]),
    u1(-np.pi / 16)(q[0]),
    cirq.CNOT(q[3], q[0]),
    u1(np.pi / 16)(q[0]),
    u1(np.pi / 8)(q[3]),
    cirq.CNOT(q[3], q[1]),
    u1(-np.pi / 8)(q[1]),
    cirq.CNOT(q[3], q[1]),
    u1(np.pi / 8)(q[1]),
    u1(np.pi / 4)(q[3]),
    cirq.CNOT(q[3], q[2]),
    u1(-np.pi / 4)(q[2]),
    cirq.CNOT(q[3], q[2]),
    u1(np.pi / 4)(q[2]),
    cirq.H(q[3]),
    cirq.CNOT(q[4], q[0]),
    u1(-np.pi / 32)(q[0]),
    cirq.CNOT(q[4], q[0]),
    u1(np.pi / 32)(q[0]),
    u1(np.pi / 16)(q[4]),
    cirq.CNOT(q[4], q[1]),
    u1(-np.pi / 16)(q[1]),
    cirq.CNOT(q[4], q[1]),
    u1(np.pi / 16)(q[1]),
    u1(np.pi / 8)(q[4]),
    cirq.CNOT(q[4], q[2]),
    u1(-np.pi / 8)(q[2]),
    cirq.CNOT(q[4], q[2]),
    u1(np.pi / 8)(q[2]),
    u1(np.pi / 4)(q[4]),
    cirq.CNOT(q[4], q[3]),
    u1(-np.pi / 4)(q[3]),
    cirq.CNOT(q[4], q[3]),
    u1(np.pi / 4)(q[3]),
    cirq.H(q[4]),
    cirq.CNOT(q[5], q[0]),
    u1(-np.pi / 64)(q[0]),
    cirq.CNOT(q[5], q[0]),
    u1(np.pi / 64)(q[0]),
    u1(np.pi / 32)(q[5]),
    cirq.CNOT(q[5], q[1]),
    u1(-np.pi / 32)(q[1]),
    cirq.CNOT(q[5], q[1]),
    u1(np.pi / 32)(q[1]),
    u1(np.pi / 16)(q[5]),
    cirq.CNOT(q[5], q[2]),
    u1(-np.pi / 16)(q[2]),
    cirq.CNOT(q[5], q[2]),
    u1(np.pi / 16)(q[2]),
    u1(np.pi / 8)(q[5]),
    cirq.CNOT(q[5], q[3]),
    u1(-np.pi / 8)(q[3]),
    cirq.CNOT(q[5], q[3]),
    u1(np.pi / 8)(q[3]),
    u1(np.pi / 4)(q[5]),
    cirq.CNOT(q[5], q[4]),
    u1(-np.pi / 4)(q[4]),
    cirq.CNOT(q[5], q[4]),
    u1(np.pi / 4)(q[4]),
    cirq.H(q[5]),
    cirq.CNOT(q[6], q[0]),
    u1(-np.pi / 128)(q[0]),
    cirq.CNOT(q[6], q[0]),
    u1(np.pi / 128)(q[0]),
    u1(np.pi / 64)(q[6]),
    cirq.CNOT(q[6], q[1]),
    u1(-np.pi / 64)(q[1]),
    cirq.CNOT(q[6], q[1]),
    u1(np.pi / 64)(q[1]),
    u1(np.pi / 32)(q[6]),
    cirq.CNOT(q[6], q[2]),
    u1(-np.pi / 32)(q[2]),
    cirq.CNOT(q[6], q[2]),
    u1(np.pi / 32)(q[2]),
    u1(np.pi / 16)(q[6]),
    cirq.CNOT(q[6], q[3]),
    u1(-np.pi / 16)(q[3]),
    cirq.CNOT(q[6], q[3]),
    u1(np.pi / 16)(q[3]),
    u1(np.pi / 8)(q[6]),
    cirq.CNOT(q[6], q[4]),
    u1(-np.pi / 8)(q[4]),
    cirq.CNOT(q[6], q[4]),
    u1(np.pi / 8)(q[4]),
    u1(np.pi / 4)(q[6]),
    cirq.CNOT(q[6], q[5]),
    u1(-np.pi / 4)(q[5]),
    cirq.CNOT(q[6], q[5]),
    u1(np.pi / 4)(q[5]),
    cirq.H(q[6]),
    cirq.CNOT(q[7], q[0]),
    u1(-np.pi / 256)(q[0]),
    cirq.CNOT(q[7], q[0]),
    u1(np.pi / 256)(q[0]),
    u1(np.pi / 128)(q[7]),
    cirq.CNOT(q[7], q[1]),
    u1(-np.pi / 128)(q[1]),
    cirq.CNOT(q[7], q[1]),
    u1(np.pi / 128)(q[1]),
    u1(np.pi / 64)(q[7]),
    cirq.CNOT(q[7], q[2]),
    u1(-np.pi / 64)(q[2]),
    cirq.CNOT(q[7], q[2]),
    u1(np.pi / 64)(q[2]),
    u1(np.pi / 32)(q[7]),
    cirq.CNOT(q[7], q[3]),
    u1(-np.pi / 32)(q[3]),
    cirq.CNOT(q[7], q[3]),
    u1(np.pi / 32)(q[3]),
    u1(np.pi / 16)(q[7]),
    cirq.CNOT(q[7], q[4]),
    u1(-np.pi / 16)(q[4]),
    cirq.CNOT(q[7], q[4]),
    u1(np.pi / 16)(q[4]),
    u1(np.pi / 8)(q[7]),
    cirq.CNOT(q[7], q[5]),
    u1(-np.pi / 8)(q[5]),
    cirq.CNOT(q[7], q[5]),
    u1(np.pi / 8)(q[5]),
    u1(np.pi / 4)(q[7]),
    cirq.CNOT(q[7], q[6]),
    u1(-np.pi / 4)(q[6]),
    cirq.CNOT(q[7], q[6]),
    u1(np.pi / 4)(q[6]),
    cirq.H(q[7]),
    cirq.CNOT(q[8], q[0]),
    u1(-np.pi / 512)(q[0]),
    cirq.CNOT(q[8], q[0]),
    u1(np.pi / 512)(q[0]),
    u1(np.pi / 256)(q[8]),
    cirq.CNOT(q[8], q[1]),
    u1(-np.pi / 256)(q[1]),
    cirq.CNOT(q[8], q[1]),
    u1(np.pi / 256)(q[1]),
    u1(np.pi / 128)(q[8]),
    cirq.CNOT(q[8], q[2]),
    u1(-np.pi / 128)(q[2]),
    cirq.CNOT(q[8], q[2]),
    u1(np.pi / 128)(q[2]),
    u1(np.pi / 64)(q[8]),
    cirq.CNOT(q[8], q[3]),
    u1(-np.pi / 64)(q[3]),
    cirq.CNOT(q[8], q[3]),
    u1(np.pi / 64)(q[3]),
    u1(np.pi / 32)(q[8]),
    cirq.CNOT(q[8], q[4]),
    u1(-np.pi / 32)(q[4]),
    cirq.CNOT(q[8], q[4]),
    u1(np.pi / 32)(q[4]),
    u1(np.pi / 16)(q[8]),
    cirq.CNOT(q[8], q[5]),
    u1(-np.pi / 16)(q[5]),
    cirq.CNOT(q[8], q[5]),
    u1(np.pi / 16)(q[5]),
    u1(np.pi / 8)(q[8]),
    cirq.CNOT(q[8], q[6]),
    u1(-np.pi / 8)(q[6]),
    cirq.CNOT(q[8], q[6]),
    u1(np.pi / 8)(q[6]),
    u1(np.pi / 4)(q[8]),
    cirq.CNOT(q[8], q[7]),
    u1(-np.pi / 4)(q[7]),
    cirq.CNOT(q[8], q[7]),
    u1(np.pi / 4)(q[7]),
    cirq.H(q[8]),
    cirq.CNOT(q[9], q[0]),
    u1(-np.pi / 1024)(q[0]),
    cirq.CNOT(q[9], q[0]),
    u1(np.pi / 1024)(q[0]),
    u1(np.pi / 512)(q[9]),
    cirq.CNOT(q[9], q[1]),
    u1(-np.pi / 512)(q[1]),
    cirq.CNOT(q[9], q[1]),
    u1(np.pi / 512)(q[1]),
    u1(np.pi / 256)(q[9]),
    cirq.CNOT(q[9], q[2]),
    u1(-np.pi / 256)(q[2]),
    cirq.CNOT(q[9], q[2]),
    u1(np.pi / 256)(q[2]),
    u1(np.pi / 128)(q[9]),
    cirq.CNOT(q[9], q[3]),
    u1(-np.pi / 128)(q[3]),
    cirq.CNOT(q[9], q[3]),
    u1(np.pi / 128)(q[3]),
    u1(np.pi / 64)(q[9]),
    cirq.CNOT(q[9], q[4]),
    u1(-np.pi / 64)(q[4]),
    cirq.CNOT(q[9], q[4]),
    u1(np.pi / 64)(q[4]),
    u1(np.pi / 32)(q[9]),
    cirq.CNOT(q[9], q[5]),
    u1(-np.pi / 32)(q[5]),
    cirq.CNOT(q[9], q[5]),
    u1(np.pi / 32)(q[5]),
    u1(np.pi / 16)(q[9]),
    cirq.CNOT(q[9], q[6]),
    u1(-np.pi / 16)(q[6]),
    cirq.CNOT(q[9], q[6]),
    u1(np.pi / 16)(q[6]),
    u1(np.pi / 8)(q[9]),
    cirq.CNOT(q[9], q[7]),
    u1(-np.pi / 8)(q[7]),
    cirq.CNOT(q[9], q[7]),
    u1(np.pi / 8)(q[7]),
    u1(np.pi / 4)(q[9]),
    cirq.CNOT(q[9], q[8]),
    u1(-np.pi / 4)(q[8]),
    cirq.CNOT(q[9], q[8]),
    u1(np.pi / 4)(q[8]),
    cirq.H(q[9]),
    cirq.CNOT(q[10], q[0]),
    u1(-np.pi / 2048)(q[0]),
    cirq.CNOT(q[10], q[0]),
    u1(np.pi / 2048)(q[0]),
    u1(np.pi / 1024)(q[10]),
    cirq.CNOT(q[10], q[1]),
    u1(-np.pi / 1024)(q[1]),
    cirq.CNOT(q[10], q[1]),
    u1(np.pi / 1024)(q[1]),
    u1(np.pi / 512)(q[10]),
    cirq.CNOT(q[10], q[2]),
    u1(-np.pi / 512)(q[2]),
    cirq.CNOT(q[10], q[2]),
    u1(np.pi / 512)(q[2]),
    u1(np.pi / 256)(q[10]),
    cirq.CNOT(q[10], q[3]),
    u1(-np.pi / 256)(q[3]),
    cirq.CNOT(q[10], q[3]),
    u1(np.pi / 256)(q[3]),
    u1(np.pi / 128)(q[10]),
    cirq.CNOT(q[10], q[4]),
    u1(-np.pi / 128)(q[4]),
    cirq.CNOT(q[10], q[4]),
    u1(np.pi / 128)(q[4]),
    u1(np.pi / 64)(q[10]),
    cirq.CNOT(q[10], q[5]),
    u1(-np.pi / 64)(q[5]),
    cirq.CNOT(q[10], q[5]),
    u1(np.pi / 64)(q[5]),
    u1(np.pi / 32)(q[10]),
    cirq.CNOT(q[10], q[6]),
    u1(-np.pi / 32)(q[6]),
    cirq.CNOT(q[10], q[6]),
    u1(np.pi / 32)(q[6]),
    u1(np.pi / 16)(q[10]),
    cirq.CNOT(q[10], q[7]),
    u1(-np.pi / 16)(q[7]),
    cirq.CNOT(q[10], q[7]),
    u1(np.pi / 16)(q[7]),
    u1(np.pi / 8)(q[10]),
    cirq.CNOT(q[10], q[8]),
    u1(-np.pi / 8)(q[8]),
    cirq.CNOT(q[10], q[8]),
    u1(np.pi / 8)(q[8]),
    u1(np.pi / 4)(q[10]),
    cirq.CNOT(q[10], q[9]),
    u1(-np.pi / 4)(q[9]),
    cirq.CNOT(q[10], q[9]),
    u1(np.pi / 4)(q[9]),
    cirq.H(q[10]),
    cirq.CNOT(q[11], q[0]),
    u1(-np.pi / 4096)(q[0]),
    cirq.CNOT(q[11], q[0]),
    u1(np.pi / 4096)(q[0]),
    u1(np.pi / 2048)(q[11]),
    cirq.CNOT(q[11], q[1]),
    u1(-np.pi / 2048)(q[1]),
    cirq.CNOT(q[11], q[1]),
    u1(np.pi / 2048)(q[1]),
    u1(np.pi / 1024)(q[11]),
    cirq.CNOT(q[11], q[2]),
    u1(-np.pi / 1024)(q[2]),
    cirq.CNOT(q[11], q[2]),
    u1(np.pi / 1024)(q[2]),
    u1(np.pi / 512)(q[11]),
    cirq.CNOT(q[11], q[3]),
    u1(-np.pi / 512)(q[3]),
    cirq.CNOT(q[11], q[3]),
    u1(np.pi / 512)(q[3]),
    u1(np.pi / 256)(q[11]),
    cirq.CNOT(q[11], q[4]),
    u1(-np.pi / 256)(q[4]),
    cirq.CNOT(q[11], q[4]),
    u1(np.pi / 256)(q[4]),
    u1(np.pi / 128)(q[11]),
    cirq.CNOT(q[11], q[5]),
    u1(-np.pi / 128)(q[5]),
    cirq.CNOT(q[11], q[5]),
    u1(np.pi / 128)(q[5]),
    u1(np.pi / 64)(q[11]),
    cirq.CNOT(q[11], q[6]),
    u1(-np.pi / 64)(q[6]),
    cirq.CNOT(q[11], q[6]),
    u1(np.pi / 64)(q[6]),
    u1(np.pi / 32)(q[11]),
    cirq.CNOT(q[11], q[7]),
    u1(-np.pi / 32)(q[7]),
    cirq.CNOT(q[11], q[7]),
    u1(np.pi / 32)(q[7]),
    u1(np.pi / 16)(q[11]),
    cirq.CNOT(q[11], q[8]),
    u1(-np.pi / 16)(q[8]),
    cirq.CNOT(q[11], q[8]),
    u1(np.pi / 16)(q[8]),
    u1(np.pi / 8)(q[11]),
    cirq.CNOT(q[11], q[9]),
    u1(-np.pi / 8)(q[9]),
    cirq.CNOT(q[11], q[9]),
    u1(np.pi / 8)(q[9]),
    u1(np.pi / 4)(q[11]),
    cirq.CNOT(q[11], q[10]),
    u1(-np.pi / 4)(q[10]),
    cirq.CNOT(q[11], q[10]),
    u1(np.pi / 4)(q[10]),
    cirq.H(q[11]),
    cirq.CNOT(q[12], q[0]),
    u1(-np.pi / 8192)(q[0]),
    cirq.CNOT(q[12], q[0]),
    u1(np.pi / 8192)(q[0]),
    u1(np.pi / 4096)(q[12]),
    cirq.CNOT(q[12], q[1]),
    u1(-np.pi / 4096)(q[1]),
    cirq.CNOT(q[12], q[1]),
    u1(np.pi / 4096)(q[1]),
    u1(np.pi / 2048)(q[12]),
    cirq.CNOT(q[12], q[2]),
    u1(-np.pi / 2048)(q[2]),
    cirq.CNOT(q[12], q[2]),
    u1(np.pi / 2048)(q[2]),
    u1(np.pi / 1024)(q[12]),
    cirq.CNOT(q[12], q[3]),
    u1(-np.pi / 1024)(q[3]),
    cirq.CNOT(q[12], q[3]),
    u1(np.pi / 1024)(q[3]),
    u1(np.pi / 512)(q[12]),
    cirq.CNOT(q[12], q[4]),
    u1(-np.pi / 512)(q[4]),
    cirq.CNOT(q[12], q[4]),
    u1(np.pi / 512)(q[4]),
    u1(np.pi / 256)(q[12]),
    cirq.CNOT(q[12], q[5]),
    u1(-np.pi / 256)(q[5]),
    cirq.CNOT(q[12], q[5]),
    u1(np.pi / 256)(q[5]),
    u1(np.pi / 128)(q[12]),
    cirq.CNOT(q[12], q[6]),
    u1(-np.pi / 128)(q[6]),
    cirq.CNOT(q[12], q[6]),
    u1(np.pi / 128)(q[6]),
    u1(np.pi / 64)(q[12]),
    cirq.CNOT(q[12], q[7]),
    u1(-np.pi / 64)(q[7]),
    cirq.CNOT(q[12], q[7]),
    u1(np.pi / 64)(q[7]),
    u1(np.pi / 32)(q[12]),
    cirq.CNOT(q[12], q[8]),
    u1(-np.pi / 32)(q[8]),
    cirq.CNOT(q[12], q[8]),
    u1(np.pi / 32)(q[8]),
    u1(np.pi / 16)(q[12]),
    cirq.CNOT(q[12], q[9]),
    u1(-np.pi / 16)(q[9]),
    cirq.CNOT(q[12], q[9]),
    u1(np.pi / 16)(q[9]),
    u1(np.pi / 8)(q[12]),
    cirq.CNOT(q[12], q[10]),
    u1(-np.pi / 8)(q[10]),
    cirq.CNOT(q[12], q[10]),
    u1(np.pi / 8)(q[10]),
    u1(np.pi / 4)(q[12]),
    cirq.CNOT(q[12], q[11]),
    u1(-np.pi / 4)(q[11]),
    cirq.CNOT(q[12], q[11]),
    u1(np.pi / 4)(q[11]),
    cirq.H(q[12]),
    cirq.CNOT(q[13], q[0]),
    u1(-np.pi / 16384)(q[0]),
    cirq.CNOT(q[13], q[0]),
    u1(np.pi / 16384)(q[0]),
    u1(np.pi / 8192)(q[13]),
    cirq.CNOT(q[13], q[1]),
    u1(-np.pi / 8192)(q[1]),
    cirq.CNOT(q[13], q[1]),
    u1(np.pi / 8192)(q[1]),
    u1(np.pi / 4096)(q[13]),
    cirq.CNOT(q[13], q[2]),
    u1(-np.pi / 4096)(q[2]),
    cirq.CNOT(q[13], q[2]),
    u1(np.pi / 4096)(q[2]),
    u1(np.pi / 2048)(q[13]),
    cirq.CNOT(q[13], q[3]),
    u1(-np.pi / 2048)(q[3]),
    cirq.CNOT(q[13], q[3]),
    u1(np.pi / 2048)(q[3]),
    u1(np.pi / 1024)(q[13]),
    cirq.CNOT(q[13], q[4]),
    u1(-np.pi / 1024)(q[4]),
    cirq.CNOT(q[13], q[4]),
    u1(np.pi / 1024)(q[4]),
    u1(np.pi / 512)(q[13]),
    cirq.CNOT(q[13], q[5]),
    u1(-np.pi / 512)(q[5]),
    cirq.CNOT(q[13], q[5]),
    u1(np.pi / 512)(q[5]),
    u1(np.pi / 256)(q[13]),
    cirq.CNOT(q[13], q[6]),
    u1(-np.pi / 256)(q[6]),
    cirq.CNOT(q[13], q[6]),
    u1(np.pi / 256)(q[6]),
    u1(np.pi / 128)(q[13]),
    cirq.CNOT(q[13], q[7]),
    u1(-np.pi / 128)(q[7]),
    cirq.CNOT(q[13], q[7]),
    u1(np.pi / 128)(q[7]),
    u1(np.pi / 64)(q[13]),
    cirq.CNOT(q[13], q[8]),
    u1(-np.pi / 64)(q[8]),
    cirq.CNOT(q[13], q[8]),
    u1(np.pi / 64)(q[8]),
    u1(np.pi / 32)(q[13]),
    cirq.CNOT(q[13], q[9]),
    u1(-np.pi / 32)(q[9]),
    cirq.CNOT(q[13], q[9]),
    u1(np.pi / 32)(q[9]),
    u1(np.pi / 16)(q[13]),
    cirq.CNOT(q[13], q[10]),
    u1(-np.pi / 16)(q[10]),
    cirq.CNOT(q[13], q[10]),
    u1(np.pi / 16)(q[10]),
    u1(np.pi / 8)(q[13]),
    cirq.CNOT(q[13], q[11]),
    u1(-np.pi / 8)(q[11]),
    cirq.CNOT(q[13], q[11]),
    u1(np.pi / 8)(q[11]),
    u1(np.pi / 4)(q[13]),
    cirq.CNOT(q[13], q[12]),
    u1(-np.pi / 4)(q[12]),
    cirq.CNOT(q[13], q[12]),
    u1(np.pi / 4)(q[12]),
    cirq.H(q[13]),
    cirq.CNOT(q[14], q[0]),
    u1(-np.pi / 32768)(q[0]),
    cirq.CNOT(q[14], q[0]),
    u1(np.pi / 32768)(q[0]),
    u1(np.pi / 16384)(q[14]),
    cirq.CNOT(q[14], q[1]),
    u1(-np.pi / 16384)(q[1]),
    cirq.CNOT(q[14], q[1]),
    u1(np.pi / 16384)(q[1]),
    u1(np.pi / 8192)(q[14]),
    cirq.CNOT(q[14], q[2]),
    u1(-np.pi / 8192)(q[2]),
    cirq.CNOT(q[14], q[2]),
    u1(np.pi / 8192)(q[2]),
    u1(np.pi / 4096)(q[14]),
    cirq.CNOT(q[14], q[3]),
    u1(-np.pi / 4096)(q[3]),
    cirq.CNOT(q[14], q[3]),
    u1(np.pi / 4096)(q[3]),
    u1(np.pi / 2048)(q[14]),
    cirq.CNOT(q[14], q[4]),
    u1(-np.pi / 2048)(q[4]),
    cirq.CNOT(q[14], q[4]),
    u1(np.pi / 2048)(q[4]),
    u1(np.pi / 1024)(q[14]),
    cirq.CNOT(q[14], q[5]),
    u1(-np.pi / 1024)(q[5]),
    cirq.CNOT(q[14], q[5]),
    u1(np.pi / 1024)(q[5]),
    u1(np.pi / 512)(q[14]),
    cirq.CNOT(q[14], q[6]),
    u1(-np.pi / 512)(q[6]),
    cirq.CNOT(q[14], q[6]),
    u1(np.pi / 512)(q[6]),
    u1(np.pi / 256)(q[14]),
    cirq.CNOT(q[14], q[7]),
    u1(-np.pi / 256)(q[7]),
    cirq.CNOT(q[14], q[7]),
    u1(np.pi / 256)(q[7]),
    u1(np.pi / 128)(q[14]),
    cirq.CNOT(q[14], q[8]),
    u1(-np.pi / 128)(q[8]),
    cirq.CNOT(q[14], q[8]),
    u1(np.pi / 128)(q[8]),
    u1(np.pi / 64)(q[14]),
    cirq.CNOT(q[14], q[9]),
    u1(-np.pi / 64)(q[9]),
    cirq.CNOT(q[14], q[9]),
    u1(np.pi / 64)(q[9]),
    u1(np.pi / 32)(q[14]),
    cirq.CNOT(q[14], q[10]),
    u1(-np.pi / 32)(q[10]),
    cirq.CNOT(q[14], q[10]),
    u1(np.pi / 32)(q[10]),
    u1(np.pi / 16)(q[14]),
    cirq.CNOT(q[14], q[11]),
    u1(-np.pi / 16)(q[11]),
    cirq.CNOT(q[14], q[11]),
    u1(np.pi / 16)(q[11]),
    u1(np.pi / 8)(q[14]),
    cirq.CNOT(q[14], q[12]),
    u1(-np.pi / 8)(q[12]),
    cirq.CNOT(q[14], q[12]),
    u1(np.pi / 8)(q[12]),
    u1(np.pi / 4)(q[14]),
    cirq.CNOT(q[14], q[13]),
    u1(-np.pi / 4)(q[13]),
    cirq.CNOT(q[14], q[13]),
    u1(np.pi / 4)(q[13]),
    cirq.H(q[14]),
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
    cirq.measure(q[14], key='meas14')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1024)
result_dict = dict(result.multi_measurement_histogram(keys=['meas0', 'meas1', 'meas2', 'meas3', 'meas4', 'meas5', 'meas6', 'meas7', 'meas8', 'meas9', 'meas10', 'meas11', 'meas12', 'meas13', 'meas14']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)