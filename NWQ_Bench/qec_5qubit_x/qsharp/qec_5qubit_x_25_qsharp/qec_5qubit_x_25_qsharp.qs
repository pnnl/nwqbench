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
        using(qubits = Qubit[25]) {
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
            ResetAll(qubits);
        }
        return (c0);
    }
}
