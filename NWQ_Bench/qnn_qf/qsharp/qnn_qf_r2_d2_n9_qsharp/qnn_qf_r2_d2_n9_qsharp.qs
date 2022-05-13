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
        using(qubits = Qubit[9]) {
            Ry(3.0199575, qubits[0]);
            Ry(0.6849634, qubits[1]);
            Ry(0.19966078, qubits[2]);
            Ry(2.4255556, qubits[3]);
            Ry(0.17965019, qubits[4]);
            Ry(0.21137635, qubits[5]);
            Ry(2.1169674, qubits[6]);
            Controlled Ry([qubits[0]], (0.81479306, qubits[1]));
            Controlled Ry([qubits[1]], (1.0362017, qubits[2]));
            Controlled Ry([qubits[2]], (0.95144891, qubits[3]));
            Controlled Ry([qubits[3]], (0.37686864, qubits[4]));
            Controlled Ry([qubits[4]], (0.59838775, qubits[5]));
            Controlled Ry([qubits[5]], (1.8460888, qubits[6]));
            Controlled Ry([qubits[6]], (0.10341369, qubits[0]));
            Ry(1.0081277, qubits[0]);
            Ry(1.8153793, qubits[1]);
            Ry(0.60519057, qubits[2]);
            Ry(2.9301845, qubits[3]);
            Ry(2.2280573, qubits[4]);
            Ry(2.5004374, qubits[5]);
            Ry(1.5186301, qubits[6]);
            Controlled Ry([qubits[0]], (2.516851, qubits[1]));
            Controlled Ry([qubits[1]], (2.9520785, qubits[2]));
            Controlled Ry([qubits[2]], (1.8930492, qubits[3]));
            Controlled Ry([qubits[3]], (2.7177606, qubits[4]));
            Controlled Ry([qubits[4]], (2.4212721, qubits[5]));
            Controlled Ry([qubits[5]], (0.45559183, qubits[6]));
            Controlled Ry([qubits[6]], (0.25042298, qubits[0]));
            Ry(2.9043619, qubits[0]);
            Ry(0.66974428, qubits[1]);
            Ry(2.753528, qubits[2]);
            Ry(0.23933046, qubits[3]);
            Ry(0.46614657, qubits[4]);
            Ry(0.0071772368, qubits[5]);
            Ry(3.0222646, qubits[6]);
            Controlled Ry([qubits[0]], (2.933675, qubits[7]));
            Controlled Ry([qubits[1]], (0.29781348, qubits[7]));
            Controlled Ry([qubits[2]], (1.0732682, qubits[7]));
            Controlled Ry([qubits[3]], (0.99333707, qubits[7]));
            Controlled Ry([qubits[4]], (2.2163495, qubits[7]));
            Controlled Ry([qubits[5]], (0.041894959, qubits[7]));
            Controlled Ry([qubits[6]], (0.20076766, qubits[7]));
            Controlled Ry([qubits[0]], (0.92724922, qubits[8]));
            Controlled Ry([qubits[1]], (0.69812999, qubits[8]));
            Controlled Ry([qubits[2]], (0.12907076, qubits[8]));
            Controlled Ry([qubits[3]], (0.079440692, qubits[8]));
            Controlled Ry([qubits[4]], (0.42589212, qubits[8]));
            Controlled Ry([qubits[5]], (0.65326438, qubits[8]));
            Controlled Ry([qubits[6]], (1.726853, qubits[8]));
            set c = SetBitValue(c, 0, ResultAsBool(M(qubits[7])));
            set c = SetBitValue(c, 1, ResultAsBool(M(qubits[8])));
            ResetAll(qubits);
        }
        return (c);
    }
}
