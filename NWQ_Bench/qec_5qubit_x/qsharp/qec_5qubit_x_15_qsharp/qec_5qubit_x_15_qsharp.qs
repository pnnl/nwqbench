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
            ResetAll(qubits);
        }
        return (c0);
    }
}
