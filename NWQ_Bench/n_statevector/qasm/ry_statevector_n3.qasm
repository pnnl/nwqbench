OPENQASM 2.0;
include "qelib1.inc";
qreg q0[3];
creg meas[3];
ry(2.1506626) q0[0];
ry(1.4482467) q0[1];
ry(2.3705663) q0[2];
barrier q0[0],q0[1],q0[2];
measure q0[0] -> meas[0];
measure q0[1] -> meas[1];
measure q0[2] -> meas[2];
