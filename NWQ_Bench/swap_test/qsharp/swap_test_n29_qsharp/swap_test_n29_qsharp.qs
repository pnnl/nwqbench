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
        using(qubits = Qubit[29]) {
            H(qubits[0]);
            Rx(-3.6924814, qubits[1]);
            Rx(5.4291652, qubits[2]);
            Rx(1.3594796, qubits[3]);
            Rx(-5.9123043, qubits[4]);
            Rx(-0.13186279, qubits[5]);
            Rx(-4.3869008, qubits[6]);
            Rx(4.9830092, qubits[7]);
            Rx(-1.4181518, qubits[8]);
            Rx(3.9058792, qubits[9]);
            Rx(2.1483107, qubits[10]);
            Rx(-1.552265, qubits[11]);
            Rx(3.5437778, qubits[12]);
            Rx(3.5074824, qubits[13]);
            Rx(-3.1458178, qubits[14]);
            Rx(-3.2923147, qubits[15]);
            Rx(5.6875289, qubits[16]);
            Rx(1.2065807, qubits[17]);
            Rx(-6.0041031, qubits[18]);
            Rx(0.50271205, qubits[19]);
            Rx(-4.1172873, qubits[20]);
            Rx(4.8261369, qubits[21]);
            Rx(-1.5885531, qubits[22]);
            Rx(3.2780951, qubits[23]);
            Rx(2.2125048, qubits[24]);
            Rx(-2.1338861, qubits[25]);
            Rx(2.9294436, qubits[26]);
            Rx(4.0850493, qubits[27]);
            Rx(-2.9631606, qubits[28]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[15]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[16]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[17]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[18]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[19]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[20]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[21]));
            Controlled SWAP([qubits[0]], (qubits[8], qubits[22]));
            Controlled SWAP([qubits[0]], (qubits[9], qubits[23]));
            Controlled SWAP([qubits[0]], (qubits[10], qubits[24]));
            Controlled SWAP([qubits[0]], (qubits[11], qubits[25]));
            Controlled SWAP([qubits[0]], (qubits[12], qubits[26]));
            Controlled SWAP([qubits[0]], (qubits[13], qubits[27]));
            Controlled SWAP([qubits[0]], (qubits[14], qubits[28]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
