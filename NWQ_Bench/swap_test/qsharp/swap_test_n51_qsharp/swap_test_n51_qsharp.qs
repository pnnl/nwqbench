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
        using(qubits = Qubit[51]) {
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
            Rx(2.9808713, qubits[15]);
            Rx(-4.5722067, qubits[16]);
            Rx(-2.9717581, qubits[17]);
            Rx(4.3812134, qubits[18]);
            Rx(-0.54413824, qubits[19]);
            Rx(2.8824416, qubits[20]);
            Rx(0.99178896, qubits[21]);
            Rx(5.4169858, qubits[22]);
            Rx(5.7239307, qubits[23]);
            Rx(3.7629698, qubits[24]);
            Rx(-4.5485128, qubits[25]);
            Rx(-3.2923147, qubits[26]);
            Rx(5.6875289, qubits[27]);
            Rx(1.2065807, qubits[28]);
            Rx(-6.0041031, qubits[29]);
            Rx(0.50271205, qubits[30]);
            Rx(-4.1172873, qubits[31]);
            Rx(4.8261369, qubits[32]);
            Rx(-1.5885531, qubits[33]);
            Rx(3.2780951, qubits[34]);
            Rx(2.2125048, qubits[35]);
            Rx(-2.1338861, qubits[36]);
            Rx(2.9294436, qubits[37]);
            Rx(4.0850493, qubits[38]);
            Rx(-2.9631606, qubits[39]);
            Rx(2.9322572, qubits[40]);
            Rx(-4.3125018, qubits[41]);
            Rx(-2.9593885, qubits[42]);
            Rx(4.335384, qubits[43]);
            Rx(-0.18151701, qubits[44]);
            Rx(3.026406, qubits[45]);
            Rx(0.67977512, qubits[46]);
            Rx(5.3901384, qubits[47]);
            Rx(5.4778772, qubits[48]);
            Rx(3.2416375, qubits[49]);
            Rx(-4.6932636, qubits[50]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[26]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[27]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[28]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[29]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[30]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[31]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[32]));
            Controlled SWAP([qubits[0]], (qubits[8], qubits[33]));
            Controlled SWAP([qubits[0]], (qubits[9], qubits[34]));
            Controlled SWAP([qubits[0]], (qubits[10], qubits[35]));
            Controlled SWAP([qubits[0]], (qubits[11], qubits[36]));
            Controlled SWAP([qubits[0]], (qubits[12], qubits[37]));
            Controlled SWAP([qubits[0]], (qubits[13], qubits[38]));
            Controlled SWAP([qubits[0]], (qubits[14], qubits[39]));
            Controlled SWAP([qubits[0]], (qubits[15], qubits[40]));
            Controlled SWAP([qubits[0]], (qubits[16], qubits[41]));
            Controlled SWAP([qubits[0]], (qubits[17], qubits[42]));
            Controlled SWAP([qubits[0]], (qubits[18], qubits[43]));
            Controlled SWAP([qubits[0]], (qubits[19], qubits[44]));
            Controlled SWAP([qubits[0]], (qubits[20], qubits[45]));
            Controlled SWAP([qubits[0]], (qubits[21], qubits[46]));
            Controlled SWAP([qubits[0]], (qubits[22], qubits[47]));
            Controlled SWAP([qubits[0]], (qubits[23], qubits[48]));
            Controlled SWAP([qubits[0]], (qubits[24], qubits[49]));
            Controlled SWAP([qubits[0]], (qubits[25], qubits[50]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
