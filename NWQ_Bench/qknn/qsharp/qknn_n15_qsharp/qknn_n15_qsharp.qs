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
            Ry(0.27466857, qubits[1]);
            Ry(0.9919349, qubits[2]);
            Ry(0.1085488, qubits[3]);
            Ry(2.6658346, qubits[4]);
            Ry(2.6766281, qubits[5]);
            Ry(0.24565172, qubits[6]);
            Ry(2.9270122, qubits[7]);
            Ry(0.16299404, qubits[8]);
            Ry(2.3066568, qubits[9]);
            Ry(1.5632304, qubits[10]);
            Ry(0.523205, qubits[11]);
            Ry(0.80548265, qubits[12]);
            Ry(1.994984, qubits[13]);
            Ry(2.6026488, qubits[14]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[8]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[9]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[10]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[11]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[12]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[13]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[14]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
