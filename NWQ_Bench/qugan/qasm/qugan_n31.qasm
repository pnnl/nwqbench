OPENQASM 2.0;
include "qelib1.inc";
qreg q0[31];
creg c0[15];
u2(0,pi) q0[0];
r(1.2839456,pi/2) q0[1];
rx(pi/2) q0[1];
r(0.16078809,pi/2) q0[2];
rx(pi/2) q0[2];
cx q0[1],q0[2];
rz(1.2977392) q0[2];
cx q0[1],q0[2];
rx(-pi/2) q0[1];
rx(-pi/2) q0[2];
u3(1.4432896,0,0) q0[2];
cx q0[1],q0[2];
u3(-1.4432896,0,0) q0[2];
cx q0[1],q0[2];
rx(pi/2) q0[2];
r(1.0313405,pi/2) q0[3];
rx(pi/2) q0[3];
cx q0[2],q0[3];
rz(2.8649402) q0[3];
cx q0[2],q0[3];
rx(-pi/2) q0[2];
rx(-pi/2) q0[3];
u3(0.60753935,0,0) q0[3];
cx q0[2],q0[3];
u3(-0.60753935,0,0) q0[3];
cx q0[2],q0[3];
rx(pi/2) q0[3];
r(0.79394264,pi/2) q0[4];
rx(pi/2) q0[4];
cx q0[3],q0[4];
rz(1.2287728) q0[4];
cx q0[3],q0[4];
rx(-pi/2) q0[3];
rx(-pi/2) q0[4];
u3(0.89724501,0,0) q0[4];
cx q0[3],q0[4];
u3(-0.89724501,0,0) q0[4];
cx q0[3],q0[4];
rx(pi/2) q0[4];
r(1.5539977,pi/2) q0[5];
rx(pi/2) q0[5];
cx q0[4],q0[5];
rz(0.88703672) q0[5];
cx q0[4],q0[5];
rx(-pi/2) q0[4];
rx(-pi/2) q0[5];
u3(0.56500464,0,0) q0[5];
cx q0[4],q0[5];
u3(-0.56500464,0,0) q0[5];
cx q0[4],q0[5];
rx(pi/2) q0[5];
r(1.1326793,pi/2) q0[6];
rx(pi/2) q0[6];
cx q0[5],q0[6];
rz(1.1945889) q0[6];
cx q0[5],q0[6];
rx(-pi/2) q0[5];
rx(-pi/2) q0[6];
u3(0.78663791,0,0) q0[6];
cx q0[5],q0[6];
u3(-0.78663791,0,0) q0[6];
cx q0[5],q0[6];
rx(pi/2) q0[6];
r(2.591545,pi/2) q0[7];
rx(pi/2) q0[7];
cx q0[6],q0[7];
rz(0.98968875) q0[7];
cx q0[6],q0[7];
rx(-pi/2) q0[6];
rx(-pi/2) q0[7];
u3(1.3825416,0,0) q0[7];
cx q0[6],q0[7];
u3(-1.3825416,0,0) q0[7];
cx q0[6],q0[7];
rx(pi/2) q0[7];
r(0.67544332,pi/2) q0[8];
rx(pi/2) q0[8];
cx q0[7],q0[8];
rz(2.8925702) q0[8];
cx q0[7],q0[8];
rx(-pi/2) q0[7];
rx(-pi/2) q0[8];
u3(1.5320829,0,0) q0[8];
cx q0[7],q0[8];
u3(-1.5320829,0,0) q0[8];
cx q0[7],q0[8];
rx(pi/2) q0[8];
r(0.21561786,pi/2) q0[9];
rx(pi/2) q0[9];
cx q0[8],q0[9];
rz(2.6101061) q0[9];
cx q0[8],q0[9];
rx(-pi/2) q0[8];
rx(-pi/2) q0[9];
u3(0.67987172,0,0) q0[9];
cx q0[8],q0[9];
u3(-0.67987172,0,0) q0[9];
cx q0[8],q0[9];
rx(pi/2) q0[9];
r(0.010274407,pi/2) q0[10];
rx(pi/2) q0[10];
cx q0[9],q0[10];
rz(0.67584848) q0[10];
cx q0[9],q0[10];
rx(-pi/2) q0[10];
u3(0.30508649,0,0) q0[10];
rx(-pi/2) q0[9];
cx q0[9],q0[10];
u3(-0.30508649,0,0) q0[10];
cx q0[9],q0[10];
rx(pi/2) q0[10];
r(2.9469741,pi/2) q0[11];
rx(pi/2) q0[11];
cx q0[10],q0[11];
rz(2.8535391) q0[11];
cx q0[10],q0[11];
rx(-pi/2) q0[10];
rx(-pi/2) q0[11];
u3(1.1107695,0,0) q0[11];
cx q0[10],q0[11];
u3(-1.1107695,0,0) q0[11];
cx q0[10],q0[11];
rx(pi/2) q0[11];
r(2.6596134,pi/2) q0[12];
rx(pi/2) q0[12];
cx q0[11],q0[12];
rz(0.70415312) q0[12];
cx q0[11],q0[12];
rx(-pi/2) q0[11];
rx(-pi/2) q0[12];
u3(0.031031735,0,0) q0[12];
cx q0[11],q0[12];
u3(-0.031031735,0,0) q0[12];
cx q0[11],q0[12];
rx(pi/2) q0[12];
r(2.3895714,pi/2) q0[13];
rx(pi/2) q0[13];
cx q0[12],q0[13];
rz(0.60245421) q0[13];
cx q0[12],q0[13];
rx(-pi/2) q0[12];
rx(-pi/2) q0[13];
u3(0.14378759,0,0) q0[13];
cx q0[12],q0[13];
u3(-0.14378759,0,0) q0[13];
cx q0[12],q0[13];
rx(pi/2) q0[13];
r(1.121267,pi/2) q0[14];
rx(pi/2) q0[14];
cx q0[13],q0[14];
rz(0.9650285) q0[14];
cx q0[13],q0[14];
rx(-pi/2) q0[13];
rx(-pi/2) q0[14];
u3(0.15877809,0,0) q0[14];
cx q0[13],q0[14];
u3(-0.15877809,0,0) q0[14];
cx q0[13],q0[14];
rx(pi/2) q0[14];
r(0.71322165,pi/2) q0[15];
rx(pi/2) q0[15];
cx q0[14],q0[15];
rz(1.8244342) q0[15];
cx q0[14],q0[15];
rx(-pi/2) q0[14];
rx(-pi/2) q0[15];
u3(0.84721245,0,0) q0[15];
cx q0[14],q0[15];
u3(-0.84721245,0,0) q0[15];
cx q0[14],q0[15];
r(0.67673819,pi/2) q0[16];
rx(pi/2) q0[16];
r(1.3952151,pi/2) q0[17];
rx(pi/2) q0[17];
cx q0[16],q0[17];
rz(2.2214731) q0[17];
cx q0[16],q0[17];
rx(-pi/2) q0[16];
rx(-pi/2) q0[17];
u3(1.4239223,0,0) q0[17];
cx q0[16],q0[17];
u3(-1.4239223,0,0) q0[17];
cx q0[16],q0[17];
cx q0[16],q0[1];
ccx q0[0],q0[1],q0[16];
cx q0[16],q0[1];
rx(pi/2) q0[17];
r(2.2098165,pi/2) q0[18];
rx(pi/2) q0[18];
cx q0[17],q0[18];
rz(0.81255174) q0[18];
cx q0[17],q0[18];
rx(-pi/2) q0[17];
rx(-pi/2) q0[18];
u3(0.42437439,0,0) q0[18];
cx q0[17],q0[18];
u3(-0.42437439,0,0) q0[18];
cx q0[17],q0[18];
cx q0[17],q0[2];
ccx q0[0],q0[2],q0[17];
cx q0[17],q0[2];
rx(pi/2) q0[18];
r(0.66984289,pi/2) q0[19];
rx(pi/2) q0[19];
cx q0[18],q0[19];
rz(1.5930278) q0[19];
cx q0[18],q0[19];
rx(-pi/2) q0[18];
rx(-pi/2) q0[19];
u3(0.39638608,0,0) q0[19];
cx q0[18],q0[19];
u3(-0.39638608,0,0) q0[19];
cx q0[18],q0[19];
cx q0[18],q0[3];
ccx q0[0],q0[3],q0[18];
cx q0[18],q0[3];
rx(pi/2) q0[19];
r(2.4347651,pi/2) q0[20];
rx(pi/2) q0[20];
cx q0[19],q0[20];
rz(2.6889413) q0[20];
cx q0[19],q0[20];
rx(-pi/2) q0[19];
rx(-pi/2) q0[20];
u3(0.5119179,0,0) q0[20];
cx q0[19],q0[20];
u3(-0.5119179,0,0) q0[20];
cx q0[19],q0[20];
cx q0[19],q0[4];
ccx q0[0],q0[4],q0[19];
cx q0[19],q0[4];
rx(pi/2) q0[20];
r(0.79898228,pi/2) q0[21];
rx(pi/2) q0[21];
cx q0[20],q0[21];
rz(2.221667) q0[21];
cx q0[20],q0[21];
rx(-pi/2) q0[20];
rx(-pi/2) q0[21];
u3(0.69135081,0,0) q0[21];
cx q0[20],q0[21];
u3(-0.69135081,0,0) q0[21];
cx q0[20],q0[21];
cx q0[20],q0[5];
ccx q0[0],q0[5],q0[20];
cx q0[20],q0[5];
rx(pi/2) q0[21];
r(0.93105611,pi/2) q0[22];
rx(pi/2) q0[22];
cx q0[21],q0[22];
rz(2.2607776) q0[22];
cx q0[21],q0[22];
rx(-pi/2) q0[21];
rx(-pi/2) q0[22];
u3(0.67053226,0,0) q0[22];
cx q0[21],q0[22];
u3(-0.67053226,0,0) q0[22];
cx q0[21],q0[22];
cx q0[21],q0[6];
ccx q0[0],q0[6],q0[21];
cx q0[21],q0[6];
rx(pi/2) q0[22];
r(0.85392831,pi/2) q0[23];
rx(pi/2) q0[23];
cx q0[22],q0[23];
rz(0.70521178) q0[23];
cx q0[22],q0[23];
rx(-pi/2) q0[22];
rx(-pi/2) q0[23];
u3(1.2476792,0,0) q0[23];
cx q0[22],q0[23];
u3(-1.2476792,0,0) q0[23];
cx q0[22],q0[23];
cx q0[22],q0[7];
ccx q0[0],q0[7],q0[22];
cx q0[22],q0[7];
rx(pi/2) q0[23];
r(1.2899547,pi/2) q0[24];
rx(pi/2) q0[24];
cx q0[23],q0[24];
rz(0.44044227) q0[24];
cx q0[23],q0[24];
rx(-pi/2) q0[23];
rx(-pi/2) q0[24];
u3(0.57223555,0,0) q0[24];
cx q0[23],q0[24];
u3(-0.57223555,0,0) q0[24];
cx q0[23],q0[24];
cx q0[23],q0[8];
ccx q0[0],q0[8],q0[23];
cx q0[23],q0[8];
rx(pi/2) q0[24];
r(1.6782757,pi/2) q0[25];
rx(pi/2) q0[25];
cx q0[24],q0[25];
rz(2.4825481) q0[25];
cx q0[24],q0[25];
rx(-pi/2) q0[24];
rx(-pi/2) q0[25];
u3(0.087312936,0,0) q0[25];
cx q0[24],q0[25];
u3(-0.087312936,0,0) q0[25];
cx q0[24],q0[25];
cx q0[24],q0[9];
ccx q0[0],q0[9],q0[24];
cx q0[24],q0[9];
rx(pi/2) q0[25];
r(0.6229332,pi/2) q0[26];
rx(pi/2) q0[26];
cx q0[25],q0[26];
rz(0.022614947) q0[26];
cx q0[25],q0[26];
rx(-pi/2) q0[25];
rx(-pi/2) q0[26];
u3(1.1183785,0,0) q0[26];
cx q0[25],q0[26];
u3(-1.1183785,0,0) q0[26];
cx q0[25],q0[26];
cx q0[25],q0[10];
ccx q0[0],q0[10],q0[25];
cx q0[25],q0[10];
rx(pi/2) q0[26];
r(0.63266441,pi/2) q0[27];
rx(pi/2) q0[27];
cx q0[26],q0[27];
rz(2.2450724) q0[27];
cx q0[26],q0[27];
rx(-pi/2) q0[26];
rx(-pi/2) q0[27];
u3(1.3044612,0,0) q0[27];
cx q0[26],q0[27];
u3(-1.3044612,0,0) q0[27];
cx q0[26],q0[27];
cx q0[26],q0[11];
ccx q0[0],q0[11],q0[26];
cx q0[26],q0[11];
rx(pi/2) q0[27];
r(1.3029852,pi/2) q0[28];
rx(pi/2) q0[28];
cx q0[27],q0[28];
rz(3.0687889) q0[28];
cx q0[27],q0[28];
rx(-pi/2) q0[27];
rx(-pi/2) q0[28];
u3(0.3777522,0,0) q0[28];
cx q0[27],q0[28];
u3(-0.3777522,0,0) q0[28];
cx q0[27],q0[28];
cx q0[27],q0[12];
ccx q0[0],q0[12],q0[27];
cx q0[27],q0[12];
rx(pi/2) q0[28];
r(2.9103147,pi/2) q0[29];
rx(pi/2) q0[29];
cx q0[28],q0[29];
rz(1.039868) q0[29];
cx q0[28],q0[29];
rx(-pi/2) q0[28];
rx(-pi/2) q0[29];
u3(0.22709394,0,0) q0[29];
cx q0[28],q0[29];
u3(-0.22709394,0,0) q0[29];
cx q0[28],q0[29];
cx q0[28],q0[13];
ccx q0[0],q0[13],q0[28];
cx q0[28],q0[13];
rx(pi/2) q0[29];
r(1.6302397,pi/2) q0[30];
rx(pi/2) q0[30];
cx q0[29],q0[30];
rz(0.85073632) q0[30];
cx q0[29],q0[30];
rx(-pi/2) q0[29];
rx(-pi/2) q0[30];
u3(0.45886514,0,0) q0[30];
cx q0[29],q0[30];
u3(-0.45886514,0,0) q0[30];
cx q0[29],q0[30];
cx q0[29],q0[14];
ccx q0[0],q0[14],q0[29];
cx q0[29],q0[14];
cx q0[30],q0[15];
ccx q0[0],q0[15],q0[30];
u2(0,pi) q0[0];
cx q0[30],q0[15];
measure q0[16] -> c0[0];
measure q0[17] -> c0[1];
measure q0[18] -> c0[2];
measure q0[19] -> c0[3];
measure q0[20] -> c0[4];
measure q0[21] -> c0[5];
measure q0[22] -> c0[6];
measure q0[23] -> c0[7];
measure q0[24] -> c0[8];
measure q0[25] -> c0[9];
measure q0[26] -> c0[10];
measure q0[27] -> c0[11];
measure q0[28] -> c0[12];
measure q0[29] -> c0[13];
measure q0[30] -> c0[14];
