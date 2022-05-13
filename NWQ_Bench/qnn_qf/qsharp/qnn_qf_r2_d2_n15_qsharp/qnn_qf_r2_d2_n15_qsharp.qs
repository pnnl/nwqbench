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
        using(qubits = Qubit[15]) {
            Ry(1.7977745, qubits[0]);
            Ry(2.4290782, qubits[1]);
            Ry(2.0518248, qubits[2]);
            Ry(1.8828395, qubits[3]);
            Ry(2.6444115, qubits[4]);
            Ry(2.9523479, qubits[5]);
            Ry(2.7122252, qubits[6]);
            Ry(1.3092064, qubits[7]);
            Ry(2.5455586, qubits[8]);
            Ry(1.1707559, qubits[9]);
            Ry(0.73521457, qubits[10]);
            Ry(1.0956246, qubits[11]);
            Ry(1.6620362, qubits[12]);
            Controlled Ry([qubits[0]], (2.2936072, qubits[1]));
            Controlled Ry([qubits[1]], (2.4366259, qubits[2]));
            Controlled Ry([qubits[2]], (1.3873553, qubits[3]));
            Controlled Ry([qubits[3]], (1.5755903, qubits[4]));
            Controlled Ry([qubits[4]], (2.8188762, qubits[5]));
            Controlled Ry([qubits[5]], (0.44547731, qubits[6]));
            Controlled Ry([qubits[6]], (2.7036384, qubits[7]));
            Controlled Ry([qubits[7]], (0.95798642, qubits[8]));
            Controlled Ry([qubits[8]], (1.0212333, qubits[9]));
            Controlled Ry([qubits[9]], (1.2326703, qubits[10]));
            Controlled Ry([qubits[10]], (1.0304913, qubits[11]));
            Controlled Ry([qubits[11]], (2.7941224, qubits[12]));
            Controlled Ry([qubits[12]], (1.3519228, qubits[0]));
            Ry(2.6966784, qubits[0]);
            Ry(1.0185554, qubits[1]);
            Ry(0.2490335, qubits[2]);
            Ry(0.27822903, qubits[3]);
            Ry(0.67767603, qubits[4]);
            Ry(1.170178, qubits[5]);
            Ry(1.6017061, qubits[6]);
            Ry(1.1324313, qubits[7]);
            Ry(2.4205829, qubits[8]);
            Ry(1.0348663, qubits[9]);
            Ry(1.1960244, qubits[10]);
            Ry(0.17937507, qubits[11]);
            Ry(3.0740486, qubits[12]);
            Controlled Ry([qubits[0]], (2.8986654, qubits[1]));
            Controlled Ry([qubits[1]], (1.466542, qubits[2]));
            Controlled Ry([qubits[2]], (1.4942799, qubits[3]));
            Controlled Ry([qubits[3]], (1.1746099, qubits[4]));
            Controlled Ry([qubits[4]], (1.7224761, qubits[5]));
            Controlled Ry([qubits[5]], (1.4907356, qubits[6]));
            Controlled Ry([qubits[6]], (2.4893668, qubits[7]));
            Controlled Ry([qubits[7]], (1.3426198, qubits[8]));
            Controlled Ry([qubits[8]], (2.0298046, qubits[9]));
            Controlled Ry([qubits[9]], (0.31647779, qubits[10]));
            Controlled Ry([qubits[10]], (1.8223344, qubits[11]));
            Controlled Ry([qubits[11]], (2.5603944, qubits[12]));
            Controlled Ry([qubits[12]], (1.3949801, qubits[0]));
            Ry(0.092043951, qubits[0]);
            Ry(0.32876019, qubits[1]);
            Ry(3.0915138, qubits[2]);
            Ry(2.6452213, qubits[3]);
            Ry(3.1193449, qubits[4]);
            Ry(0.7492682, qubits[5]);
            Ry(1.9111307, qubits[6]);
            Ry(0.33431689, qubits[7]);
            Ry(2.934947, qubits[8]);
            Ry(2.5044793, qubits[9]);
            Ry(1.5396555, qubits[10]);
            Ry(1.1956838, qubits[11]);
            Ry(0.42721248, qubits[12]);
            Controlled Ry([qubits[0]], (0.55220528, qubits[13]));
            Controlled Ry([qubits[1]], (2.879998, qubits[13]));
            Controlled Ry([qubits[2]], (2.7494499, qubits[13]));
            Controlled Ry([qubits[3]], (0.085577304, qubits[13]));
            Controlled Ry([qubits[4]], (1.4899562, qubits[13]));
            Controlled Ry([qubits[5]], (2.6948186, qubits[13]));
            Controlled Ry([qubits[6]], (2.0293363, qubits[13]));
            Controlled Ry([qubits[7]], (2.9635696, qubits[13]));
            Controlled Ry([qubits[8]], (2.0392029, qubits[13]));
            Controlled Ry([qubits[9]], (0.47816264, qubits[13]));
            Controlled Ry([qubits[10]], (2.5668759, qubits[13]));
            Controlled Ry([qubits[11]], (0.18281766, qubits[13]));
            Controlled Ry([qubits[12]], (1.8175045, qubits[13]));
            Controlled Ry([qubits[0]], (3.1017869, qubits[14]));
            Controlled Ry([qubits[1]], (0.15811296, qubits[14]));
            Controlled Ry([qubits[2]], (1.3312993, qubits[14]));
            Controlled Ry([qubits[3]], (2.1821697, qubits[14]));
            Controlled Ry([qubits[4]], (1.0340898, qubits[14]));
            Controlled Ry([qubits[5]], (2.5211007, qubits[14]));
            Controlled Ry([qubits[6]], (0.06668857, qubits[14]));
            Controlled Ry([qubits[7]], (2.1189792, qubits[14]));
            Controlled Ry([qubits[8]], (2.1782705, qubits[14]));
            Controlled Ry([qubits[9]], (0.84003651, qubits[14]));
            Controlled Ry([qubits[10]], (0.86549387, qubits[14]));
            Controlled Ry([qubits[11]], (2.0566554, qubits[14]));
            Controlled Ry([qubits[12]], (0.28477526, qubits[14]));
            set c = SetBitValue(c, 0, ResultAsBool(M(qubits[13])));
            set c = SetBitValue(c, 1, ResultAsBool(M(qubits[14])));
            ResetAll(qubits);
        }
        return (c);
    }
}
