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
            u2(0.0, PI(), qubits[0]);
            Rx(PI() / 2.0, qubits[1]);
            Rx(PI() / 2.0, qubits[2]);
            Rx(PI() / 2.0, qubits[3]);
            Rx(PI() / 2.0, qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[3], qubits[4]);
            Rz(0.16702648, qubits[2]);
            Rz(2.8732151, qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[3], qubits[4]);
            Rx(-PI() / 2.0, qubits[1]);
            Rx(-PI() / 2.0, qubits[2]);
            Rx(-PI() / 2.0, qubits[3]);
            Rx(-PI() / 2.0, qubits[4]);
            u3(1.0109876, 0.0, 0.0, qubits[2]);
            u3(0.33986129, 0.0, 0.0, qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[3], qubits[4]);
            u3(-1.0109876, 0.0, 0.0, qubits[2]);
            u3(-0.33986129, 0.0, 0.0, qubits[4]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[3], qubits[4]);
            CNOT(qubits[3], qubits[1]);
            CCNOT(qubits[0], qubits[1], qubits[3]);
            CNOT(qubits[3], qubits[1]);
            CNOT(qubits[4], qubits[2]);
            CCNOT(qubits[0], qubits[2], qubits[4]);
            u2(0.0, PI(), qubits[0]);
            CNOT(qubits[4], qubits[2]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[3])));
            set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[4])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
