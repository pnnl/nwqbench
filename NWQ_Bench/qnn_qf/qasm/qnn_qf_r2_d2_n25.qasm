OPENQASM 2.0;
include "qelib1.inc";
qreg q[25];
creg c[2];
ry(2.4046372) q[0];
ry(2.3336143) q[1];
ry(0.72133708) q[2];
ry(1.2300238) q[3];
ry(0.10197243) q[4];
ry(0.69592388) q[5];
ry(1.3613843) q[6];
ry(0.5556097) q[7];
ry(1.4779006) q[8];
ry(0.50657227) q[9];
ry(2.9520682) q[10];
ry(1.3080473) q[11];
ry(2.8924044) q[12];
ry(2.4984378) q[13];
ry(2.9348787) q[14];
ry(3.0971339) q[15];
ry(2.921169) q[16];
ry(1.1886529) q[17];
ry(2.6757282) q[18];
ry(2.338456) q[19];
ry(2.0531018) q[20];
ry(2.9369249) q[21];
ry(1.6146981) q[22];
cry(1.1414484) q[0],q[1];
cry(1.3104948) q[1],q[2];
cry(2.9488226) q[2],q[3];
cry(2.3282812) q[3],q[4];
cry(1.8701555) q[4],q[5];
cry(0.16767714) q[5],q[6];
cry(1.2373367) q[6],q[7];
cry(2.674611) q[7],q[8];
cry(1.5038571) q[8],q[9];
cry(1.8698485) q[9],q[10];
cry(0.294313) q[10],q[11];
cry(0.8994402) q[11],q[12];
cry(1.752392) q[12],q[13];
cry(1.7175125) q[13],q[14];
cry(0.37698405) q[14],q[15];
cry(0.96841912) q[15],q[16];
cry(3.0982528) q[16],q[17];
cry(1.2282107) q[17],q[18];
cry(0.80083453) q[18],q[19];
cry(2.3188841) q[19],q[20];
cry(2.5995155) q[20],q[21];
cry(0.93857984) q[21],q[22];
cry(0.63822073) q[22],q[0];
ry(1.9413184) q[0];
ry(1.2085058) q[1];
ry(0.7701523) q[2];
ry(3.0569623) q[3];
ry(2.4862034) q[4];
ry(1.3241212) q[5];
ry(0.52798856) q[6];
ry(2.5582703) q[7];
ry(1.0876095) q[8];
ry(0.2310176) q[9];
ry(1.0148172) q[10];
ry(1.7166428) q[11];
ry(1.0521398) q[12];
ry(2.239007) q[13];
ry(0.64819717) q[14];
ry(2.0142363) q[15];
ry(2.9262324) q[16];
ry(0.0054313038) q[17];
ry(1.7623353) q[18];
ry(0.87994577) q[19];
ry(0.78226646) q[20];
ry(2.0612786) q[21];
ry(0.84047059) q[22];
cry(1.34973) q[0],q[1];
cry(0.97470663) q[1],q[2];
cry(0.025435813) q[2],q[3];
cry(2.9278685) q[3],q[4];
cry(2.3737549) q[4],q[5];
cry(2.8485333) q[5],q[6];
cry(2.1689026) q[6],q[7];
cry(2.2029461) q[7],q[8];
cry(1.0586872) q[8],q[9];
cry(1.6016692) q[9],q[10];
cry(2.5923506) q[10],q[11];
cry(2.358091) q[11],q[12];
cry(1.0014829) q[12],q[13];
cry(2.679315) q[13],q[14];
cry(1.782026) q[14],q[15];
cry(1.0299718) q[15],q[16];
cry(3.0017512) q[16],q[17];
cry(0.11425213) q[17],q[18];
cry(1.0524761) q[18],q[19];
cry(2.9116021) q[19],q[20];
cry(2.0787959) q[20],q[21];
cry(0.38858815) q[21],q[22];
cry(1.2246489) q[22],q[0];
ry(0.062132702) q[0];
ry(2.0324349) q[1];
ry(0.2411408) q[2];
ry(0.3218655) q[3];
ry(2.3034366) q[4];
ry(2.1618027) q[5];
ry(2.4662505) q[6];
ry(0.10813863) q[7];
ry(0.78527373) q[8];
ry(1.1999737) q[9];
ry(1.537061) q[10];
ry(0.3983319) q[11];
ry(1.9941611) q[12];
ry(0.51317647) q[13];
ry(0.10166123) q[14];
ry(1.8670245) q[15];
ry(0.0072601447) q[16];
ry(2.7808594) q[17];
ry(1.7465951) q[18];
ry(0.15020818) q[19];
ry(0.17539502) q[20];
ry(0.1654123) q[21];
ry(0.035401541) q[22];
cry(2.243115) q[0],q[23];
cry(1.7246459) q[1],q[23];
cry(2.3173242) q[2],q[23];
cry(1.7832024) q[3],q[23];
cry(1.4016966) q[4],q[23];
cry(0.55701435) q[5],q[23];
cry(1.1949274) q[6],q[23];
cry(0.92853556) q[7],q[23];
cry(2.0343624) q[8],q[23];
cry(2.1080536) q[9],q[23];
cry(1.434495) q[10],q[23];
cry(2.2557125) q[11],q[23];
cry(2.8785988) q[12],q[23];
cry(0.12036396) q[13],q[23];
cry(0.21366093) q[14],q[23];
cry(2.5115313) q[15],q[23];
cry(0.61849089) q[16],q[23];
cry(1.1318183) q[17],q[23];
cry(1.1052579) q[18],q[23];
cry(2.83834) q[19],q[23];
cry(1.1548658) q[20],q[23];
cry(1.4192155) q[21],q[23];
cry(2.4928367) q[22],q[23];
cry(1.1986511) q[0],q[24];
cry(2.244777) q[1],q[24];
cry(1.5451018) q[2],q[24];
cry(2.5612201) q[3],q[24];
cry(0.58222979) q[4],q[24];
cry(2.7587097) q[5],q[24];
cry(2.3223639) q[6],q[24];
cry(1.7464534) q[7],q[24];
cry(1.0925269) q[8],q[24];
cry(1.4426669) q[9],q[24];
cry(0.26513699) q[10],q[24];
cry(0.8721534) q[11],q[24];
cry(2.7416068) q[12],q[24];
cry(2.4328144) q[13],q[24];
cry(1.3445639) q[14],q[24];
cry(1.9438733) q[15],q[24];
cry(2.5758755) q[16],q[24];
cry(0.5227285) q[17],q[24];
cry(1.09593) q[18],q[24];
cry(1.4953231) q[19],q[24];
cry(0.85781967) q[20],q[24];
cry(0.039022339) q[21],q[24];
cry(0.11357496) q[22],q[24];
measure q[23] -> c[0];
measure q[24] -> c[1];
