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
        using(qubits = Qubit[65]) {
            H(qubits[0]);
            Ry(0.86584834, qubits[1]);
            Ry(0.14743545, qubits[2]);
            Ry(0.64245885, qubits[3]);
            Ry(0.25817201, qubits[4]);
            Ry(0.40688468, qubits[5]);
            Ry(1.0394706, qubits[6]);
            Ry(2.5998695, qubits[7]);
            Ry(0.1055923, qubits[8]);
            Ry(2.4725444, qubits[9]);
            Ry(0.18212307, qubits[10]);
            Ry(2.2954319, qubits[11]);
            Ry(2.4837325, qubits[12]);
            Ry(1.0053865, qubits[13]);
            Ry(2.3769598, qubits[14]);
            Ry(0.71175862, qubits[15]);
            Ry(2.8680846, qubits[16]);
            Ry(2.9177723, qubits[17]);
            Ry(2.7116586, qubits[18]);
            Ry(1.5525267, qubits[19]);
            Ry(3.0664089, qubits[20]);
            Ry(1.9557245, qubits[21]);
            Ry(0.33250542, qubits[22]);
            Ry(0.39294631, qubits[23]);
            Ry(0.08921268, qubits[24]);
            Ry(2.0177685, qubits[25]);
            Ry(1.08657, qubits[26]);
            Ry(1.6967852, qubits[27]);
            Ry(1.9741458, qubits[28]);
            Ry(2.954569, qubits[29]);
            Ry(2.8135386, qubits[30]);
            Ry(0.13754074, qubits[31]);
            Ry(1.2504093, qubits[32]);
            Ry(0.17780116, qubits[33]);
            Ry(3.1166501, qubits[34]);
            Ry(1.5933304, qubits[35]);
            Ry(1.5154323, qubits[36]);
            Ry(0.98146752, qubits[37]);
            Ry(0.2271846, qubits[38]);
            Ry(0.68798613, qubits[39]);
            Ry(1.3090969, qubits[40]);
            Ry(2.1192561, qubits[41]);
            Ry(2.527927, qubits[42]);
            Ry(1.4018773, qubits[43]);
            Ry(1.7981196, qubits[44]);
            Ry(0.54568437, qubits[45]);
            Ry(3.0629303, qubits[46]);
            Ry(2.7640781, qubits[47]);
            Ry(0.85225091, qubits[48]);
            Ry(2.9031715, qubits[49]);
            Ry(2.7264022, qubits[50]);
            Ry(2.4490761, qubits[51]);
            Ry(0.12435028, qubits[52]);
            Ry(1.0599252, qubits[53]);
            Ry(2.8109149, qubits[54]);
            Ry(2.0532561, qubits[55]);
            Ry(1.2379397, qubits[56]);
            Ry(2.3032082, qubits[57]);
            Ry(1.6474646, qubits[58]);
            Ry(0.98522003, qubits[59]);
            Ry(1.9140947, qubits[60]);
            Ry(2.7385181, qubits[61]);
            Ry(0.55956924, qubits[62]);
            Ry(3.0138218, qubits[63]);
            Ry(0.16889234, qubits[64]);
            Controlled SWAP([qubits[0]], (qubits[1], qubits[33]));
            Controlled SWAP([qubits[0]], (qubits[2], qubits[34]));
            Controlled SWAP([qubits[0]], (qubits[3], qubits[35]));
            Controlled SWAP([qubits[0]], (qubits[4], qubits[36]));
            Controlled SWAP([qubits[0]], (qubits[5], qubits[37]));
            Controlled SWAP([qubits[0]], (qubits[6], qubits[38]));
            Controlled SWAP([qubits[0]], (qubits[7], qubits[39]));
            Controlled SWAP([qubits[0]], (qubits[8], qubits[40]));
            Controlled SWAP([qubits[0]], (qubits[9], qubits[41]));
            Controlled SWAP([qubits[0]], (qubits[10], qubits[42]));
            Controlled SWAP([qubits[0]], (qubits[11], qubits[43]));
            Controlled SWAP([qubits[0]], (qubits[12], qubits[44]));
            Controlled SWAP([qubits[0]], (qubits[13], qubits[45]));
            Controlled SWAP([qubits[0]], (qubits[14], qubits[46]));
            Controlled SWAP([qubits[0]], (qubits[15], qubits[47]));
            Controlled SWAP([qubits[0]], (qubits[16], qubits[48]));
            Controlled SWAP([qubits[0]], (qubits[17], qubits[49]));
            Controlled SWAP([qubits[0]], (qubits[18], qubits[50]));
            Controlled SWAP([qubits[0]], (qubits[19], qubits[51]));
            Controlled SWAP([qubits[0]], (qubits[20], qubits[52]));
            Controlled SWAP([qubits[0]], (qubits[21], qubits[53]));
            Controlled SWAP([qubits[0]], (qubits[22], qubits[54]));
            Controlled SWAP([qubits[0]], (qubits[23], qubits[55]));
            Controlled SWAP([qubits[0]], (qubits[24], qubits[56]));
            Controlled SWAP([qubits[0]], (qubits[25], qubits[57]));
            Controlled SWAP([qubits[0]], (qubits[26], qubits[58]));
            Controlled SWAP([qubits[0]], (qubits[27], qubits[59]));
            Controlled SWAP([qubits[0]], (qubits[28], qubits[60]));
            Controlled SWAP([qubits[0]], (qubits[29], qubits[61]));
            Controlled SWAP([qubits[0]], (qubits[30], qubits[62]));
            Controlled SWAP([qubits[0]], (qubits[31], qubits[63]));
            Controlled SWAP([qubits[0]], (qubits[32], qubits[64]));
            H(qubits[0]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
