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
    
    operation Circuit() : (Int) {
        mutable c0 = 0;
        using(qubits = Qubit[65]) {
            H(qubits[0]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[3]);
            CNOT(qubits[1], qubits[3]);
            CNOT(qubits[1], qubits[4]);
            CNOT(qubits[1], qubits[4]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[3])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[4])));
            H(qubits[5]);
            CNOT(qubits[5], qubits[6]);
            CNOT(qubits[6], qubits[7]);
            CNOT(qubits[5], qubits[8]);
            CNOT(qubits[6], qubits[8]);
            CNOT(qubits[6], qubits[9]);
            CNOT(qubits[6], qubits[9]);
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[8])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[9])));
            H(qubits[10]);
            CNOT(qubits[10], qubits[11]);
            CNOT(qubits[11], qubits[12]);
            CNOT(qubits[10], qubits[13]);
            CNOT(qubits[11], qubits[13]);
            CNOT(qubits[11], qubits[14]);
            CNOT(qubits[11], qubits[14]);
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[13])));
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[14])));
            H(qubits[15]);
            CNOT(qubits[15], qubits[16]);
            CNOT(qubits[16], qubits[17]);
            CNOT(qubits[15], qubits[18]);
            CNOT(qubits[16], qubits[18]);
            CNOT(qubits[16], qubits[19]);
            CNOT(qubits[16], qubits[19]);
            set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[18])));
            set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[19])));
            H(qubits[20]);
            CNOT(qubits[20], qubits[21]);
            CNOT(qubits[21], qubits[22]);
            CNOT(qubits[20], qubits[23]);
            CNOT(qubits[21], qubits[23]);
            CNOT(qubits[21], qubits[24]);
            CNOT(qubits[21], qubits[24]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[23])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[24])));
            H(qubits[25]);
            CNOT(qubits[25], qubits[26]);
            CNOT(qubits[26], qubits[27]);
            CNOT(qubits[25], qubits[28]);
            CNOT(qubits[26], qubits[28]);
            CNOT(qubits[26], qubits[29]);
            CNOT(qubits[26], qubits[29]);
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[28])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[29])));
            H(qubits[30]);
            CNOT(qubits[30], qubits[31]);
            CNOT(qubits[31], qubits[32]);
            CNOT(qubits[30], qubits[33]);
            CNOT(qubits[31], qubits[33]);
            CNOT(qubits[31], qubits[34]);
            CNOT(qubits[31], qubits[34]);
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[33])));
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[34])));
            H(qubits[35]);
            CNOT(qubits[35], qubits[36]);
            CNOT(qubits[36], qubits[37]);
            CNOT(qubits[35], qubits[38]);
            CNOT(qubits[36], qubits[38]);
            CNOT(qubits[36], qubits[39]);
            CNOT(qubits[36], qubits[39]);
            set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[38])));
            set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[39])));
            H(qubits[40]);
            CNOT(qubits[40], qubits[41]);
            CNOT(qubits[41], qubits[42]);
            CNOT(qubits[40], qubits[43]);
            CNOT(qubits[41], qubits[43]);
            CNOT(qubits[41], qubits[44]);
            CNOT(qubits[41], qubits[44]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[43])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[44])));
            H(qubits[45]);
            CNOT(qubits[45], qubits[46]);
            CNOT(qubits[46], qubits[47]);
            CNOT(qubits[45], qubits[48]);
            CNOT(qubits[46], qubits[48]);
            CNOT(qubits[46], qubits[49]);
            CNOT(qubits[46], qubits[49]);
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[48])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[49])));
            H(qubits[50]);
            CNOT(qubits[50], qubits[51]);
            CNOT(qubits[51], qubits[52]);
            CNOT(qubits[50], qubits[53]);
            CNOT(qubits[51], qubits[53]);
            CNOT(qubits[51], qubits[54]);
            CNOT(qubits[51], qubits[54]);
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[53])));
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[54])));
            H(qubits[55]);
            CNOT(qubits[55], qubits[56]);
            CNOT(qubits[56], qubits[57]);
            CNOT(qubits[55], qubits[58]);
            CNOT(qubits[56], qubits[58]);
            CNOT(qubits[56], qubits[59]);
            CNOT(qubits[56], qubits[59]);
            set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[58])));
            set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[59])));
            H(qubits[60]);
            CNOT(qubits[60], qubits[61]);
            CNOT(qubits[61], qubits[62]);
            CNOT(qubits[60], qubits[63]);
            CNOT(qubits[61], qubits[63]);
            CNOT(qubits[61], qubits[64]);
            CNOT(qubits[61], qubits[64]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[63])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[64])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
