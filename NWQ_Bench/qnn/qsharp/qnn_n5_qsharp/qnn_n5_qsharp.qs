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
            H(qubits[0]);
            Ry(4.9053416, qubits[1]);
            Ry(2.6219432, qubits[2]);
            Ry(2.1643378, qubits[3]);
            Ry(2.035242, qubits[4]);
            Rz(5.321323, qubits[1]);
            Rz(2.8180595, qubits[2]);
            Rz(2.5775709, qubits[3]);
            Rz(0.54460083, qubits[4]);
            yy(3.8044817, qubits[1], qubits[2]);
            zz(2.9653883, qubits[1], qubits[2]);
            Controlled Ry([qubits[1]], (3.8801311, qubits[2]));
            Controlled Rz([qubits[1]], (3.4880895, qubits[2]));
            Controlled SWAP([qubits[0]], (qubits[1], qubits[3]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[4]));
            H(qubits[0]);
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
