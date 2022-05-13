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
        using(qubits = Qubit[15]) {
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
            X(qubits[14]);
            H(qubits[14]);
            CNOT(qubits[0], qubits[14]);
            H(qubits[0]);
            CNOT(qubits[1], qubits[14]);
            H(qubits[1]);
            CNOT(qubits[2], qubits[14]);
            H(qubits[2]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[14]);
            H(qubits[4]);
            H(qubits[5]);
            CNOT(qubits[6], qubits[14]);
            H(qubits[6]);
            H(qubits[7]);
            H(qubits[8]);
            CNOT(qubits[9], qubits[14]);
            H(qubits[9]);
            CNOT(qubits[10], qubits[14]);
            H(qubits[10]);
            H(qubits[11]);
            H(qubits[12]);
            CNOT(qubits[13], qubits[14]);
            H(qubits[13]);
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
            ResetAll(qubits);
        }
        return (c0);
    }
}
