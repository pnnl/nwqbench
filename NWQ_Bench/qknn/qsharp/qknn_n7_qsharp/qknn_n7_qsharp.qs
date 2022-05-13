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
        using(qubits = Qubit[7]) {
            H(qubits[0]);
            Ry(0.21315685, qubits[1]);
            Ry(0.13443125, qubits[2]);
            Ry(2.5425711, qubits[3]);
            Ry(1.3995784, qubits[4]);
            Ry(1.8805686, qubits[5]);
            Ry(2.0339493, qubits[6]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[4]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[5]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[6]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
