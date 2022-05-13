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
        using(qubits = Qubit[31]) {
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
            Ry(0.99378383, qubits[15]);
            Ry(1.6801839, qubits[16]);
            Ry(0.51077586, qubits[17]);
            Ry(2.2853262, qubits[18]);
            Ry(1.8372675, qubits[19]);
            Ry(2.1131759, qubits[20]);
            Ry(1.2755787, qubits[21]);
            Ry(2.7975419, qubits[22]);
            Ry(2.4755003, qubits[23]);
            Ry(2.161285, qubits[24]);
            Ry(0.91382352, qubits[25]);
            Ry(1.5041891, qubits[26]);
            Ry(0.42170479, qubits[27]);
            Ry(0.80734219, qubits[28]);
            Ry(1.9456087, qubits[29]);
            Ry(2.0823405, qubits[30]);
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
            set meas = SetBitValue(meas, 15, ResultAsBool(M(qubits[15])));
            set meas = SetBitValue(meas, 16, ResultAsBool(M(qubits[16])));
            set meas = SetBitValue(meas, 17, ResultAsBool(M(qubits[17])));
            set meas = SetBitValue(meas, 18, ResultAsBool(M(qubits[18])));
            set meas = SetBitValue(meas, 19, ResultAsBool(M(qubits[19])));
            set meas = SetBitValue(meas, 20, ResultAsBool(M(qubits[20])));
            set meas = SetBitValue(meas, 21, ResultAsBool(M(qubits[21])));
            set meas = SetBitValue(meas, 22, ResultAsBool(M(qubits[22])));
            set meas = SetBitValue(meas, 23, ResultAsBool(M(qubits[23])));
            set meas = SetBitValue(meas, 24, ResultAsBool(M(qubits[24])));
            set meas = SetBitValue(meas, 25, ResultAsBool(M(qubits[25])));
            set meas = SetBitValue(meas, 26, ResultAsBool(M(qubits[26])));
            set meas = SetBitValue(meas, 27, ResultAsBool(M(qubits[27])));
            set meas = SetBitValue(meas, 28, ResultAsBool(M(qubits[28])));
            set meas = SetBitValue(meas, 29, ResultAsBool(M(qubits[29])));
            set meas = SetBitValue(meas, 30, ResultAsBool(M(qubits[30])));
            ResetAll(qubits);
        }
        return (meas);
    }
}
