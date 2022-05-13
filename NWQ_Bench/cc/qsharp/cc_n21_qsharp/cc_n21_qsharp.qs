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
        using(qubits = Qubit[21]) {
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
            CNOT(qubits[0], qubits[20]);
            CNOT(qubits[1], qubits[20]);
            CNOT(qubits[2], qubits[20]);
            CNOT(qubits[3], qubits[20]);
            CNOT(qubits[4], qubits[20]);
            CNOT(qubits[5], qubits[20]);
            CNOT(qubits[6], qubits[20]);
            CNOT(qubits[7], qubits[20]);
            CNOT(qubits[8], qubits[20]);
            CNOT(qubits[9], qubits[20]);
            CNOT(qubits[10], qubits[20]);
            CNOT(qubits[11], qubits[20]);
            CNOT(qubits[12], qubits[20]);
            CNOT(qubits[13], qubits[20]);
            CNOT(qubits[14], qubits[20]);
            CNOT(qubits[15], qubits[20]);
            CNOT(qubits[16], qubits[20]);
            CNOT(qubits[17], qubits[20]);
            CNOT(qubits[18], qubits[20]);
            CNOT(qubits[19], qubits[20]);
            set c0 = SetBitValue(c0, 20, ResultAsBool(M(qubits[20])));
            if(c0 == 0) {
                X(qubits[20]);
            }
            if(c0 == 0) {
                H(qubits[20]);
            }
            if(c0 == 1048576) {
                H(qubits[0]);
            }
            if(c0 == 1048576) {
                H(qubits[1]);
            }
            if(c0 == 1048576) {
                H(qubits[2]);
            }
            if(c0 == 1048576) {
                H(qubits[3]);
            }
            if(c0 == 1048576) {
                H(qubits[4]);
            }
            if(c0 == 1048576) {
                H(qubits[5]);
            }
            if(c0 == 1048576) {
                H(qubits[6]);
            }
            if(c0 == 1048576) {
                H(qubits[7]);
            }
            if(c0 == 1048576) {
                H(qubits[8]);
            }
            if(c0 == 1048576) {
                H(qubits[9]);
            }
            if(c0 == 1048576) {
                H(qubits[10]);
            }
            if(c0 == 1048576) {
                H(qubits[11]);
            }
            if(c0 == 1048576) {
                H(qubits[12]);
            }
            if(c0 == 1048576) {
                H(qubits[13]);
            }
            if(c0 == 1048576) {
                H(qubits[14]);
            }
            if(c0 == 1048576) {
                H(qubits[15]);
            }
            if(c0 == 1048576) {
                H(qubits[16]);
            }
            if(c0 == 1048576) {
                H(qubits[17]);
            }
            if(c0 == 1048576) {
                H(qubits[18]);
            }
            if(c0 == 1048576) {
                H(qubits[19]);
            }
            if(c0 == 0) {
                CNOT(qubits[6], qubits[20]);
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
            ResetAll(qubits);
        }
        return (c0);
    }
}
