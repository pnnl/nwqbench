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
    
    operation Circuit() : (Int, Int) {
        mutable c = 0;
        mutable meas = 0;
        using(qubits = Qubit[9]) {
            H(qubits[0]);
            Ry(3.7977104, qubits[1]);
            Ry(2.1872989, qubits[2]);
            Ry(1.8219176, qubits[3]);
            Ry(3.8088077, qubits[4]);
            Ry(-0.83617905, qubits[5]);
            Ry(-0.84824244, qubits[6]);
            Ry(-2.3567766, qubits[7]);
            Ry(1.9180287, qubits[8]);
            Rz(5.465414, qubits[1]);
            Rz(4.0266574, qubits[2]);
            Rz(4.2161812, qubits[3]);
            Rz(5.6376766, qubits[4]);
            Rz(1.7639482, qubits[5]);
            Rz(3.0085304, qubits[6]);
            Rz(-1.9598407, qubits[7]);
            Rz(-0.015369036, qubits[8]);
            yy(2.5820511, qubits[1], qubits[2]);
            zz(0.77865462, qubits[1], qubits[2]);
            yy(3.4375327, qubits[2], qubits[3]);
            zz(3.1808425, qubits[2], qubits[3]);
            Controlled Ry([qubits[1]], (1.2040922, qubits[2]));
            yy(3.9571394, qubits[3], qubits[4]);
            Controlled Rz([qubits[1]], (2.7980963, qubits[2]));
            zz(4.9835202, qubits[3], qubits[4]);
            Controlled Ry([qubits[2]], (0.35436225, qubits[3]));
            Controlled Rz([qubits[2]], (1.063099, qubits[3]));
            Controlled Ry([qubits[3]], (0.24436762, qubits[4]));
            Controlled Rz([qubits[3]], (3.2324448, qubits[4]));
            Controlled SWAP([qubits[0]], (qubits[1], qubits[5]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[6]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[7]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[8]));
            H(qubits[0]);
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            set meas = SetBitValue(meas, 3, ResultAsBool(M(qubits[3])));
            set meas = SetBitValue(meas, 4, ResultAsBool(M(qubits[4])));
            set meas = SetBitValue(meas, 5, ResultAsBool(M(qubits[5])));
            set meas = SetBitValue(meas, 6, ResultAsBool(M(qubits[6])));
            set meas = SetBitValue(meas, 7, ResultAsBool(M(qubits[7])));
            set meas = SetBitValue(meas, 8, ResultAsBool(M(qubits[8])));
            ResetAll(qubits);
        }
        return (c, meas);
    }
}
