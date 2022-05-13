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
        using(qubits = Qubit[5]) {
            H(qubits[0]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[3]);
            CNOT(qubits[1], qubits[3]);
            CNOT(qubits[1], qubits[4]);
            CNOT(qubits[1], qubits[4]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[3])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[4])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
