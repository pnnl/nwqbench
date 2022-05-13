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
        using(qubits = Qubit[30]) {
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
            X(qubits[29]);
            H(qubits[29]);
            CNOT(qubits[0], qubits[29]);
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[29]);
            H(qubits[4]);
            CNOT(qubits[5], qubits[29]);
            H(qubits[5]);
            H(qubits[6]);
            CNOT(qubits[7], qubits[29]);
            H(qubits[7]);
            CNOT(qubits[8], qubits[29]);
            H(qubits[8]);
            H(qubits[9]);
            CNOT(qubits[10], qubits[29]);
            H(qubits[10]);
            CNOT(qubits[11], qubits[29]);
            H(qubits[11]);
            H(qubits[12]);
            CNOT(qubits[13], qubits[29]);
            H(qubits[13]);
            H(qubits[14]);
            CNOT(qubits[15], qubits[29]);
            H(qubits[15]);
            H(qubits[16]);
            CNOT(qubits[17], qubits[29]);
            H(qubits[17]);
            H(qubits[18]);
            H(qubits[19]);
            H(qubits[20]);
            CNOT(qubits[21], qubits[29]);
            H(qubits[21]);
            CNOT(qubits[22], qubits[29]);
            H(qubits[22]);
            CNOT(qubits[23], qubits[29]);
            H(qubits[23]);
            CNOT(qubits[24], qubits[29]);
            H(qubits[24]);
            CNOT(qubits[25], qubits[29]);
            H(qubits[25]);
            CNOT(qubits[26], qubits[29]);
            H(qubits[26]);
            CNOT(qubits[27], qubits[29]);
            H(qubits[27]);
            CNOT(qubits[28], qubits[29]);
            H(qubits[28]);
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
            ResetAll(qubits);
        }
        return (c0);
    }
}
