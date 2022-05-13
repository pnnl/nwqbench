namespace Quantum {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;

    function SetBitValue(reg: Int, bit: Int, value: Bool): Int {
        if(value) {
            return reg ||| (1 <<< bit);
        } else {
            return reg &&& ~~~(1 <<< bit);
        }
    }
    
    operation Circuit(): (Int) {
mutable c0 = 0;
using(qubits = Qubit[31]) {
u2(0.0, PI(), qubits[0]);
Rx(PI() / 2.0, qubits[1]);
Rx(PI() / 2.0, qubits[2]);
Rx(PI() / 2.0, qubits[3]);
Rx(PI() / 2.0, qubits[4]);
Rx(PI() / 2.0, qubits[5]);
Rx(PI() / 2.0, qubits[6]);
Rx(PI() / 2.0, qubits[7]);
Rx(PI() / 2.0, qubits[8]);
Rx(PI() / 2.0, qubits[9]);
Rx(PI() / 2.0, qubits[10]);
Rx(PI() / 2.0, qubits[11]);
Rx(PI() / 2.0, qubits[12]);
Rx(PI() / 2.0, qubits[13]);
Rx(PI() / 2.0, qubits[14]);
Rx(PI() / 2.0, qubits[15]);
Rx(PI() / 2.0, qubits[16]);
Rx(PI() / 2.0, qubits[17]);
Rx(PI() / 2.0, qubits[18]);
Rx(PI() / 2.0, qubits[19]);
Rx(PI() / 2.0, qubits[20]);
Rx(PI() / 2.0, qubits[21]);
Rx(PI() / 2.0, qubits[22]);
Rx(PI() / 2.0, qubits[23]);
Rx(PI() / 2.0, qubits[24]);
Rx(PI() / 2.0, qubits[25]);
Rx(PI() / 2.0, qubits[26]);
Rx(PI() / 2.0, qubits[27]);
Rx(PI() / 2.0, qubits[28]);
Rx(PI() / 2.0, qubits[29]);
Rx(PI() / 2.0, qubits[30]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[16], qubits[17]);
Rz(1.2977392, qubits[2]);
Rz(2.2214731, qubits[17]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[16], qubits[17]);
Rx(-PI() / 2.0, qubits[1]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[16]);
Rx(-PI() / 2.0, qubits[17]);
u3(1.4432896, 0.0, 0.0, qubits[2]);
u3(1.4239223, 0.0, 0.0, qubits[17]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[16], qubits[17]);
u3(-1.4432896, 0.0, 0.0, qubits[2]);
u3(-1.4239223, 0.0, 0.0, qubits[17]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[16], qubits[17]);
Rx(PI() / 2.0, qubits[2]);
Rx(PI() / 2.0, qubits[17]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[17], qubits[18]);
Rz(2.8649402, qubits[3]);
Rz(0.81255174, qubits[18]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[17], qubits[18]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[17]);
Rx(-PI() / 2.0, qubits[18]);
u3(0.60753935, 0.0, 0.0, qubits[3]);
u3(0.42437439, 0.0, 0.0, qubits[18]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[17], qubits[18]);
u3(-0.60753935, 0.0, 0.0, qubits[3]);
u3(-0.42437439, 0.0, 0.0, qubits[18]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[17], qubits[18]);
Rx(PI() / 2.0, qubits[3]);
Rx(PI() / 2.0, qubits[18]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[18], qubits[19]);
Rz(1.2287728, qubits[4]);
Rz(1.5930278, qubits[19]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[18], qubits[19]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[4]);
Rx(-PI() / 2.0, qubits[18]);
Rx(-PI() / 2.0, qubits[19]);
u3(0.89724501, 0.0, 0.0, qubits[4]);
u3(0.39638608, 0.0, 0.0, qubits[19]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[18], qubits[19]);
u3(-0.89724501, 0.0, 0.0, qubits[4]);
u3(-0.39638608, 0.0, 0.0, qubits[19]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[18], qubits[19]);
Rx(PI() / 2.0, qubits[4]);
Rx(PI() / 2.0, qubits[19]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[19], qubits[20]);
Rz(0.88703672, qubits[5]);
Rz(2.6889413, qubits[20]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[19], qubits[20]);
Rx(-PI() / 2.0, qubits[4]);
Rx(-PI() / 2.0, qubits[5]);
Rx(-PI() / 2.0, qubits[19]);
Rx(-PI() / 2.0, qubits[20]);
u3(0.56500464, 0.0, 0.0, qubits[5]);
u3(0.5119179, 0.0, 0.0, qubits[20]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[19], qubits[20]);
u3(-0.56500464, 0.0, 0.0, qubits[5]);
u3(-0.5119179, 0.0, 0.0, qubits[20]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[19], qubits[20]);
Rx(PI() / 2.0, qubits[5]);
Rx(PI() / 2.0, qubits[20]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[20], qubits[21]);
Rz(1.1945889, qubits[6]);
Rz(2.221667, qubits[21]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[20], qubits[21]);
Rx(-PI() / 2.0, qubits[5]);
Rx(-PI() / 2.0, qubits[6]);
Rx(-PI() / 2.0, qubits[20]);
Rx(-PI() / 2.0, qubits[21]);
u3(0.78663791, 0.0, 0.0, qubits[6]);
u3(0.69135081, 0.0, 0.0, qubits[21]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[20], qubits[21]);
u3(-0.78663791, 0.0, 0.0, qubits[6]);
u3(-0.69135081, 0.0, 0.0, qubits[21]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[20], qubits[21]);
Rx(PI() / 2.0, qubits[6]);
Rx(PI() / 2.0, qubits[21]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[21], qubits[22]);
Rz(0.98968875, qubits[7]);
Rz(2.2607776, qubits[22]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[21], qubits[22]);
Rx(-PI() / 2.0, qubits[6]);
Rx(-PI() / 2.0, qubits[7]);
Rx(-PI() / 2.0, qubits[21]);
Rx(-PI() / 2.0, qubits[22]);
u3(1.3825416, 0.0, 0.0, qubits[7]);
u3(0.67053226, 0.0, 0.0, qubits[22]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[21], qubits[22]);
u3(-1.3825416, 0.0, 0.0, qubits[7]);
u3(-0.67053226, 0.0, 0.0, qubits[22]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[21], qubits[22]);
Rx(PI() / 2.0, qubits[7]);
Rx(PI() / 2.0, qubits[22]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[22], qubits[23]);
Rz(2.8925702, qubits[8]);
Rz(0.70521178, qubits[23]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[22], qubits[23]);
Rx(-PI() / 2.0, qubits[7]);
Rx(-PI() / 2.0, qubits[8]);
Rx(-PI() / 2.0, qubits[22]);
Rx(-PI() / 2.0, qubits[23]);
u3(1.5320829, 0.0, 0.0, qubits[8]);
u3(1.2476792, 0.0, 0.0, qubits[23]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[22], qubits[23]);
u3(-1.5320829, 0.0, 0.0, qubits[8]);
u3(-1.2476792, 0.0, 0.0, qubits[23]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[22], qubits[23]);
Rx(PI() / 2.0, qubits[8]);
Rx(PI() / 2.0, qubits[23]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[23], qubits[24]);
Rz(2.6101061, qubits[9]);
Rz(0.44044227, qubits[24]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[23], qubits[24]);
Rx(-PI() / 2.0, qubits[8]);
Rx(-PI() / 2.0, qubits[9]);
Rx(-PI() / 2.0, qubits[23]);
Rx(-PI() / 2.0, qubits[24]);
u3(0.67987172, 0.0, 0.0, qubits[9]);
u3(0.57223555, 0.0, 0.0, qubits[24]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[23], qubits[24]);
u3(-0.67987172, 0.0, 0.0, qubits[9]);
u3(-0.57223555, 0.0, 0.0, qubits[24]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[23], qubits[24]);
Rx(PI() / 2.0, qubits[9]);
Rx(PI() / 2.0, qubits[24]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[24], qubits[25]);
Rz(0.67584848, qubits[10]);
Rz(2.4825481, qubits[25]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[24], qubits[25]);
Rx(-PI() / 2.0, qubits[9]);
Rx(-PI() / 2.0, qubits[10]);
Rx(-PI() / 2.0, qubits[24]);
Rx(-PI() / 2.0, qubits[25]);
u3(0.30508649, 0.0, 0.0, qubits[10]);
u3(0.087312936, 0.0, 0.0, qubits[25]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[24], qubits[25]);
u3(-0.30508649, 0.0, 0.0, qubits[10]);
u3(-0.087312936, 0.0, 0.0, qubits[25]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[24], qubits[25]);
Rx(PI() / 2.0, qubits[10]);
Rx(PI() / 2.0, qubits[25]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[25], qubits[26]);
Rz(2.8535391, qubits[11]);
Rz(0.022614947, qubits[26]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[25], qubits[26]);
Rx(-PI() / 2.0, qubits[10]);
Rx(-PI() / 2.0, qubits[11]);
Rx(-PI() / 2.0, qubits[25]);
Rx(-PI() / 2.0, qubits[26]);
u3(1.1107695, 0.0, 0.0, qubits[11]);
u3(1.1183785, 0.0, 0.0, qubits[26]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[25], qubits[26]);
u3(-1.1107695, 0.0, 0.0, qubits[11]);
u3(-1.1183785, 0.0, 0.0, qubits[26]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[25], qubits[26]);
Rx(PI() / 2.0, qubits[11]);
Rx(PI() / 2.0, qubits[26]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[26], qubits[27]);
Rz(0.70415312, qubits[12]);
Rz(2.2450724, qubits[27]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[26], qubits[27]);
Rx(-PI() / 2.0, qubits[11]);
Rx(-PI() / 2.0, qubits[12]);
Rx(-PI() / 2.0, qubits[26]);
Rx(-PI() / 2.0, qubits[27]);
u3(0.031031735, 0.0, 0.0, qubits[12]);
u3(1.3044612, 0.0, 0.0, qubits[27]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[26], qubits[27]);
u3(-0.031031735, 0.0, 0.0, qubits[12]);
u3(-1.3044612, 0.0, 0.0, qubits[27]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[26], qubits[27]);
Rx(PI() / 2.0, qubits[12]);
Rx(PI() / 2.0, qubits[27]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[27], qubits[28]);
Rz(0.60245421, qubits[13]);
Rz(3.0687889, qubits[28]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[27], qubits[28]);
Rx(-PI() / 2.0, qubits[12]);
Rx(-PI() / 2.0, qubits[13]);
Rx(-PI() / 2.0, qubits[27]);
Rx(-PI() / 2.0, qubits[28]);
u3(0.14378759, 0.0, 0.0, qubits[13]);
u3(0.3777522, 0.0, 0.0, qubits[28]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[27], qubits[28]);
u3(-0.14378759, 0.0, 0.0, qubits[13]);
u3(-0.3777522, 0.0, 0.0, qubits[28]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[27], qubits[28]);
Rx(PI() / 2.0, qubits[13]);
Rx(PI() / 2.0, qubits[28]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[28], qubits[29]);
Rz(0.9650285, qubits[14]);
Rz(1.039868, qubits[29]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[28], qubits[29]);
Rx(-PI() / 2.0, qubits[13]);
Rx(-PI() / 2.0, qubits[14]);
Rx(-PI() / 2.0, qubits[28]);
Rx(-PI() / 2.0, qubits[29]);
u3(0.15877809, 0.0, 0.0, qubits[14]);
u3(0.22709394, 0.0, 0.0, qubits[29]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[28], qubits[29]);
u3(-0.15877809, 0.0, 0.0, qubits[14]);
u3(-0.22709394, 0.0, 0.0, qubits[29]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[28], qubits[29]);
Rx(PI() / 2.0, qubits[14]);
Rx(PI() / 2.0, qubits[29]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[29], qubits[30]);
Rz(1.8244342, qubits[15]);
Rz(0.85073632, qubits[30]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[29], qubits[30]);
Rx(-PI() / 2.0, qubits[14]);
Rx(-PI() / 2.0, qubits[15]);
Rx(-PI() / 2.0, qubits[29]);
Rx(-PI() / 2.0, qubits[30]);
u3(0.84721245, 0.0, 0.0, qubits[15]);
u3(0.45886514, 0.0, 0.0, qubits[30]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[29], qubits[30]);
u3(-0.84721245, 0.0, 0.0, qubits[15]);
u3(-0.45886514, 0.0, 0.0, qubits[30]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[29], qubits[30]);
CNOT(qubits[16], qubits[1]);
CCNOT(qubits[0], qubits[1], qubits[16]);
CNOT(qubits[16], qubits[1]);
CNOT(qubits[17], qubits[2]);
CCNOT(qubits[0], qubits[2], qubits[17]);
CNOT(qubits[17], qubits[2]);
CNOT(qubits[18], qubits[3]);
CCNOT(qubits[0], qubits[3], qubits[18]);
CNOT(qubits[18], qubits[3]);
CNOT(qubits[19], qubits[4]);
CCNOT(qubits[0], qubits[4], qubits[19]);
CNOT(qubits[19], qubits[4]);
CNOT(qubits[20], qubits[5]);
CCNOT(qubits[0], qubits[5], qubits[20]);
CNOT(qubits[20], qubits[5]);
CNOT(qubits[21], qubits[6]);
CCNOT(qubits[0], qubits[6], qubits[21]);
CNOT(qubits[21], qubits[6]);
CNOT(qubits[22], qubits[7]);
CCNOT(qubits[0], qubits[7], qubits[22]);
CNOT(qubits[22], qubits[7]);
CNOT(qubits[23], qubits[8]);
CCNOT(qubits[0], qubits[8], qubits[23]);
CNOT(qubits[23], qubits[8]);
CNOT(qubits[24], qubits[9]);
CCNOT(qubits[0], qubits[9], qubits[24]);
CNOT(qubits[24], qubits[9]);
CNOT(qubits[25], qubits[10]);
CCNOT(qubits[0], qubits[10], qubits[25]);
CNOT(qubits[25], qubits[10]);
CNOT(qubits[26], qubits[11]);
CCNOT(qubits[0], qubits[11], qubits[26]);
CNOT(qubits[26], qubits[11]);
CNOT(qubits[27], qubits[12]);
CCNOT(qubits[0], qubits[12], qubits[27]);
CNOT(qubits[27], qubits[12]);
CNOT(qubits[28], qubits[13]);
CCNOT(qubits[0], qubits[13], qubits[28]);
CNOT(qubits[28], qubits[13]);
CNOT(qubits[29], qubits[14]);
CCNOT(qubits[0], qubits[14], qubits[29]);
CNOT(qubits[29], qubits[14]);
CNOT(qubits[30], qubits[15]);
CCNOT(qubits[0], qubits[15], qubits[30]);
u2(0.0, PI(), qubits[0]);
CNOT(qubits[30], qubits[15]);
set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[16])));
set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[17])));
set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[18])));
set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[19])));
set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[20])));
set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[21])));
set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[22])));
set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[23])));
set c0 = SetBitValue(c0, 8, ResultAsBool(M(qubits[24])));
set c0 = SetBitValue(c0, 9, ResultAsBool(M(qubits[25])));
set c0 = SetBitValue(c0, 10, ResultAsBool(M(qubits[26])));
set c0 = SetBitValue(c0, 11, ResultAsBool(M(qubits[27])));
set c0 = SetBitValue(c0, 12, ResultAsBool(M(qubits[28])));
set c0 = SetBitValue(c0, 13, ResultAsBool(M(qubits[29])));
set c0 = SetBitValue(c0, 14, ResultAsBool(M(qubits[30])));
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
        }
        return (c0);
    }
}
