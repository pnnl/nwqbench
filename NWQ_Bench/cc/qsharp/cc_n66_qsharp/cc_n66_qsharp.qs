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
        using(qubits = Qubit[66]) {
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            H(qubits[5]);
            H(qubits[6]);
            H(qubits[7]);
            H(qubits[8]);
            H(qubits[9]);
            H(qubits[10]);
            H(qubits[11]);
            H(qubits[12]);
            H(qubits[13]);
            H(qubits[14]);
            H(qubits[15]);
            H(qubits[16]);
            H(qubits[17]);
            H(qubits[18]);
            H(qubits[19]);
            H(qubits[20]);
            H(qubits[21]);
            H(qubits[22]);
            H(qubits[23]);
            H(qubits[24]);
            H(qubits[25]);
            H(qubits[26]);
            H(qubits[27]);
            H(qubits[28]);
            H(qubits[29]);
            H(qubits[30]);
            H(qubits[31]);
            H(qubits[32]);
            H(qubits[33]);
            H(qubits[34]);
            H(qubits[35]);
            H(qubits[36]);
            H(qubits[37]);
            H(qubits[38]);
            H(qubits[39]);
            H(qubits[40]);
            H(qubits[41]);
            H(qubits[42]);
            H(qubits[43]);
            H(qubits[44]);
            H(qubits[45]);
            H(qubits[46]);
            H(qubits[47]);
            H(qubits[48]);
            H(qubits[49]);
            H(qubits[50]);
            H(qubits[51]);
            H(qubits[52]);
            H(qubits[53]);
            H(qubits[54]);
            H(qubits[55]);
            H(qubits[56]);
            H(qubits[57]);
            H(qubits[58]);
            H(qubits[59]);
            H(qubits[60]);
            H(qubits[61]);
            H(qubits[62]);
            H(qubits[63]);
            H(qubits[64]);
            CNOT(qubits[0], qubits[65]);
            CNOT(qubits[1], qubits[65]);
            CNOT(qubits[2], qubits[65]);
            CNOT(qubits[3], qubits[65]);
            CNOT(qubits[4], qubits[65]);
            CNOT(qubits[5], qubits[65]);
            CNOT(qubits[6], qubits[65]);
            CNOT(qubits[7], qubits[65]);
            CNOT(qubits[8], qubits[65]);
            CNOT(qubits[9], qubits[65]);
            CNOT(qubits[10], qubits[65]);
            CNOT(qubits[11], qubits[65]);
            CNOT(qubits[12], qubits[65]);
            CNOT(qubits[13], qubits[65]);
            CNOT(qubits[14], qubits[65]);
            CNOT(qubits[15], qubits[65]);
            CNOT(qubits[16], qubits[65]);
            CNOT(qubits[17], qubits[65]);
            CNOT(qubits[18], qubits[65]);
            CNOT(qubits[19], qubits[65]);
            CNOT(qubits[20], qubits[65]);
            CNOT(qubits[21], qubits[65]);
            CNOT(qubits[22], qubits[65]);
            CNOT(qubits[23], qubits[65]);
            CNOT(qubits[24], qubits[65]);
            CNOT(qubits[25], qubits[65]);
            CNOT(qubits[26], qubits[65]);
            CNOT(qubits[27], qubits[65]);
            CNOT(qubits[28], qubits[65]);
            CNOT(qubits[29], qubits[65]);
            CNOT(qubits[30], qubits[65]);
            CNOT(qubits[31], qubits[65]);
            CNOT(qubits[32], qubits[65]);
            CNOT(qubits[33], qubits[65]);
            CNOT(qubits[34], qubits[65]);
            CNOT(qubits[35], qubits[65]);
            CNOT(qubits[36], qubits[65]);
            CNOT(qubits[37], qubits[65]);
            CNOT(qubits[38], qubits[65]);
            CNOT(qubits[39], qubits[65]);
            CNOT(qubits[40], qubits[65]);
            CNOT(qubits[41], qubits[65]);
            CNOT(qubits[42], qubits[65]);
            CNOT(qubits[43], qubits[65]);
            CNOT(qubits[44], qubits[65]);
            CNOT(qubits[45], qubits[65]);
            CNOT(qubits[46], qubits[65]);
            CNOT(qubits[47], qubits[65]);
            CNOT(qubits[48], qubits[65]);
            CNOT(qubits[49], qubits[65]);
            CNOT(qubits[50], qubits[65]);
            CNOT(qubits[51], qubits[65]);
            CNOT(qubits[52], qubits[65]);
            CNOT(qubits[53], qubits[65]);
            CNOT(qubits[54], qubits[65]);
            CNOT(qubits[55], qubits[65]);
            CNOT(qubits[56], qubits[65]);
            CNOT(qubits[57], qubits[65]);
            CNOT(qubits[58], qubits[65]);
            CNOT(qubits[59], qubits[65]);
            CNOT(qubits[60], qubits[65]);
            CNOT(qubits[61], qubits[65]);
            CNOT(qubits[62], qubits[65]);
            CNOT(qubits[63], qubits[65]);
            CNOT(qubits[64], qubits[65]);
            set c0 = SetBitValue(c0, 65, ResultAsBool(M(qubits[65])));
            if(c0 == 0) {
                X(qubits[65]);
            }
            if(c0 == 0) {
                H(qubits[65]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[0]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[1]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[2]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[3]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[4]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[5]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[6]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[7]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[8]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[9]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[10]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[11]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[12]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[13]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[14]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[15]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[16]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[17]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[18]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[19]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[20]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[21]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[22]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[23]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[24]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[25]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[26]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[27]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[28]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[29]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[30]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[31]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[32]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[33]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[34]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[35]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[36]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[37]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[38]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[39]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[40]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[41]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[42]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[43]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[44]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[45]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[46]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[47]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[48]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[49]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[50]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[51]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[52]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[53]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[54]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[55]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[56]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[57]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[58]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[59]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[60]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[61]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[62]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[63]);
            }
            if(c0 == 36893488147419103000) {
                H(qubits[64]);
            }
            if(c0 == 0) {
                CNOT(qubits[24], qubits[65]);
            }
            if(c0 == 0) {
                H(qubits[0]);
            }
            if(c0 == 0) {
                H(qubits[1]);
            }
            if(c0 == 0) {
                H(qubits[2]);
            }
            if(c0 == 0) {
                H(qubits[3]);
            }
            if(c0 == 0) {
                H(qubits[4]);
            }
            if(c0 == 0) {
                H(qubits[5]);
            }
            if(c0 == 0) {
                H(qubits[6]);
            }
            if(c0 == 0) {
                H(qubits[7]);
            }
            if(c0 == 0) {
                H(qubits[8]);
            }
            if(c0 == 0) {
                H(qubits[9]);
            }
            if(c0 == 0) {
                H(qubits[10]);
            }
            if(c0 == 0) {
                H(qubits[11]);
            }
            if(c0 == 0) {
                H(qubits[12]);
            }
            if(c0 == 0) {
                H(qubits[13]);
            }
            if(c0 == 0) {
                H(qubits[14]);
            }
            if(c0 == 0) {
                H(qubits[15]);
            }
            if(c0 == 0) {
                H(qubits[16]);
            }
            if(c0 == 0) {
                H(qubits[17]);
            }
            if(c0 == 0) {
                H(qubits[18]);
            }
            if(c0 == 0) {
                H(qubits[19]);
            }
            if(c0 == 0) {
                H(qubits[20]);
            }
            if(c0 == 0) {
                H(qubits[21]);
            }
            if(c0 == 0) {
                H(qubits[22]);
            }
            if(c0 == 0) {
                H(qubits[23]);
            }
            if(c0 == 0) {
                H(qubits[24]);
            }
            if(c0 == 0) {
                H(qubits[25]);
            }
            if(c0 == 0) {
                H(qubits[26]);
            }
            if(c0 == 0) {
                H(qubits[27]);
            }
            if(c0 == 0) {
                H(qubits[28]);
            }
            if(c0 == 0) {
                H(qubits[29]);
            }
            if(c0 == 0) {
                H(qubits[30]);
            }
            if(c0 == 0) {
                H(qubits[31]);
            }
            if(c0 == 0) {
                H(qubits[32]);
            }
            if(c0 == 0) {
                H(qubits[33]);
            }
            if(c0 == 0) {
                H(qubits[34]);
            }
            if(c0 == 0) {
                H(qubits[35]);
            }
            if(c0 == 0) {
                H(qubits[36]);
            }
            if(c0 == 0) {
                H(qubits[37]);
            }
            if(c0 == 0) {
                H(qubits[38]);
            }
            if(c0 == 0) {
                H(qubits[39]);
            }
            if(c0 == 0) {
                H(qubits[40]);
            }
            if(c0 == 0) {
                H(qubits[41]);
            }
            if(c0 == 0) {
                H(qubits[42]);
            }
            if(c0 == 0) {
                H(qubits[43]);
            }
            if(c0 == 0) {
                H(qubits[44]);
            }
            if(c0 == 0) {
                H(qubits[45]);
            }
            if(c0 == 0) {
                H(qubits[46]);
            }
            if(c0 == 0) {
                H(qubits[47]);
            }
            if(c0 == 0) {
                H(qubits[48]);
            }
            if(c0 == 0) {
                H(qubits[49]);
            }
            if(c0 == 0) {
                H(qubits[50]);
            }
            if(c0 == 0) {
                H(qubits[51]);
            }
            if(c0 == 0) {
                H(qubits[52]);
            }
            if(c0 == 0) {
                H(qubits[53]);
            }
            if(c0 == 0) {
                H(qubits[54]);
            }
            if(c0 == 0) {
                H(qubits[55]);
            }
            if(c0 == 0) {
                H(qubits[56]);
            }
            if(c0 == 0) {
                H(qubits[57]);
            }
            if(c0 == 0) {
                H(qubits[58]);
            }
            if(c0 == 0) {
                H(qubits[59]);
            }
            if(c0 == 0) {
                H(qubits[60]);
            }
            if(c0 == 0) {
                H(qubits[61]);
            }
            if(c0 == 0) {
                H(qubits[62]);
            }
            if(c0 == 0) {
                H(qubits[63]);
            }
            if(c0 == 0) {
                H(qubits[64]);
            }
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[1])));
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[2])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[3])));
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[4])));
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[5])));
            set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[6])));
            set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[7])));
            set c0 = SetBitValue(c0, 8, ResultAsBool(M(qubits[8])));
            set c0 = SetBitValue(c0, 9, ResultAsBool(M(qubits[9])));
            set c0 = SetBitValue(c0, 10, ResultAsBool(M(qubits[10])));
            set c0 = SetBitValue(c0, 11, ResultAsBool(M(qubits[11])));
            set c0 = SetBitValue(c0, 12, ResultAsBool(M(qubits[12])));
            set c0 = SetBitValue(c0, 13, ResultAsBool(M(qubits[13])));
            set c0 = SetBitValue(c0, 14, ResultAsBool(M(qubits[14])));
            set c0 = SetBitValue(c0, 15, ResultAsBool(M(qubits[15])));
            set c0 = SetBitValue(c0, 16, ResultAsBool(M(qubits[16])));
            set c0 = SetBitValue(c0, 17, ResultAsBool(M(qubits[17])));
            set c0 = SetBitValue(c0, 18, ResultAsBool(M(qubits[18])));
            set c0 = SetBitValue(c0, 19, ResultAsBool(M(qubits[19])));
            set c0 = SetBitValue(c0, 20, ResultAsBool(M(qubits[20])));
            set c0 = SetBitValue(c0, 21, ResultAsBool(M(qubits[21])));
            set c0 = SetBitValue(c0, 22, ResultAsBool(M(qubits[22])));
            set c0 = SetBitValue(c0, 23, ResultAsBool(M(qubits[23])));
            set c0 = SetBitValue(c0, 24, ResultAsBool(M(qubits[24])));
            set c0 = SetBitValue(c0, 25, ResultAsBool(M(qubits[25])));
            set c0 = SetBitValue(c0, 26, ResultAsBool(M(qubits[26])));
            set c0 = SetBitValue(c0, 27, ResultAsBool(M(qubits[27])));
            set c0 = SetBitValue(c0, 28, ResultAsBool(M(qubits[28])));
            set c0 = SetBitValue(c0, 29, ResultAsBool(M(qubits[29])));
            set c0 = SetBitValue(c0, 30, ResultAsBool(M(qubits[30])));
            set c0 = SetBitValue(c0, 31, ResultAsBool(M(qubits[31])));
            set c0 = SetBitValue(c0, 32, ResultAsBool(M(qubits[32])));
            set c0 = SetBitValue(c0, 33, ResultAsBool(M(qubits[33])));
            set c0 = SetBitValue(c0, 34, ResultAsBool(M(qubits[34])));
            set c0 = SetBitValue(c0, 35, ResultAsBool(M(qubits[35])));
            set c0 = SetBitValue(c0, 36, ResultAsBool(M(qubits[36])));
            set c0 = SetBitValue(c0, 37, ResultAsBool(M(qubits[37])));
            set c0 = SetBitValue(c0, 38, ResultAsBool(M(qubits[38])));
            set c0 = SetBitValue(c0, 39, ResultAsBool(M(qubits[39])));
            set c0 = SetBitValue(c0, 40, ResultAsBool(M(qubits[40])));
            set c0 = SetBitValue(c0, 41, ResultAsBool(M(qubits[41])));
            set c0 = SetBitValue(c0, 42, ResultAsBool(M(qubits[42])));
            set c0 = SetBitValue(c0, 43, ResultAsBool(M(qubits[43])));
            set c0 = SetBitValue(c0, 44, ResultAsBool(M(qubits[44])));
            set c0 = SetBitValue(c0, 45, ResultAsBool(M(qubits[45])));
            set c0 = SetBitValue(c0, 46, ResultAsBool(M(qubits[46])));
            set c0 = SetBitValue(c0, 47, ResultAsBool(M(qubits[47])));
            set c0 = SetBitValue(c0, 48, ResultAsBool(M(qubits[48])));
            set c0 = SetBitValue(c0, 49, ResultAsBool(M(qubits[49])));
            set c0 = SetBitValue(c0, 50, ResultAsBool(M(qubits[50])));
            set c0 = SetBitValue(c0, 51, ResultAsBool(M(qubits[51])));
            set c0 = SetBitValue(c0, 52, ResultAsBool(M(qubits[52])));
            set c0 = SetBitValue(c0, 53, ResultAsBool(M(qubits[53])));
            set c0 = SetBitValue(c0, 54, ResultAsBool(M(qubits[54])));
            set c0 = SetBitValue(c0, 55, ResultAsBool(M(qubits[55])));
            set c0 = SetBitValue(c0, 56, ResultAsBool(M(qubits[56])));
            set c0 = SetBitValue(c0, 57, ResultAsBool(M(qubits[57])));
            set c0 = SetBitValue(c0, 58, ResultAsBool(M(qubits[58])));
            set c0 = SetBitValue(c0, 59, ResultAsBool(M(qubits[59])));
            set c0 = SetBitValue(c0, 60, ResultAsBool(M(qubits[60])));
            set c0 = SetBitValue(c0, 61, ResultAsBool(M(qubits[61])));
            set c0 = SetBitValue(c0, 62, ResultAsBool(M(qubits[62])));
            set c0 = SetBitValue(c0, 63, ResultAsBool(M(qubits[63])));
            set c0 = SetBitValue(c0, 64, ResultAsBool(M(qubits[64])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
