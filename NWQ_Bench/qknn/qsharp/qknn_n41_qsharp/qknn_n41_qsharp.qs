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
        using(qubits = Qubit[41]) {
            H(qubits[0]);
            Ry(0.50072778, qubits[1]);
            Ry(1.0905048, qubits[2]);
            Ry(0.96912599, qubits[3]);
            Ry(2.0864011, qubits[4]);
            Ry(2.7911299, qubits[5]);
            Ry(2.3880772, qubits[6]);
            Ry(2.2261445, qubits[7]);
            Ry(0.22184773, qubits[8]);
            Ry(2.7212956, qubits[9]);
            Ry(1.9315409, qubits[10]);
            Ry(2.3227224, qubits[11]);
            Ry(2.0549615, qubits[12]);
            Ry(1.3219394, qubits[13]);
            Ry(0.54140268, qubits[14]);
            Ry(1.8966163, qubits[15]);
            Ry(1.0842249, qubits[16]);
            Ry(1.3174914, qubits[17]);
            Ry(0.073000976, qubits[18]);
            Ry(1.3129869, qubits[19]);
            Ry(1.6354905, qubits[20]);
            Ry(0.8695423, qubits[21]);
            Ry(0.64843691, qubits[22]);
            Ry(2.9542704, qubits[23]);
            Ry(0.70479938, qubits[24]);
            Ry(1.8734066, qubits[25]);
            Ry(0.62818487, qubits[26]);
            Ry(1.9826479, qubits[27]);
            Ry(1.6334053, qubits[28]);
            Ry(0.73244297, qubits[29]);
            Ry(2.7419252, qubits[30]);
            Ry(0.42221128, qubits[31]);
            Ry(1.1315377, qubits[32]);
            Ry(0.6363216, qubits[33]);
            Ry(1.8338719, qubits[34]);
            Ry(1.3875238, qubits[35]);
            Ry(2.9311037, qubits[36]);
            Ry(0.54880829, qubits[37]);
            Ry(0.86364103, qubits[38]);
            Ry(1.0224812, qubits[39]);
            Ry(0.44227803, qubits[40]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[21]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[22]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[23]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[24]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[25]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[26]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[27]));
            Controlled SWAP([qubits[0]], (qubits[8], qubits[28]));
            Controlled SWAP([qubits[0]], (qubits[9], qubits[29]));
            Controlled SWAP([qubits[0]], (qubits[10], qubits[30]));
            Controlled SWAP([qubits[0]], (qubits[11], qubits[31]));
            Controlled SWAP([qubits[0]], (qubits[12], qubits[32]));
            Controlled SWAP([qubits[0]], (qubits[13], qubits[33]));
            Controlled SWAP([qubits[0]], (qubits[14], qubits[34]));
            Controlled SWAP([qubits[0]], (qubits[15], qubits[35]));
            Controlled SWAP([qubits[0]], (qubits[16], qubits[36]));
            Controlled SWAP([qubits[0]], (qubits[17], qubits[37]));
            Controlled SWAP([qubits[0]], (qubits[18], qubits[38]));
            Controlled SWAP([qubits[0]], (qubits[19], qubits[39]));
            Controlled SWAP([qubits[0]], (qubits[20], qubits[40]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
