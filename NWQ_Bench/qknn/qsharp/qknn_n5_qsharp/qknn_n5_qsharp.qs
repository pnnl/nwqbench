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
            Ry(2.2439274, qubits[1]);
            Ry(0.38780286, qubits[2]);
            Ry(2.8663306, qubits[3]);
            Ry(2.209665, qubits[4]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[3]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[4]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
