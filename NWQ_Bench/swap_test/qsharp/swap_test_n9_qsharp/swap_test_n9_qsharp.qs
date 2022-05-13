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
        using(qubits = Qubit[9]) {
            H(qubits[0]);
            Rx(-3.8535372, qubits[1]);
            Rx(-4.2592974, qubits[2]);
            Rx(0.76934517, qubits[3]);
            Rx(5.2757681, qubits[4]);
            Rx(-4.3555394, qubits[5]);
            Rx(-1.1088457, qubits[6]);
            Rx(0.60673656, qubits[7]);
            Rx(3.1760628, qubits[8]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[5]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[6]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[7]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[8]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
