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
        using(qubits = Qubit[5]) {
            Ry(-PI() / 4.0, qubits[0]);
            Ry(-0.95531662, qubits[1]);
            Ry(-PI() / 3.0, qubits[2]);
            Ry(-1.1071487, qubits[3]);
            X(qubits[4]);
            Controlled Z([qubits[4]], (qubits[3]));
            Ry(1.1071487, qubits[3]);
            Controlled Z([qubits[3]], (qubits[2]));
            Ry(PI() / 3.0, qubits[2]);
            CNOT(qubits[3], qubits[4]);
            Controlled Z([qubits[2]], (qubits[1]));
            Ry(0.95531662, qubits[1]);
            CNOT(qubits[2], qubits[3]);
            Controlled Z([qubits[1]], (qubits[0]));
            Ry(PI() / 4.0, qubits[0]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[1]);
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            set meas = SetBitValue(meas, 3, ResultAsBool(M(qubits[3])));
            set meas = SetBitValue(meas, 4, ResultAsBool(M(qubits[4])));
            ResetAll(qubits);
        }
        return (c, meas);
    }
}
