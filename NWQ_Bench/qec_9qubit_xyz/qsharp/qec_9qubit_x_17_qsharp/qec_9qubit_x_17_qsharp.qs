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
        using(qubits = Qubit[17]) {
            H(qubits[0]);
            CNOT(qubits[0], qubits[3]);
            CNOT(qubits[0], qubits[6]);
            H(qubits[0]);
            H(qubits[3]);
            H(qubits[6]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[3], qubits[4]);
            CNOT(qubits[6], qubits[7]);
            CNOT(qubits[0], qubits[2]);
            CNOT(qubits[3], qubits[5]);
            CNOT(qubits[6], qubits[8]);
            CNOT(qubits[0], qubits[9]);
            CNOT(qubits[1], qubits[9]);
            CNOT(qubits[1], qubits[10]);
            CNOT(qubits[2], qubits[10]);
            CNOT(qubits[3], qubits[11]);
            CNOT(qubits[4], qubits[11]);
            CNOT(qubits[4], qubits[12]);
            CNOT(qubits[5], qubits[12]);
            CNOT(qubits[6], qubits[13]);
            CNOT(qubits[7], qubits[13]);
            CNOT(qubits[7], qubits[14]);
            CNOT(qubits[8], qubits[14]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[9])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[10])));
            set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[11])));
            set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[12])));
            set c0 = SetBitValue(c0, 4, ResultAsBool(M(qubits[13])));
            set c0 = SetBitValue(c0, 5, ResultAsBool(M(qubits[14])));
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            H(qubits[5]);
            H(qubits[6]);
            H(qubits[7]);
            H(qubits[8]);
            CNOT(qubits[0], qubits[15]);
            CNOT(qubits[3], qubits[16]);
            CNOT(qubits[1], qubits[15]);
            CNOT(qubits[4], qubits[16]);
            CNOT(qubits[2], qubits[15]);
            CNOT(qubits[5], qubits[16]);
            CNOT(qubits[3], qubits[15]);
            CNOT(qubits[6], qubits[16]);
            CNOT(qubits[4], qubits[15]);
            CNOT(qubits[7], qubits[16]);
            CNOT(qubits[5], qubits[15]);
            CNOT(qubits[8], qubits[16]);
            set c0 = SetBitValue(c0, 6, ResultAsBool(M(qubits[15])));
            set c0 = SetBitValue(c0, 7, ResultAsBool(M(qubits[16])));
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            H(qubits[5]);
            H(qubits[6]);
            H(qubits[7]);
            ResetAll(qubits);
        }
        return (c0);
    }
}
