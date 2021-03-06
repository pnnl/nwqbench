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
        mutable c = 0;
        using(qubits = Qubit[25]) {
            Ry(2.4046372, qubits[0]);
            Ry(2.3336143, qubits[1]);
            Ry(0.72133708, qubits[2]);
            Ry(1.2300238, qubits[3]);
            Ry(0.10197243, qubits[4]);
            Ry(0.69592388, qubits[5]);
            Ry(1.3613843, qubits[6]);
            Ry(0.5556097, qubits[7]);
            Ry(1.4779006, qubits[8]);
            Ry(0.50657227, qubits[9]);
            Ry(2.9520682, qubits[10]);
            Ry(1.3080473, qubits[11]);
            Ry(2.8924044, qubits[12]);
            Ry(2.4984378, qubits[13]);
            Ry(2.9348787, qubits[14]);
            Ry(3.0971339, qubits[15]);
            Ry(2.921169, qubits[16]);
            Ry(1.1886529, qubits[17]);
            Ry(2.6757282, qubits[18]);
            Ry(2.338456, qubits[19]);
            Ry(2.0531018, qubits[20]);
            Ry(2.9369249, qubits[21]);
            Ry(1.6146981, qubits[22]);
            Controlled Ry([qubits[0]], (1.1414484, qubits[1]));
            Controlled Ry([qubits[1]], (1.3104948, qubits[2]));
            Controlled Ry([qubits[2]], (2.9488226, qubits[3]));
            Controlled Ry([qubits[3]], (2.3282812, qubits[4]));
            Controlled Ry([qubits[4]], (1.8701555, qubits[5]));
            Controlled Ry([qubits[5]], (0.16767714, qubits[6]));
            Controlled Ry([qubits[6]], (1.2373367, qubits[7]));
            Controlled Ry([qubits[7]], (2.674611, qubits[8]));
            Controlled Ry([qubits[8]], (1.5038571, qubits[9]));
            Controlled Ry([qubits[9]], (1.8698485, qubits[10]));
            Controlled Ry([qubits[10]], (0.294313, qubits[11]));
            Controlled Ry([qubits[11]], (0.8994402, qubits[12]));
            Controlled Ry([qubits[12]], (1.752392, qubits[13]));
            Controlled Ry([qubits[13]], (1.7175125, qubits[14]));
            Controlled Ry([qubits[14]], (0.37698405, qubits[15]));
            Controlled Ry([qubits[15]], (0.96841912, qubits[16]));
            Controlled Ry([qubits[16]], (3.0982528, qubits[17]));
            Controlled Ry([qubits[17]], (1.2282107, qubits[18]));
            Controlled Ry([qubits[18]], (0.80083453, qubits[19]));
            Controlled Ry([qubits[19]], (2.3188841, qubits[20]));
            Controlled Ry([qubits[20]], (2.5995155, qubits[21]));
            Controlled Ry([qubits[21]], (0.93857984, qubits[22]));
            Controlled Ry([qubits[22]], (0.63822073, qubits[0]));
            Ry(1.9413184, qubits[0]);
            Ry(1.2085058, qubits[1]);
            Ry(0.7701523, qubits[2]);
            Ry(3.0569623, qubits[3]);
            Ry(2.4862034, qubits[4]);
            Ry(1.3241212, qubits[5]);
            Ry(0.52798856, qubits[6]);
            Ry(2.5582703, qubits[7]);
            Ry(1.0876095, qubits[8]);
            Ry(0.2310176, qubits[9]);
            Ry(1.0148172, qubits[10]);
            Ry(1.7166428, qubits[11]);
            Ry(1.0521398, qubits[12]);
            Ry(2.239007, qubits[13]);
            Ry(0.64819717, qubits[14]);
            Ry(2.0142363, qubits[15]);
            Ry(2.9262324, qubits[16]);
            Ry(0.0054313038, qubits[17]);
            Ry(1.7623353, qubits[18]);
            Ry(0.87994577, qubits[19]);
            Ry(0.78226646, qubits[20]);
            Ry(2.0612786, qubits[21]);
            Ry(0.84047059, qubits[22]);
            Controlled Ry([qubits[0]], (1.34973, qubits[1]));
            Controlled Ry([qubits[1]], (0.97470663, qubits[2]));
            Controlled Ry([qubits[2]], (0.025435813, qubits[3]));
            Controlled Ry([qubits[3]], (2.9278685, qubits[4]));
            Controlled Ry([qubits[4]], (2.3737549, qubits[5]));
            Controlled Ry([qubits[5]], (2.8485333, qubits[6]));
            Controlled Ry([qubits[6]], (2.1689026, qubits[7]));
            Controlled Ry([qubits[7]], (2.2029461, qubits[8]));
            Controlled Ry([qubits[8]], (1.0586872, qubits[9]));
            Controlled Ry([qubits[9]], (1.6016692, qubits[10]));
            Controlled Ry([qubits[10]], (2.5923506, qubits[11]));
            Controlled Ry([qubits[11]], (2.358091, qubits[12]));
            Controlled Ry([qubits[12]], (1.0014829, qubits[13]));
            Controlled Ry([qubits[13]], (2.679315, qubits[14]));
            Controlled Ry([qubits[14]], (1.782026, qubits[15]));
            Controlled Ry([qubits[15]], (1.0299718, qubits[16]));
            Controlled Ry([qubits[16]], (3.0017512, qubits[17]));
            Controlled Ry([qubits[17]], (0.11425213, qubits[18]));
            Controlled Ry([qubits[18]], (1.0524761, qubits[19]));
            Controlled Ry([qubits[19]], (2.9116021, qubits[20]));
            Controlled Ry([qubits[20]], (2.0787959, qubits[21]));
            Controlled Ry([qubits[21]], (0.38858815, qubits[22]));
            Controlled Ry([qubits[22]], (1.2246489, qubits[0]));
            Ry(0.062132702, qubits[0]);
            Ry(2.0324349, qubits[1]);
            Ry(0.2411408, qubits[2]);
            Ry(0.3218655, qubits[3]);
            Ry(2.3034366, qubits[4]);
            Ry(2.1618027, qubits[5]);
            Ry(2.4662505, qubits[6]);
            Ry(0.10813863, qubits[7]);
            Ry(0.78527373, qubits[8]);
            Ry(1.1999737, qubits[9]);
            Ry(1.537061, qubits[10]);
            Ry(0.3983319, qubits[11]);
            Ry(1.9941611, qubits[12]);
            Ry(0.51317647, qubits[13]);
            Ry(0.10166123, qubits[14]);
            Ry(1.8670245, qubits[15]);
            Ry(0.0072601447, qubits[16]);
            Ry(2.7808594, qubits[17]);
            Ry(1.7465951, qubits[18]);
            Ry(0.15020818, qubits[19]);
            Ry(0.17539502, qubits[20]);
            Ry(0.1654123, qubits[21]);
            Ry(0.035401541, qubits[22]);
            Controlled Ry([qubits[0]], (2.243115, qubits[23]));
            Controlled Ry([qubits[1]], (1.7246459, qubits[23]));
            Controlled Ry([qubits[2]], (2.3173242, qubits[23]));
            Controlled Ry([qubits[3]], (1.7832024, qubits[23]));
            Controlled Ry([qubits[4]], (1.4016966, qubits[23]));
            Controlled Ry([qubits[5]], (0.55701435, qubits[23]));
            Controlled Ry([qubits[6]], (1.1949274, qubits[23]));
            Controlled Ry([qubits[7]], (0.92853556, qubits[23]));
            Controlled Ry([qubits[8]], (2.0343624, qubits[23]));
            Controlled Ry([qubits[9]], (2.1080536, qubits[23]));
            Controlled Ry([qubits[10]], (1.434495, qubits[23]));
            Controlled Ry([qubits[11]], (2.2557125, qubits[23]));
            Controlled Ry([qubits[12]], (2.8785988, qubits[23]));
            Controlled Ry([qubits[13]], (0.12036396, qubits[23]));
            Controlled Ry([qubits[14]], (0.21366093, qubits[23]));
            Controlled Ry([qubits[15]], (2.5115313, qubits[23]));
            Controlled Ry([qubits[16]], (0.61849089, qubits[23]));
            Controlled Ry([qubits[17]], (1.1318183, qubits[23]));
            Controlled Ry([qubits[18]], (1.1052579, qubits[23]));
            Controlled Ry([qubits[19]], (2.83834, qubits[23]));
            Controlled Ry([qubits[20]], (1.1548658, qubits[23]));
            Controlled Ry([qubits[21]], (1.4192155, qubits[23]));
            Controlled Ry([qubits[22]], (2.4928367, qubits[23]));
            Controlled Ry([qubits[0]], (1.1986511, qubits[24]));
            Controlled Ry([qubits[1]], (2.244777, qubits[24]));
            Controlled Ry([qubits[2]], (1.5451018, qubits[24]));
            Controlled Ry([qubits[3]], (2.5612201, qubits[24]));
            Controlled Ry([qubits[4]], (0.58222979, qubits[24]));
            Controlled Ry([qubits[5]], (2.7587097, qubits[24]));
            Controlled Ry([qubits[6]], (2.3223639, qubits[24]));
            Controlled Ry([qubits[7]], (1.7464534, qubits[24]));
            Controlled Ry([qubits[8]], (1.0925269, qubits[24]));
            Controlled Ry([qubits[9]], (1.4426669, qubits[24]));
            Controlled Ry([qubits[10]], (0.26513699, qubits[24]));
            Controlled Ry([qubits[11]], (0.8721534, qubits[24]));
            Controlled Ry([qubits[12]], (2.7416068, qubits[24]));
            Controlled Ry([qubits[13]], (2.4328144, qubits[24]));
            Controlled Ry([qubits[14]], (1.3445639, qubits[24]));
            Controlled Ry([qubits[15]], (1.9438733, qubits[24]));
            Controlled Ry([qubits[16]], (2.5758755, qubits[24]));
            Controlled Ry([qubits[17]], (0.5227285, qubits[24]));
            Controlled Ry([qubits[18]], (1.09593, qubits[24]));
            Controlled Ry([qubits[19]], (1.4953231, qubits[24]));
            Controlled Ry([qubits[20]], (0.85781967, qubits[24]));
            Controlled Ry([qubits[21]], (0.039022339, qubits[24]));
            Controlled Ry([qubits[22]], (0.11357496, qubits[24]));
            set c = SetBitValue(c, 0, ResultAsBool(M(qubits[23])));
            set c = SetBitValue(c, 1, ResultAsBool(M(qubits[24])));
            ResetAll(qubits);
        }
        return (c);
    }
}
