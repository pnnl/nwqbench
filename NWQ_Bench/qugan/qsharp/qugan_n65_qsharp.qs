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
using(qubits = Qubit[65]) {
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
Rx(PI() / 2.0, qubits[31]);
Rx(PI() / 2.0, qubits[32]);
Rx(PI() / 2.0, qubits[33]);
Rx(PI() / 2.0, qubits[34]);
Rx(PI() / 2.0, qubits[35]);
Rx(PI() / 2.0, qubits[36]);
Rx(PI() / 2.0, qubits[37]);
Rx(PI() / 2.0, qubits[38]);
Rx(PI() / 2.0, qubits[39]);
Rx(PI() / 2.0, qubits[40]);
Rx(PI() / 2.0, qubits[41]);
Rx(PI() / 2.0, qubits[42]);
Rx(PI() / 2.0, qubits[43]);
Rx(PI() / 2.0, qubits[44]);
Rx(PI() / 2.0, qubits[45]);
Rx(PI() / 2.0, qubits[46]);
Rx(PI() / 2.0, qubits[47]);
Rx(PI() / 2.0, qubits[48]);
Rx(PI() / 2.0, qubits[49]);
Rx(PI() / 2.0, qubits[50]);
Rx(PI() / 2.0, qubits[51]);
Rx(PI() / 2.0, qubits[52]);
Rx(PI() / 2.0, qubits[53]);
Rx(PI() / 2.0, qubits[54]);
Rx(PI() / 2.0, qubits[55]);
Rx(PI() / 2.0, qubits[56]);
Rx(PI() / 2.0, qubits[57]);
Rx(PI() / 2.0, qubits[58]);
Rx(PI() / 2.0, qubits[59]);
Rx(PI() / 2.0, qubits[60]);
Rx(PI() / 2.0, qubits[61]);
Rx(PI() / 2.0, qubits[62]);
Rx(PI() / 2.0, qubits[63]);
Rx(PI() / 2.0, qubits[64]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[33], qubits[34]);
Rz(2.1326225, qubits[2]);
Rz(2.5992881, qubits[34]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[33], qubits[34]);
Rx(-PI() / 2.0, qubits[1]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[33]);
Rx(-PI() / 2.0, qubits[34]);
u3(0.1238051, 0.0, 0.0, qubits[2]);
u3(1.3204729, 0.0, 0.0, qubits[34]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[33], qubits[34]);
u3(-0.1238051, 0.0, 0.0, qubits[2]);
u3(-1.3204729, 0.0, 0.0, qubits[34]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[33], qubits[34]);
Rx(PI() / 2.0, qubits[2]);
Rx(PI() / 2.0, qubits[34]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[34], qubits[35]);
Rz(0.60955675, qubits[3]);
Rz(3.0840557, qubits[35]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[34], qubits[35]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[34]);
Rx(-PI() / 2.0, qubits[35]);
u3(0.073350091, 0.0, 0.0, qubits[3]);
u3(0.56985898, 0.0, 0.0, qubits[35]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[34], qubits[35]);
u3(-0.073350091, 0.0, 0.0, qubits[3]);
u3(-0.56985898, 0.0, 0.0, qubits[35]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[34], qubits[35]);
Rx(PI() / 2.0, qubits[3]);
Rx(PI() / 2.0, qubits[35]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[35], qubits[36]);
Rz(0.07095891, qubits[4]);
Rz(2.1600561, qubits[36]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[35], qubits[36]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[4]);
Rx(-PI() / 2.0, qubits[35]);
Rx(-PI() / 2.0, qubits[36]);
u3(1.070064, 0.0, 0.0, qubits[4]);
u3(0.64846351, 0.0, 0.0, qubits[36]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[35], qubits[36]);
u3(-1.070064, 0.0, 0.0, qubits[4]);
u3(-0.64846351, 0.0, 0.0, qubits[36]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[35], qubits[36]);
Rx(PI() / 2.0, qubits[4]);
Rx(PI() / 2.0, qubits[36]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[36], qubits[37]);
Rz(1.9285273, qubits[5]);
Rz(2.5527338, qubits[37]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[36], qubits[37]);
Rx(-PI() / 2.0, qubits[4]);
Rx(-PI() / 2.0, qubits[5]);
Rx(-PI() / 2.0, qubits[36]);
Rx(-PI() / 2.0, qubits[37]);
u3(1.3040954, 0.0, 0.0, qubits[5]);
u3(0.81334021, 0.0, 0.0, qubits[37]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[36], qubits[37]);
u3(-1.3040954, 0.0, 0.0, qubits[5]);
u3(-0.81334021, 0.0, 0.0, qubits[37]);
CNOT(qubits[4], qubits[5]);
CNOT(qubits[36], qubits[37]);
Rx(PI() / 2.0, qubits[5]);
Rx(PI() / 2.0, qubits[37]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[37], qubits[38]);
Rz(1.3094099, qubits[6]);
Rz(1.5159622, qubits[38]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[37], qubits[38]);
Rx(-PI() / 2.0, qubits[5]);
Rx(-PI() / 2.0, qubits[6]);
Rx(-PI() / 2.0, qubits[37]);
Rx(-PI() / 2.0, qubits[38]);
u3(1.4618621, 0.0, 0.0, qubits[6]);
u3(0.58187016, 0.0, 0.0, qubits[38]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[37], qubits[38]);
u3(-1.4618621, 0.0, 0.0, qubits[6]);
u3(-0.58187016, 0.0, 0.0, qubits[38]);
CNOT(qubits[5], qubits[6]);
CNOT(qubits[37], qubits[38]);
Rx(PI() / 2.0, qubits[6]);
Rx(PI() / 2.0, qubits[38]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[38], qubits[39]);
Rz(1.2025341, qubits[7]);
Rz(0.93954697, qubits[39]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[38], qubits[39]);
Rx(-PI() / 2.0, qubits[6]);
Rx(-PI() / 2.0, qubits[7]);
Rx(-PI() / 2.0, qubits[38]);
Rx(-PI() / 2.0, qubits[39]);
u3(1.5655627, 0.0, 0.0, qubits[7]);
u3(1.0287651, 0.0, 0.0, qubits[39]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[38], qubits[39]);
u3(-1.5655627, 0.0, 0.0, qubits[7]);
u3(-1.0287651, 0.0, 0.0, qubits[39]);
CNOT(qubits[6], qubits[7]);
CNOT(qubits[38], qubits[39]);
Rx(PI() / 2.0, qubits[7]);
Rx(PI() / 2.0, qubits[39]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[39], qubits[40]);
Rz(0.56055484, qubits[8]);
Rz(1.2783898, qubits[40]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[39], qubits[40]);
Rx(-PI() / 2.0, qubits[7]);
Rx(-PI() / 2.0, qubits[8]);
Rx(-PI() / 2.0, qubits[39]);
Rx(-PI() / 2.0, qubits[40]);
u3(0.2789862, 0.0, 0.0, qubits[8]);
u3(0.1967155, 0.0, 0.0, qubits[40]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[39], qubits[40]);
u3(-0.2789862, 0.0, 0.0, qubits[8]);
u3(-0.1967155, 0.0, 0.0, qubits[40]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[39], qubits[40]);
Rx(PI() / 2.0, qubits[8]);
Rx(PI() / 2.0, qubits[40]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[40], qubits[41]);
Rz(0.55424183, qubits[9]);
Rz(2.4964547, qubits[41]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[40], qubits[41]);
Rx(-PI() / 2.0, qubits[8]);
Rx(-PI() / 2.0, qubits[9]);
Rx(-PI() / 2.0, qubits[40]);
Rx(-PI() / 2.0, qubits[41]);
u3(1.3743, 0.0, 0.0, qubits[9]);
u3(1.1285759, 0.0, 0.0, qubits[41]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[40], qubits[41]);
u3(-1.3743, 0.0, 0.0, qubits[9]);
u3(-1.1285759, 0.0, 0.0, qubits[41]);
CNOT(qubits[8], qubits[9]);
CNOT(qubits[40], qubits[41]);
Rx(PI() / 2.0, qubits[9]);
Rx(PI() / 2.0, qubits[41]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[41], qubits[42]);
Rz(1.6434892, qubits[10]);
Rz(1.5511031, qubits[42]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[41], qubits[42]);
Rx(-PI() / 2.0, qubits[9]);
Rx(-PI() / 2.0, qubits[10]);
Rx(-PI() / 2.0, qubits[41]);
Rx(-PI() / 2.0, qubits[42]);
u3(1.2492124, 0.0, 0.0, qubits[10]);
u3(0.89482599, 0.0, 0.0, qubits[42]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[41], qubits[42]);
u3(-1.2492124, 0.0, 0.0, qubits[10]);
u3(-0.89482599, 0.0, 0.0, qubits[42]);
CNOT(qubits[9], qubits[10]);
CNOT(qubits[41], qubits[42]);
Rx(PI() / 2.0, qubits[10]);
Rx(PI() / 2.0, qubits[42]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[42], qubits[43]);
Rz(2.0672045, qubits[11]);
Rz(1.0795082, qubits[43]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[42], qubits[43]);
Rx(-PI() / 2.0, qubits[10]);
Rx(-PI() / 2.0, qubits[11]);
Rx(-PI() / 2.0, qubits[42]);
Rx(-PI() / 2.0, qubits[43]);
u3(0.34878789, 0.0, 0.0, qubits[11]);
u3(1.0050012, 0.0, 0.0, qubits[43]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[42], qubits[43]);
u3(-0.34878789, 0.0, 0.0, qubits[11]);
u3(-1.0050012, 0.0, 0.0, qubits[43]);
CNOT(qubits[10], qubits[11]);
CNOT(qubits[42], qubits[43]);
Rx(PI() / 2.0, qubits[11]);
Rx(PI() / 2.0, qubits[43]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[43], qubits[44]);
Rz(1.2355332, qubits[12]);
Rz(2.2331017, qubits[44]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[43], qubits[44]);
Rx(-PI() / 2.0, qubits[11]);
Rx(-PI() / 2.0, qubits[12]);
Rx(-PI() / 2.0, qubits[43]);
Rx(-PI() / 2.0, qubits[44]);
u3(1.2619787, 0.0, 0.0, qubits[12]);
u3(0.2325188, 0.0, 0.0, qubits[44]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[43], qubits[44]);
u3(-1.2619787, 0.0, 0.0, qubits[12]);
u3(-0.2325188, 0.0, 0.0, qubits[44]);
CNOT(qubits[11], qubits[12]);
CNOT(qubits[43], qubits[44]);
Rx(PI() / 2.0, qubits[12]);
Rx(PI() / 2.0, qubits[44]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[44], qubits[45]);
Rz(1.8357102, qubits[13]);
Rz(2.9179752, qubits[45]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[44], qubits[45]);
Rx(-PI() / 2.0, qubits[12]);
Rx(-PI() / 2.0, qubits[13]);
Rx(-PI() / 2.0, qubits[44]);
Rx(-PI() / 2.0, qubits[45]);
u3(1.0663474, 0.0, 0.0, qubits[13]);
u3(0.8736573, 0.0, 0.0, qubits[45]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[44], qubits[45]);
u3(-1.0663474, 0.0, 0.0, qubits[13]);
u3(-0.8736573, 0.0, 0.0, qubits[45]);
CNOT(qubits[12], qubits[13]);
CNOT(qubits[44], qubits[45]);
Rx(PI() / 2.0, qubits[13]);
Rx(PI() / 2.0, qubits[45]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[45], qubits[46]);
Rz(2.0101551, qubits[14]);
Rz(1.9797768, qubits[46]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[45], qubits[46]);
Rx(-PI() / 2.0, qubits[13]);
Rx(-PI() / 2.0, qubits[14]);
Rx(-PI() / 2.0, qubits[45]);
Rx(-PI() / 2.0, qubits[46]);
u3(0.02833167, 0.0, 0.0, qubits[14]);
u3(0.92648115, 0.0, 0.0, qubits[46]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[45], qubits[46]);
u3(-0.02833167, 0.0, 0.0, qubits[14]);
u3(-0.92648115, 0.0, 0.0, qubits[46]);
CNOT(qubits[13], qubits[14]);
CNOT(qubits[45], qubits[46]);
Rx(PI() / 2.0, qubits[14]);
Rx(PI() / 2.0, qubits[46]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[46], qubits[47]);
Rz(2.5928222, qubits[15]);
Rz(2.0603188, qubits[47]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[46], qubits[47]);
Rx(-PI() / 2.0, qubits[14]);
Rx(-PI() / 2.0, qubits[15]);
Rx(-PI() / 2.0, qubits[46]);
Rx(-PI() / 2.0, qubits[47]);
u3(1.3303132, 0.0, 0.0, qubits[15]);
u3(0.24767259, 0.0, 0.0, qubits[47]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[46], qubits[47]);
u3(-1.3303132, 0.0, 0.0, qubits[15]);
u3(-0.24767259, 0.0, 0.0, qubits[47]);
CNOT(qubits[14], qubits[15]);
CNOT(qubits[46], qubits[47]);
Rx(PI() / 2.0, qubits[15]);
Rx(PI() / 2.0, qubits[47]);
CNOT(qubits[15], qubits[16]);
CNOT(qubits[47], qubits[48]);
Rz(1.280053, qubits[16]);
Rz(2.3201302, qubits[48]);
CNOT(qubits[15], qubits[16]);
CNOT(qubits[47], qubits[48]);
Rx(-PI() / 2.0, qubits[15]);
Rx(-PI() / 2.0, qubits[16]);
Rx(-PI() / 2.0, qubits[47]);
Rx(-PI() / 2.0, qubits[48]);
u3(1.5226708, 0.0, 0.0, qubits[16]);
u3(0.26555996, 0.0, 0.0, qubits[48]);
CNOT(qubits[15], qubits[16]);
CNOT(qubits[47], qubits[48]);
u3(-1.5226708, 0.0, 0.0, qubits[16]);
u3(-0.26555996, 0.0, 0.0, qubits[48]);
CNOT(qubits[15], qubits[16]);
CNOT(qubits[47], qubits[48]);
Rx(PI() / 2.0, qubits[16]);
Rx(PI() / 2.0, qubits[48]);
CNOT(qubits[16], qubits[17]);
CNOT(qubits[48], qubits[49]);
Rz(2.3336259, qubits[17]);
Rz(2.2480372, qubits[49]);
CNOT(qubits[16], qubits[17]);
CNOT(qubits[48], qubits[49]);
Rx(-PI() / 2.0, qubits[16]);
Rx(-PI() / 2.0, qubits[17]);
Rx(-PI() / 2.0, qubits[48]);
Rx(-PI() / 2.0, qubits[49]);
u3(0.83796289, 0.0, 0.0, qubits[17]);
u3(1.3917255, 0.0, 0.0, qubits[49]);
CNOT(qubits[16], qubits[17]);
CNOT(qubits[48], qubits[49]);
u3(-0.83796289, 0.0, 0.0, qubits[17]);
u3(-1.3917255, 0.0, 0.0, qubits[49]);
CNOT(qubits[16], qubits[17]);
CNOT(qubits[48], qubits[49]);
Rx(PI() / 2.0, qubits[17]);
Rx(PI() / 2.0, qubits[49]);
CNOT(qubits[17], qubits[18]);
CNOT(qubits[49], qubits[50]);
Rz(1.5555978, qubits[18]);
Rz(0.36410389, qubits[50]);
CNOT(qubits[17], qubits[18]);
CNOT(qubits[49], qubits[50]);
Rx(-PI() / 2.0, qubits[17]);
Rx(-PI() / 2.0, qubits[18]);
Rx(-PI() / 2.0, qubits[49]);
Rx(-PI() / 2.0, qubits[50]);
u3(1.5067029, 0.0, 0.0, qubits[18]);
u3(1.4631176, 0.0, 0.0, qubits[50]);
CNOT(qubits[17], qubits[18]);
CNOT(qubits[49], qubits[50]);
u3(-1.5067029, 0.0, 0.0, qubits[18]);
u3(-1.4631176, 0.0, 0.0, qubits[50]);
CNOT(qubits[17], qubits[18]);
CNOT(qubits[49], qubits[50]);
Rx(PI() / 2.0, qubits[18]);
Rx(PI() / 2.0, qubits[50]);
CNOT(qubits[18], qubits[19]);
CNOT(qubits[50], qubits[51]);
Rz(2.0293988, qubits[19]);
Rz(2.9267501, qubits[51]);
CNOT(qubits[18], qubits[19]);
CNOT(qubits[50], qubits[51]);
Rx(-PI() / 2.0, qubits[18]);
Rx(-PI() / 2.0, qubits[19]);
Rx(-PI() / 2.0, qubits[50]);
Rx(-PI() / 2.0, qubits[51]);
u3(1.1411507, 0.0, 0.0, qubits[19]);
u3(0.46225096, 0.0, 0.0, qubits[51]);
CNOT(qubits[18], qubits[19]);
CNOT(qubits[50], qubits[51]);
u3(-1.1411507, 0.0, 0.0, qubits[19]);
u3(-0.46225096, 0.0, 0.0, qubits[51]);
CNOT(qubits[18], qubits[19]);
CNOT(qubits[50], qubits[51]);
Rx(PI() / 2.0, qubits[19]);
Rx(PI() / 2.0, qubits[51]);
CNOT(qubits[19], qubits[20]);
CNOT(qubits[51], qubits[52]);
Rz(3.0228648, qubits[20]);
Rz(2.2840095, qubits[52]);
CNOT(qubits[19], qubits[20]);
CNOT(qubits[51], qubits[52]);
Rx(-PI() / 2.0, qubits[19]);
Rx(-PI() / 2.0, qubits[20]);
Rx(-PI() / 2.0, qubits[51]);
Rx(-PI() / 2.0, qubits[52]);
u3(1.5538562, 0.0, 0.0, qubits[20]);
u3(1.4028767, 0.0, 0.0, qubits[52]);
CNOT(qubits[19], qubits[20]);
CNOT(qubits[51], qubits[52]);
u3(-1.5538562, 0.0, 0.0, qubits[20]);
u3(-1.4028767, 0.0, 0.0, qubits[52]);
CNOT(qubits[19], qubits[20]);
CNOT(qubits[51], qubits[52]);
Rx(PI() / 2.0, qubits[20]);
Rx(PI() / 2.0, qubits[52]);
CNOT(qubits[20], qubits[21]);
CNOT(qubits[52], qubits[53]);
Rz(2.8828939, qubits[21]);
Rz(0.12864404, qubits[53]);
CNOT(qubits[20], qubits[21]);
CNOT(qubits[52], qubits[53]);
Rx(-PI() / 2.0, qubits[20]);
Rx(-PI() / 2.0, qubits[21]);
Rx(-PI() / 2.0, qubits[52]);
Rx(-PI() / 2.0, qubits[53]);
u3(0.42818033, 0.0, 0.0, qubits[21]);
u3(1.2328002, 0.0, 0.0, qubits[53]);
CNOT(qubits[20], qubits[21]);
CNOT(qubits[52], qubits[53]);
u3(-0.42818033, 0.0, 0.0, qubits[21]);
u3(-1.2328002, 0.0, 0.0, qubits[53]);
CNOT(qubits[20], qubits[21]);
CNOT(qubits[52], qubits[53]);
Rx(PI() / 2.0, qubits[21]);
Rx(PI() / 2.0, qubits[53]);
CNOT(qubits[21], qubits[22]);
CNOT(qubits[53], qubits[54]);
Rz(1.6567731, qubits[22]);
Rz(0.28632795, qubits[54]);
CNOT(qubits[21], qubits[22]);
CNOT(qubits[53], qubits[54]);
Rx(-PI() / 2.0, qubits[21]);
Rx(-PI() / 2.0, qubits[22]);
Rx(-PI() / 2.0, qubits[53]);
Rx(-PI() / 2.0, qubits[54]);
u3(0.8630194, 0.0, 0.0, qubits[22]);
u3(0.61298445, 0.0, 0.0, qubits[54]);
CNOT(qubits[21], qubits[22]);
CNOT(qubits[53], qubits[54]);
u3(-0.8630194, 0.0, 0.0, qubits[22]);
u3(-0.61298445, 0.0, 0.0, qubits[54]);
CNOT(qubits[21], qubits[22]);
CNOT(qubits[53], qubits[54]);
Rx(PI() / 2.0, qubits[22]);
Rx(PI() / 2.0, qubits[54]);
CNOT(qubits[22], qubits[23]);
CNOT(qubits[54], qubits[55]);
Rz(1.2531216, qubits[23]);
Rz(1.5912115, qubits[55]);
CNOT(qubits[22], qubits[23]);
CNOT(qubits[54], qubits[55]);
Rx(-PI() / 2.0, qubits[22]);
Rx(-PI() / 2.0, qubits[23]);
Rx(-PI() / 2.0, qubits[54]);
Rx(-PI() / 2.0, qubits[55]);
u3(0.20983154, 0.0, 0.0, qubits[23]);
u3(0.72834728, 0.0, 0.0, qubits[55]);
CNOT(qubits[22], qubits[23]);
CNOT(qubits[54], qubits[55]);
u3(-0.20983154, 0.0, 0.0, qubits[23]);
u3(-0.72834728, 0.0, 0.0, qubits[55]);
CNOT(qubits[22], qubits[23]);
CNOT(qubits[54], qubits[55]);
Rx(PI() / 2.0, qubits[23]);
Rx(PI() / 2.0, qubits[55]);
CNOT(qubits[23], qubits[24]);
CNOT(qubits[55], qubits[56]);
Rz(0.44813225, qubits[24]);
Rz(3.0019755, qubits[56]);
CNOT(qubits[23], qubits[24]);
CNOT(qubits[55], qubits[56]);
Rx(-PI() / 2.0, qubits[23]);
Rx(-PI() / 2.0, qubits[24]);
Rx(-PI() / 2.0, qubits[55]);
Rx(-PI() / 2.0, qubits[56]);
u3(0.18094276, 0.0, 0.0, qubits[24]);
u3(0.68235224, 0.0, 0.0, qubits[56]);
CNOT(qubits[23], qubits[24]);
CNOT(qubits[55], qubits[56]);
u3(-0.18094276, 0.0, 0.0, qubits[24]);
u3(-0.68235224, 0.0, 0.0, qubits[56]);
CNOT(qubits[23], qubits[24]);
CNOT(qubits[55], qubits[56]);
Rx(PI() / 2.0, qubits[24]);
Rx(PI() / 2.0, qubits[56]);
CNOT(qubits[24], qubits[25]);
CNOT(qubits[56], qubits[57]);
Rz(0.082978172, qubits[25]);
Rz(3.1057103, qubits[57]);
CNOT(qubits[24], qubits[25]);
CNOT(qubits[56], qubits[57]);
Rx(-PI() / 2.0, qubits[24]);
Rx(-PI() / 2.0, qubits[25]);
Rx(-PI() / 2.0, qubits[56]);
Rx(-PI() / 2.0, qubits[57]);
u3(0.28335569, 0.0, 0.0, qubits[25]);
u3(0.40333772, 0.0, 0.0, qubits[57]);
CNOT(qubits[24], qubits[25]);
CNOT(qubits[56], qubits[57]);
u3(-0.28335569, 0.0, 0.0, qubits[25]);
u3(-0.40333772, 0.0, 0.0, qubits[57]);
CNOT(qubits[24], qubits[25]);
CNOT(qubits[56], qubits[57]);
Rx(PI() / 2.0, qubits[25]);
Rx(PI() / 2.0, qubits[57]);
CNOT(qubits[25], qubits[26]);
CNOT(qubits[57], qubits[58]);
Rz(0.334982, qubits[26]);
Rz(0.89718806, qubits[58]);
CNOT(qubits[25], qubits[26]);
CNOT(qubits[57], qubits[58]);
Rx(-PI() / 2.0, qubits[25]);
Rx(-PI() / 2.0, qubits[26]);
Rx(-PI() / 2.0, qubits[57]);
Rx(-PI() / 2.0, qubits[58]);
u3(1.3337842, 0.0, 0.0, qubits[26]);
u3(0.91118801, 0.0, 0.0, qubits[58]);
CNOT(qubits[25], qubits[26]);
CNOT(qubits[57], qubits[58]);
u3(-1.3337842, 0.0, 0.0, qubits[26]);
u3(-0.91118801, 0.0, 0.0, qubits[58]);
CNOT(qubits[25], qubits[26]);
CNOT(qubits[57], qubits[58]);
Rx(PI() / 2.0, qubits[26]);
Rx(PI() / 2.0, qubits[58]);
CNOT(qubits[26], qubits[27]);
CNOT(qubits[58], qubits[59]);
Rz(2.7250419, qubits[27]);
Rz(2.3662803, qubits[59]);
CNOT(qubits[26], qubits[27]);
CNOT(qubits[58], qubits[59]);
Rx(-PI() / 2.0, qubits[26]);
Rx(-PI() / 2.0, qubits[27]);
Rx(-PI() / 2.0, qubits[58]);
Rx(-PI() / 2.0, qubits[59]);
u3(0.90962314, 0.0, 0.0, qubits[27]);
u3(0.28325665, 0.0, 0.0, qubits[59]);
CNOT(qubits[26], qubits[27]);
CNOT(qubits[58], qubits[59]);
u3(-0.90962314, 0.0, 0.0, qubits[27]);
u3(-0.28325665, 0.0, 0.0, qubits[59]);
CNOT(qubits[26], qubits[27]);
CNOT(qubits[58], qubits[59]);
Rx(PI() / 2.0, qubits[27]);
Rx(PI() / 2.0, qubits[59]);
CNOT(qubits[27], qubits[28]);
CNOT(qubits[59], qubits[60]);
Rz(0.3558715, qubits[28]);
Rz(0.90177392, qubits[60]);
CNOT(qubits[27], qubits[28]);
CNOT(qubits[59], qubits[60]);
Rx(-PI() / 2.0, qubits[27]);
Rx(-PI() / 2.0, qubits[28]);
Rx(-PI() / 2.0, qubits[59]);
Rx(-PI() / 2.0, qubits[60]);
u3(0.71850312, 0.0, 0.0, qubits[28]);
u3(0.69136665, 0.0, 0.0, qubits[60]);
CNOT(qubits[27], qubits[28]);
CNOT(qubits[59], qubits[60]);
u3(-0.71850312, 0.0, 0.0, qubits[28]);
u3(-0.69136665, 0.0, 0.0, qubits[60]);
CNOT(qubits[27], qubits[28]);
CNOT(qubits[59], qubits[60]);
Rx(PI() / 2.0, qubits[28]);
Rx(PI() / 2.0, qubits[60]);
CNOT(qubits[28], qubits[29]);
CNOT(qubits[60], qubits[61]);
Rz(0.31873261, qubits[29]);
Rz(0.14310722, qubits[61]);
CNOT(qubits[28], qubits[29]);
CNOT(qubits[60], qubits[61]);
Rx(-PI() / 2.0, qubits[28]);
Rx(-PI() / 2.0, qubits[29]);
Rx(-PI() / 2.0, qubits[60]);
Rx(-PI() / 2.0, qubits[61]);
u3(1.4297983, 0.0, 0.0, qubits[29]);
u3(1.1465328, 0.0, 0.0, qubits[61]);
CNOT(qubits[28], qubits[29]);
CNOT(qubits[60], qubits[61]);
u3(-1.4297983, 0.0, 0.0, qubits[29]);
u3(-1.1465328, 0.0, 0.0, qubits[61]);
CNOT(qubits[28], qubits[29]);
CNOT(qubits[60], qubits[61]);
Rx(PI() / 2.0, qubits[29]);
Rx(PI() / 2.0, qubits[61]);
CNOT(qubits[29], qubits[30]);
CNOT(qubits[61], qubits[62]);
Rz(0.35919566, qubits[30]);
Rz(3.0513977, qubits[62]);
CNOT(qubits[29], qubits[30]);
CNOT(qubits[61], qubits[62]);
Rx(-PI() / 2.0, qubits[29]);
Rx(-PI() / 2.0, qubits[30]);
Rx(-PI() / 2.0, qubits[61]);
Rx(-PI() / 2.0, qubits[62]);
u3(1.2279201, 0.0, 0.0, qubits[30]);
u3(0.40787137, 0.0, 0.0, qubits[62]);
CNOT(qubits[29], qubits[30]);
CNOT(qubits[61], qubits[62]);
u3(-1.2279201, 0.0, 0.0, qubits[30]);
u3(-0.40787137, 0.0, 0.0, qubits[62]);
CNOT(qubits[29], qubits[30]);
CNOT(qubits[61], qubits[62]);
Rx(PI() / 2.0, qubits[30]);
Rx(PI() / 2.0, qubits[62]);
CNOT(qubits[30], qubits[31]);
CNOT(qubits[62], qubits[63]);
Rz(0.44237778, qubits[31]);
Rz(1.4919719, qubits[63]);
CNOT(qubits[30], qubits[31]);
CNOT(qubits[62], qubits[63]);
Rx(-PI() / 2.0, qubits[30]);
Rx(-PI() / 2.0, qubits[31]);
Rx(-PI() / 2.0, qubits[62]);
Rx(-PI() / 2.0, qubits[63]);
u3(1.5152635, 0.0, 0.0, qubits[31]);
u3(1.0966814, 0.0, 0.0, qubits[63]);
CNOT(qubits[30], qubits[31]);
CNOT(qubits[62], qubits[63]);
u3(-1.5152635, 0.0, 0.0, qubits[31]);
u3(-1.0966814, 0.0, 0.0, qubits[63]);
CNOT(qubits[30], qubits[31]);
CNOT(qubits[62], qubits[63]);
Rx(PI() / 2.0, qubits[31]);
Rx(PI() / 2.0, qubits[63]);
CNOT(qubits[31], qubits[32]);
CNOT(qubits[63], qubits[64]);
Rz(2.9660002, qubits[32]);
Rz(0.90310564, qubits[64]);
CNOT(qubits[31], qubits[32]);
CNOT(qubits[63], qubits[64]);
Rx(-PI() / 2.0, qubits[31]);
Rx(-PI() / 2.0, qubits[32]);
Rx(-PI() / 2.0, qubits[63]);
Rx(-PI() / 2.0, qubits[64]);
u3(0.8690639, 0.0, 0.0, qubits[32]);
u3(1.3558226, 0.0, 0.0, qubits[64]);
CNOT(qubits[31], qubits[32]);
CNOT(qubits[63], qubits[64]);
u3(-0.8690639, 0.0, 0.0, qubits[32]);
u3(-1.3558226, 0.0, 0.0, qubits[64]);
CNOT(qubits[31], qubits[32]);
CNOT(qubits[63], qubits[64]);
CNOT(qubits[33], qubits[1]);
CCNOT(qubits[0], qubits[1], qubits[33]);
CNOT(qubits[33], qubits[1]);
CNOT(qubits[34], qubits[2]);
CCNOT(qubits[0], qubits[2], qubits[34]);
CNOT(qubits[34], qubits[2]);
CNOT(qubits[35], qubits[3]);
CCNOT(qubits[0], qubits[3], qubits[35]);
CNOT(qubits[35], qubits[3]);
CNOT(qubits[36], qubits[4]);
CCNOT(qubits[0], qubits[4], qubits[36]);
CNOT(qubits[36], qubits[4]);
CNOT(qubits[37], qubits[5]);
CCNOT(qubits[0], qubits[5], qubits[37]);
CNOT(qubits[37], qubits[5]);
CNOT(qubits[38], qubits[6]);
CCNOT(qubits[0], qubits[6], qubits[38]);
CNOT(qubits[38], qubits[6]);
CNOT(qubits[39], qubits[7]);
CCNOT(qubits[0], qubits[7], qubits[39]);
CNOT(qubits[39], qubits[7]);
CNOT(qubits[40], qubits[8]);
CCNOT(qubits[0], qubits[8], qubits[40]);
CNOT(qubits[40], qubits[8]);
CNOT(qubits[41], qubits[9]);
CCNOT(qubits[0], qubits[9], qubits[41]);
CNOT(qubits[41], qubits[9]);
CNOT(qubits[42], qubits[10]);
CCNOT(qubits[0], qubits[10], qubits[42]);
CNOT(qubits[42], qubits[10]);
CNOT(qubits[43], qubits[11]);
CCNOT(qubits[0], qubits[11], qubits[43]);
CNOT(qubits[43], qubits[11]);
CNOT(qubits[44], qubits[12]);
CCNOT(qubits[0], qubits[12], qubits[44]);
CNOT(qubits[44], qubits[12]);
CNOT(qubits[45], qubits[13]);
CCNOT(qubits[0], qubits[13], qubits[45]);
CNOT(qubits[45], qubits[13]);
CNOT(qubits[46], qubits[14]);
CCNOT(qubits[0], qubits[14], qubits[46]);
CNOT(qubits[46], qubits[14]);
CNOT(qubits[47], qubits[15]);
CCNOT(qubits[0], qubits[15], qubits[47]);
CNOT(qubits[47], qubits[15]);
CNOT(qubits[48], qubits[16]);
CCNOT(qubits[0], qubits[16], qubits[48]);
CNOT(qubits[48], qubits[16]);
CNOT(qubits[49], qubits[17]);
CCNOT(qubits[0], qubits[17], qubits[49]);
CNOT(qubits[49], qubits[17]);
CNOT(qubits[50], qubits[18]);
CCNOT(qubits[0], qubits[18], qubits[50]);
CNOT(qubits[50], qubits[18]);
CNOT(qubits[51], qubits[19]);
CCNOT(qubits[0], qubits[19], qubits[51]);
CNOT(qubits[51], qubits[19]);
CNOT(qubits[52], qubits[20]);
CCNOT(qubits[0], qubits[20], qubits[52]);
CNOT(qubits[52], qubits[20]);
CNOT(qubits[53], qubits[21]);
CCNOT(qubits[0], qubits[21], qubits[53]);
CNOT(qubits[53], qubits[21]);
CNOT(qubits[54], qubits[22]);
CCNOT(qubits[0], qubits[22], qubits[54]);
CNOT(qubits[54], qubits[22]);
CNOT(qubits[55], qubits[23]);
CCNOT(qubits[0], qubits[23], qubits[55]);
CNOT(qubits[55], qubits[23]);
CNOT(qubits[56], qubits[24]);
CCNOT(qubits[0], qubits[24], qubits[56]);
CNOT(qubits[56], qubits[24]);
CNOT(qubits[57], qubits[25]);
CCNOT(qubits[0], qubits[25], qubits[57]);
CNOT(qubits[57], qubits[25]);
CNOT(qubits[58], qubits[26]);
CCNOT(qubits[0], qubits[26], qubits[58]);
CNOT(qubits[58], qubits[26]);
CNOT(qubits[59], qubits[27]);
CCNOT(qubits[0], qubits[27], qubits[59]);
CNOT(qubits[59], qubits[27]);
CNOT(qubits[60], qubits[28]);
CCNOT(qubits[0], qubits[28], qubits[60]);
CNOT(qubits[60], qubits[28]);
CNOT(qubits[61], qubits[29]);
CCNOT(qubits[0], qubits[29], qubits[61]);
CNOT(qubits[61], qubits[29]);
CNOT(qubits[62], qubits[30]);
CCNOT(qubits[0], qubits[30], qubits[62]);
CNOT(qubits[62], qubits[30]);
CNOT(qubits[63], qubits[31]);
CCNOT(qubits[0], qubits[31], qubits[63]);
CNOT(qubits[63], qubits[31]);
CNOT(qubits[64], qubits[32]);
CCNOT(qubits[0], qubits[32], qubits[64]);
u2(0.0, PI(), qubits[0]);
CNOT(qubits[64], qubits[32]);
set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[33])));
set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[34])));
set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[35])));
set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[36])));
set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[37])));
set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[38])));
set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[39])));
set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[40])));
set c0 = SetBitValue(c0, 8, ResultAsBool(M(qubits[41])));
set c0 = SetBitValue(c0, 9, ResultAsBool(M(qubits[42])));
set c0 = SetBitValue(c0, 10, ResultAsBool(M(qubits[43])));
set c0 = SetBitValue(c0, 11, ResultAsBool(M(qubits[44])));
set c0 = SetBitValue(c0, 12, ResultAsBool(M(qubits[45])));
set c0 = SetBitValue(c0, 13, ResultAsBool(M(qubits[46])));
set c0 = SetBitValue(c0, 14, ResultAsBool(M(qubits[47])));
set c0 = SetBitValue(c0, 15, ResultAsBool(M(qubits[48])));
set c0 = SetBitValue(c0, 16, ResultAsBool(M(qubits[49])));
set c0 = SetBitValue(c0, 17, ResultAsBool(M(qubits[50])));
set c0 = SetBitValue(c0, 18, ResultAsBool(M(qubits[51])));
set c0 = SetBitValue(c0, 19, ResultAsBool(M(qubits[52])));
set c0 = SetBitValue(c0, 20, ResultAsBool(M(qubits[53])));
set c0 = SetBitValue(c0, 21, ResultAsBool(M(qubits[54])));
set c0 = SetBitValue(c0, 22, ResultAsBool(M(qubits[55])));
set c0 = SetBitValue(c0, 23, ResultAsBool(M(qubits[56])));
set c0 = SetBitValue(c0, 24, ResultAsBool(M(qubits[57])));
set c0 = SetBitValue(c0, 25, ResultAsBool(M(qubits[58])));
set c0 = SetBitValue(c0, 26, ResultAsBool(M(qubits[59])));
set c0 = SetBitValue(c0, 27, ResultAsBool(M(qubits[60])));
set c0 = SetBitValue(c0, 28, ResultAsBool(M(qubits[61])));
set c0 = SetBitValue(c0, 29, ResultAsBool(M(qubits[62])));
set c0 = SetBitValue(c0, 30, ResultAsBool(M(qubits[63])));
set c0 = SetBitValue(c0, 31, ResultAsBool(M(qubits[64])));
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
