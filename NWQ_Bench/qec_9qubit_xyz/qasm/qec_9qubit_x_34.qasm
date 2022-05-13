OPENQASM 2.0;
include "qelib1.inc";
qreg q0[18];
qreg q1[16];
creg c0[16];
h q0[0];
cx q0[0],q0[3];
cx q0[0],q0[6];
h q0[0];
h q0[3];
h q0[6];
cx q0[0],q0[1];
cx q0[0],q0[2];
cx q0[3],q0[4];
cx q0[3],q0[5];
cx q0[6],q0[7];
cx q0[6],q0[8];
cx q0[0],q1[0];
cx q0[1],q1[0];
cx q0[1],q1[1];
cx q0[2],q1[1];
cx q0[3],q1[2];
cx q0[4],q1[2];
cx q0[4],q1[3];
cx q0[5],q1[3];
cx q0[6],q1[4];
cx q0[7],q1[4];
cx q0[7],q1[5];
cx q0[8],q1[5];
measure q1[0] -> c0[0];
measure q1[1] -> c0[1];
measure q1[2] -> c0[2];
measure q1[3] -> c0[3];
measure q1[4] -> c0[4];
measure q1[5] -> c0[5];
h q0[0];
h q0[1];
h q0[2];
h q0[3];
h q0[4];
h q0[5];
h q0[6];
h q0[7];
h q0[8];
cx q0[0],q1[6];
cx q0[3],q1[7];
cx q0[1],q1[6];
cx q0[4],q1[7];
cx q0[2],q1[6];
cx q0[5],q1[7];
cx q0[3],q1[6];
cx q0[6],q1[7];
cx q0[4],q1[6];
cx q0[7],q1[7];
cx q0[5],q1[6];
cx q0[8],q1[7];
measure q1[6] -> c0[6];
measure q1[7] -> c0[7];
h q0[0];
h q0[1];
h q0[2];
h q0[3];
h q0[4];
h q0[5];
h q0[6];
h q0[7];
h q0[9];
cx q0[9],q0[12];
cx q0[9],q0[15];
h q0[9];
h q0[12];
h q0[15];
cx q0[9],q0[10];
cx q0[9],q0[11];
cx q0[12],q0[13];
cx q0[12],q0[14];
cx q0[15],q0[16];
cx q0[15],q0[17];
cx q0[9],q1[8];
cx q0[10],q1[8];
cx q0[10],q1[9];
cx q0[11],q1[9];
cx q0[12],q1[10];
cx q0[13],q1[10];
cx q0[13],q1[11];
cx q0[14],q1[11];
cx q0[15],q1[12];
cx q0[16],q1[12];
cx q0[16],q1[13];
cx q0[17],q1[13];
measure q1[8] -> c0[8];
measure q1[9] -> c0[9];
measure q1[10] -> c0[10];
measure q1[11] -> c0[11];
measure q1[12] -> c0[12];
measure q1[13] -> c0[13];
h q0[9];
h q0[10];
h q0[11];
h q0[12];
h q0[13];
h q0[14];
h q0[15];
h q0[16];
h q0[17];
cx q0[9],q1[14];
cx q0[12],q1[15];
cx q0[10],q1[14];
cx q0[13],q1[15];
cx q0[11],q1[14];
cx q0[14],q1[15];
cx q0[12],q1[14];
cx q0[15],q1[15];
cx q0[13],q1[14];
cx q0[16],q1[15];
cx q0[14],q1[14];
cx q0[17],q1[15];
measure q1[14] -> c0[14];
measure q1[15] -> c0[15];
h q0[9];
h q0[10];
h q0[11];
h q0[12];
h q0[13];
h q0[14];
h q0[15];
h q0[16];