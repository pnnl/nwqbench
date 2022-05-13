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
        mutable meas = 0;
        using(qubits = Qubit[15]) {
            Ry(2.1506626, qubits[0]);
            Ry(1.4482467, qubits[1]);
            Ry(2.3705663, qubits[2]);
            Ry(1.9765769, qubits[3]);
            Ry(0.62383312, qubits[4]);
            Ry(2.8280429, qubits[5]);
            Ry(2.120318, qubits[6]);
            Ry(2.1798952, qubits[7]);
            Ry(0.7320994, qubits[8]);
            Ry(1.4714046, qubits[9]);
            Ry(1.3094267, qubits[10]);
            Ry(2.5935193, qubits[11]);
            Ry(1.8626523, qubits[12]);
            Ry(2.2725045, qubits[13]);
            Ry(1.4573817, qubits[14]);
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
        return (meas);
    }
}
