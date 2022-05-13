OPENQASM 2.0;
include "qelib1.inc";
qreg q0[11];
creg c0[11];
h q0[0];
h q0[1];
h q0[2];
h q0[3];
h q0[4];
h q0[5];
h q0[6];
h q0[7];
h q0[8];
h q0[9];
cx q0[0],q0[10];
cx q0[1],q0[10];
cx q0[2],q0[10];
cx q0[3],q0[10];
cx q0[4],q0[10];
cx q0[5],q0[10];
cx q0[6],q0[10];
cx q0[7],q0[10];
cx q0[8],q0[10];
cx q0[9],q0[10];
measure q0[10] -> c0[10];
if(c0==0) x q0[10];
if(c0==0) h q0[10];
if(c0==1024) h q0[0];
if(c0==1024) h q0[1];
if(c0==1024) h q0[2];
if(c0==1024) h q0[3];
if(c0==1024) h q0[4];
if(c0==1024) h q0[5];
if(c0==1024) h q0[6];
if(c0==1024) h q0[7];
if(c0==1024) h q0[8];
if(c0==1024) h q0[9];
barrier q0[0],q0[1],q0[2],q0[3],q0[4],q0[5],q0[6],q0[7],q0[8],q0[9],q0[10];
if(c0==0) cx q0[3],q0[10];
barrier q0[0],q0[1],q0[2],q0[3],q0[4],q0[5],q0[6],q0[7],q0[8],q0[9],q0[10];
if(c0==0) h q0[0];
if(c0==0) h q0[1];
if(c0==0) h q0[2];
if(c0==0) h q0[3];
if(c0==0) h q0[4];
if(c0==0) h q0[5];
if(c0==0) h q0[6];
if(c0==0) h q0[7];
if(c0==0) h q0[8];
if(c0==0) h q0[9];
measure q0[0] -> c0[0];
measure q0[1] -> c0[1];
measure q0[2] -> c0[2];
measure q0[3] -> c0[3];
measure q0[4] -> c0[4];
measure q0[5] -> c0[5];
measure q0[6] -> c0[6];
measure q0[7] -> c0[7];
measure q0[8] -> c0[8];
measure q0[9] -> c0[9];