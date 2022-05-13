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
        using(qubits = Qubit[15]) {
            H(qubits[0]);
            Ry(4.6657245, qubits[1]);
            Ry(1.552304, qubits[2]);
            Ry(0.75870345, qubits[3]);
            Ry(5.3649138, qubits[4]);
            Ry(4.8555286, qubits[5]);
            Ry(3.1742778, qubits[6]);
            Ry(4.3194047, qubits[7]);
            Ry(-2.4543916, qubits[8]);
            Ry(-2.0350321, qubits[9]);
            Ry(1.147724, qubits[10]);
            Ry(2.0464092, qubits[11]);
            Ry(-1.8095397, qubits[12]);
            Ry(-1.4813434, qubits[13]);
            Ry(-0.85377198, qubits[14]);
            Rz(3.7977995, qubits[1]);
            Rz(1.2413078, qubits[2]);
            Rz(1.2318791, qubits[3]);
            Rz(1.6023095, qubits[4]);
            Rz(1.1116801, qubits[5]);
            Rz(5.0114181, qubits[6]);
            Rz(5.5246443, qubits[7]);
            Rz(2.9980787, qubits[8]);
            Rz(-1.2059923, qubits[9]);
            Rz(2.4694738, qubits[10]);
            Rz(-2.3386974, qubits[11]);
            Rz(-0.49181898, qubits[12]);
            Rz(1.4527108, qubits[13]);
            Rz(1.0003452, qubits[14]);
            yy(3.6631548, qubits[1], qubits[2]);
            zz(6.2345074, qubits[1], qubits[2]);
            yy(1.170895, qubits[2], qubits[3]);
            zz(3.4619423, qubits[2], qubits[3]);
            Controlled Ry([qubits[1]], (3.99579, qubits[2]));
            yy(0.5775641, qubits[3], qubits[4]);
            Controlled Rz([qubits[1]], (4.9222201, qubits[2]));
            zz(2.9578414, qubits[3], qubits[4]);
            Controlled Ry([qubits[2]], (5.2865479, qubits[3]));
            yy(4.2772443, qubits[4], qubits[5]);
            Controlled Rz([qubits[2]], (4.6679845, qubits[3]));
            zz(2.084639, qubits[4], qubits[5]);
            Controlled Ry([qubits[3]], (1.3945543, qubits[4]));
            yy(0.63004618, qubits[5], qubits[6]);
            Controlled Rz([qubits[3]], (0.27538905, qubits[4]));
            zz(1.9195556, qubits[5], qubits[6]);
            Controlled Ry([qubits[4]], (3.0322379, qubits[5]));
            yy(5.7417715, qubits[6], qubits[7]);
            Controlled Rz([qubits[4]], (2.8183949, qubits[5]));
            zz(6.0514407, qubits[6], qubits[7]);
            Controlled Ry([qubits[5]], (2.2733639, qubits[6]));
            Controlled Rz([qubits[5]], (6.2831176, qubits[6]));
            Controlled Ry([qubits[6]], (5.1160943, qubits[7]));
            Controlled Rz([qubits[6]], (1.8639966, qubits[7]));
            Controlled SWAP([qubits[0]], (qubits[1], qubits[8]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[9]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[10]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[11]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[12]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[13]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[14]));
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
            set meas = SetBitValue(meas, 9, ResultAsBool(M(qubits[9])));
            set meas = SetBitValue(meas, 10, ResultAsBool(M(qubits[10])));
            set meas = SetBitValue(meas, 11, ResultAsBool(M(qubits[11])));
            set meas = SetBitValue(meas, 12, ResultAsBool(M(qubits[12])));
            set meas = SetBitValue(meas, 13, ResultAsBool(M(qubits[13])));
            set meas = SetBitValue(meas, 14, ResultAsBool(M(qubits[14])));
            ResetAll(qubits);
        }
        return (c, meas);
    }
}
