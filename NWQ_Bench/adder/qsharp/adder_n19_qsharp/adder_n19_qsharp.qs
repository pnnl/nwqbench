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
        using(qubits = Qubit[19]) {
            X(qubits[1]);
            X(qubits[2]);
            X(qubits[3]);
            X(qubits[4]);
            X(qubits[5]);
            X(qubits[6]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[16]);
            CNOT(qubits[0], qubits[8]);
            CNOT(qubits[0], qubits[16]);
            CCNOT(qubits[16], qubits[8], qubits[0]);
            CNOT(qubits[1], qubits[9]);
            CNOT(qubits[1], qubits[0]);
            CCNOT(qubits[0], qubits[9], qubits[1]);
            CNOT(qubits[2], qubits[10]);
            CNOT(qubits[2], qubits[1]);
            CCNOT(qubits[1], qubits[10], qubits[2]);
            CNOT(qubits[3], qubits[11]);
            CNOT(qubits[3], qubits[2]);
            CCNOT(qubits[2], qubits[11], qubits[3]);
            CNOT(qubits[3], qubits[17]);
            CCNOT(qubits[2], qubits[11], qubits[3]);
            CNOT(qubits[3], qubits[2]);
            CNOT(qubits[2], qubits[11]);
            CCNOT(qubits[1], qubits[10], qubits[2]);
            CNOT(qubits[2], qubits[1]);
            CNOT(qubits[1], qubits[10]);
            CCNOT(qubits[0], qubits[9], qubits[1]);
            CNOT(qubits[1], qubits[0]);
            CNOT(qubits[0], qubits[9]);
            CCNOT(qubits[16], qubits[8], qubits[0]);
            CNOT(qubits[0], qubits[16]);
            CNOT(qubits[16], qubits[8]);
            CNOT(qubits[4], qubits[12]);
            CNOT(qubits[4], qubits[17]);
            CCNOT(qubits[17], qubits[12], qubits[4]);
            CNOT(qubits[5], qubits[13]);
            CNOT(qubits[5], qubits[4]);
            CCNOT(qubits[4], qubits[13], qubits[5]);
            CNOT(qubits[6], qubits[14]);
            CNOT(qubits[6], qubits[5]);
            CCNOT(qubits[5], qubits[14], qubits[6]);
            CNOT(qubits[7], qubits[15]);
            CNOT(qubits[7], qubits[6]);
            CCNOT(qubits[6], qubits[15], qubits[7]);
            CNOT(qubits[7], qubits[18]);
            CCNOT(qubits[6], qubits[15], qubits[7]);
            CNOT(qubits[7], qubits[6]);
            CNOT(qubits[6], qubits[15]);
            CCNOT(qubits[5], qubits[14], qubits[6]);
            CNOT(qubits[6], qubits[5]);
            CNOT(qubits[5], qubits[14]);
            CCNOT(qubits[4], qubits[13], qubits[5]);
            CNOT(qubits[5], qubits[4]);
            CNOT(qubits[4], qubits[13]);
            CCNOT(qubits[17], qubits[12], qubits[4]);
            CNOT(qubits[4], qubits[17]);
            CNOT(qubits[17], qubits[12]);
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
            ResetAll(qubits);
        }
        return (c, meas);
    }
}
