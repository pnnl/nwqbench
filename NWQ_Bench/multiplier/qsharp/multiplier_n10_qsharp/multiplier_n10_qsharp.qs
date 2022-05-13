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
        using(qubits = Qubit[10]) {
            X(qubits[6]);
            X(qubits[9]);
            CCNOT(qubits[8], qubits[6], qubits[1]);
            CCNOT(qubits[1], qubits[2], qubits[3]);
            CCNOT(qubits[8], qubits[7], qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[4], qubits[5]);
            CCNOT(qubits[0], qubits[2], qubits[3]);
            CNOT(qubits[3], qubits[5]);
            CCNOT(qubits[0], qubits[2], qubits[3]);
            CNOT(qubits[1], qubits[2]);
            CCNOT(qubits[1], qubits[2], qubits[3]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[2]);
            CCNOT(qubits[8], qubits[6], qubits[1]);
            CCNOT(qubits[1], qubits[2], qubits[3]);
            CCNOT(qubits[8], qubits[7], qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CCNOT(qubits[9], qubits[6], qubits[4]);
            CCNOT(qubits[0], qubits[2], qubits[3]);
            CNOT(qubits[4], qubits[5]);
            CNOT(qubits[3], qubits[5]);
            CCNOT(qubits[0], qubits[2], qubits[3]);
            CCNOT(qubits[9], qubits[6], qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CCNOT(qubits[1], qubits[2], qubits[3]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[2]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[2])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[5])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
