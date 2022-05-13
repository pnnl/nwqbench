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
        using(qubits = Qubit[6]) {
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[5]);
            CNOT(qubits[2], qubits[5]);
            CNOT(qubits[3], qubits[5]);
            CNOT(qubits[4], qubits[5]);
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[5])));
            if(c0 == 0) {
                X(qubits[5]);
            }
            if(c0 == 0) {
                H(qubits[5]);
            }
            if(c0 == 32) {
                H(qubits[0]);
            }
            if(c0 == 32) {
                H(qubits[1]);
            }
            if(c0 == 32) {
                H(qubits[2]);
            }
            if(c0 == 32) {
                H(qubits[3]);
            }
            if(c0 == 32) {
                H(qubits[4]);
            }
            if(c0 == 0) {
                CNOT(qubits[1], qubits[5]);
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
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[1])));
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[2])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[3])));
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[4])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
