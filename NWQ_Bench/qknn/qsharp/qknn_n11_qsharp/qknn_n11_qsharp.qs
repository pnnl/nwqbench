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
        using(qubits = Qubit[11]) {
            H(qubits[0]);
            Ry(2.8008902, qubits[1]);
            Ry(0.69545835, qubits[2]);
            Ry(0.099936864, qubits[3]);
            Ry(3.078129, qubits[4]);
            Ry(0.68494174, qubits[5]);
            Ry(0.53728786, qubits[6]);
            Ry(3.0576215, qubits[7]);
            Ry(0.26289246, qubits[8]);
            Ry(1.1357725, qubits[9]);
            Ry(0.98289791, qubits[10]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[6]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[7]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[8]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[9]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[10]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
