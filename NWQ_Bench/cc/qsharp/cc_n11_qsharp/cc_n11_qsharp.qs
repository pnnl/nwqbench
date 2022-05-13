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
        using(qubits = Qubit[11]) {
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
            CNOT(qubits[0], qubits[10]);
            CNOT(qubits[1], qubits[10]);
            CNOT(qubits[2], qubits[10]);
            CNOT(qubits[3], qubits[10]);
            CNOT(qubits[4], qubits[10]);
            CNOT(qubits[5], qubits[10]);
            CNOT(qubits[6], qubits[10]);
            CNOT(qubits[7], qubits[10]);
            CNOT(qubits[8], qubits[10]);
            CNOT(qubits[9], qubits[10]);
            set c0 = SetBitValue(c0, 10, ResultAsBool(M(qubits[10])));
            if(c0 == 0) {
                X(qubits[10]);
            }
            if(c0 == 0) {
                H(qubits[10]);
            }
            if(c0 == 1024) {
                H(qubits[0]);
            }
            if(c0 == 1024) {
                H(qubits[1]);
            }
            if(c0 == 1024) {
                H(qubits[2]);
            }
            if(c0 == 1024) {
                H(qubits[3]);
            }
            if(c0 == 1024) {
                H(qubits[4]);
            }
            if(c0 == 1024) {
                H(qubits[5]);
            }
            if(c0 == 1024) {
                H(qubits[6]);
            }
            if(c0 == 1024) {
                H(qubits[7]);
            }
            if(c0 == 1024) {
                H(qubits[8]);
            }
            if(c0 == 1024) {
                H(qubits[9]);
            }
            if(c0 == 0) {
                CNOT(qubits[3], qubits[10]);
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
            ResetAll(qubits);
        }
        return (c0);
    }
}
