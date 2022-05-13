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
        using(qubits = Qubit[25]) {
            H(qubits[0]);
            Ry(0.93346815, qubits[1]);
            Ry(0.82988213, qubits[2]);
            Ry(1.181111, qubits[3]);
            Ry(1.802503, qubits[4]);
            Ry(2.969805, qubits[5]);
            Ry(1.5765553, qubits[6]);
            Ry(1.8340893, qubits[7]);
            Ry(2.741925, qubits[8]);
            Ry(1.5106361, qubits[9]);
            Ry(0.76354036, qubits[10]);
            Ry(0.15484631, qubits[11]);
            Ry(1.9311432, qubits[12]);
            Ry(0.69057517, qubits[13]);
            Ry(0.74294505, qubits[14]);
            Ry(0.79338648, qubits[15]);
            Ry(1.9075145, qubits[16]);
            Ry(2.5852457, qubits[17]);
            Ry(1.5388629, qubits[18]);
            Ry(0.8484669, qubits[19]);
            Ry(1.9789905, qubits[20]);
            Ry(1.177473, qubits[21]);
            Ry(0.46112786, qubits[22]);
            Ry(0.17065064, qubits[23]);
            Ry(1.8262873, qubits[24]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[13]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[14]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[15]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[16]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[17]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[18]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[19]));
            Controlled SWAP([qubits[0]], (qubits[8], qubits[20]));
            Controlled SWAP([qubits[0]], (qubits[9], qubits[21]));
            Controlled SWAP([qubits[0]], (qubits[10], qubits[22]));
            Controlled SWAP([qubits[0]], (qubits[11], qubits[23]));
            Controlled SWAP([qubits[0]], (qubits[12], qubits[24]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
