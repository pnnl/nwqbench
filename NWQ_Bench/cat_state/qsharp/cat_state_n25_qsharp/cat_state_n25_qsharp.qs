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
    
    operation Circuit() : (Int, Int) {
        mutable c = 0;
        mutable meas = 0;
        using(qubits = Qubit[25]) {
            H(qubits[0]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[2], qubits[3]);
            CNOT(qubits[3], qubits[4]);
            CNOT(qubits[4], qubits[5]);
            CNOT(qubits[5], qubits[6]);
            CNOT(qubits[6], qubits[7]);
            CNOT(qubits[7], qubits[8]);
            CNOT(qubits[8], qubits[9]);
            CNOT(qubits[9], qubits[10]);
            CNOT(qubits[10], qubits[11]);
            CNOT(qubits[11], qubits[12]);
            CNOT(qubits[12], qubits[13]);
            CNOT(qubits[13], qubits[14]);
            CNOT(qubits[14], qubits[15]);
            CNOT(qubits[15], qubits[16]);
            CNOT(qubits[16], qubits[17]);
            CNOT(qubits[17], qubits[18]);
            CNOT(qubits[18], qubits[19]);
            CNOT(qubits[19], qubits[20]);
            CNOT(qubits[20], qubits[21]);
            CNOT(qubits[21], qubits[22]);
            CNOT(qubits[22], qubits[23]);
            CNOT(qubits[23], qubits[24]);
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            set meas = SetBitValue(meas, 3, ResultAsBool(M(qubits[3])));
            set meas = SetBitValue(meas, 4, ResultAsBool(M(qubits[4])));
            set meas = SetBitValue(meas, 5, ResultAsBool(M(qubits[5])));
            set meas = SetBitValue(meas, 6, ResultAsBool(M(qubits[6])));
            set meas = SetBitValue(meas, 7, ResultAsBool(M(qubits[7])));
            set meas = SetBitValue(meas, 8, ResultAsBool(M(qubits[8])));
            set meas = SetBitValue(meas, 9, ResultAsBool(M(qubits[9])));
            set meas = SetBitValue(meas, 10, ResultAsBool(M(qubits[10])));
            set meas = SetBitValue(meas, 11, ResultAsBool(M(qubits[11])));
            set meas = SetBitValue(meas, 12, ResultAsBool(M(qubits[12])));
            set meas = SetBitValue(meas, 13, ResultAsBool(M(qubits[13])));
            set meas = SetBitValue(meas, 14, ResultAsBool(M(qubits[14])));
            set meas = SetBitValue(meas, 15, ResultAsBool(M(qubits[15])));
            set meas = SetBitValue(meas, 16, ResultAsBool(M(qubits[16])));
            set meas = SetBitValue(meas, 17, ResultAsBool(M(qubits[17])));
            set meas = SetBitValue(meas, 18, ResultAsBool(M(qubits[18])));
            set meas = SetBitValue(meas, 19, ResultAsBool(M(qubits[19])));
            set meas = SetBitValue(meas, 20, ResultAsBool(M(qubits[20])));
            set meas = SetBitValue(meas, 21, ResultAsBool(M(qubits[21])));
            set meas = SetBitValue(meas, 22, ResultAsBool(M(qubits[22])));
            set meas = SetBitValue(meas, 23, ResultAsBool(M(qubits[23])));
            set meas = SetBitValue(meas, 24, ResultAsBool(M(qubits[24])));
            ResetAll(qubits);
        }
        return (c, meas);
    }
}
