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
        mutable c0 = 0;
        mutable meas = 0;
        using(qubits = Qubit[9]) {
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            H(qubits[5]);
            H(qubits[6]);
            H(qubits[7]);
            H(qubits[8]);
            CNOT(qubits[0], qubits[1]);
            Rz(2.8311259, qubits[1]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[1], qubits[2]);
            Rz(1.2265915, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[2], qubits[3]);
            Rz(1.479296, qubits[3]);
            CNOT(qubits[2], qubits[3]);
            CNOT(qubits[3], qubits[4]);
            Rz(2.9514659, qubits[4]);
            CNOT(qubits[3], qubits[4]);
            CNOT(qubits[4], qubits[5]);
            Rz(2.3882589, qubits[5]);
            CNOT(qubits[4], qubits[5]);
            CNOT(qubits[5], qubits[6]);
            Rz(1.1734905, qubits[6]);
            CNOT(qubits[5], qubits[6]);
            CNOT(qubits[6], qubits[7]);
            Rz(2.2581292, qubits[7]);
            CNOT(qubits[6], qubits[7]);
            CNOT(qubits[7], qubits[8]);
            Rz(1.1319911, qubits[8]);
            CNOT(qubits[7], qubits[8]);
            CNOT(qubits[7], qubits[8]);
            Rz(2.1029369, qubits[8]);
            CNOT(qubits[7], qubits[8]);
            CNOT(qubits[6], qubits[7]);
            Rz(2.6862292, qubits[8]);
            Rz(2.8882597, qubits[7]);
            H(qubits[8]);
            CNOT(qubits[6], qubits[7]);
            CNOT(qubits[5], qubits[6]);
            Rz(2.6511854, qubits[7]);
            Rz(1.0268664, qubits[6]);
            H(qubits[7]);
            CNOT(qubits[5], qubits[6]);
            CNOT(qubits[4], qubits[5]);
            Rz(0.76967459, qubits[6]);
            Rz(0.55298471, qubits[5]);
            H(qubits[6]);
            CNOT(qubits[4], qubits[5]);
            CNOT(qubits[3], qubits[4]);
            Rz(2.4446613, qubits[5]);
            Rz(0.90856313, qubits[4]);
            H(qubits[5]);
            CNOT(qubits[3], qubits[4]);
            CNOT(qubits[2], qubits[3]);
            Rz(1.9013246, qubits[4]);
            Rz(2.9827742, qubits[3]);
            H(qubits[4]);
            CNOT(qubits[2], qubits[3]);
            CNOT(qubits[1], qubits[2]);
            Rz(0.014797547, qubits[3]);
            Rz(0.19787971, qubits[2]);
            H(qubits[3]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[1]);
            Rz(0.85822507, qubits[2]);
            Rz(0.22373175, qubits[1]);
            H(qubits[2]);
            CNOT(qubits[0], qubits[1]);
            Rz(0.0041994242, qubits[0]);
            Rz(2.9933554, qubits[1]);
            H(qubits[0]);
            H(qubits[1]);
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            set meas = SetBitValue(meas, 3, ResultAsBool(M(qubits[3])));
            set meas = SetBitValue(meas, 4, ResultAsBool(M(qubits[4])));
            set meas = SetBitValue(meas, 5, ResultAsBool(M(qubits[5])));
            set meas = SetBitValue(meas, 6, ResultAsBool(M(qubits[6])));
            set meas = SetBitValue(meas, 7, ResultAsBool(M(qubits[7])));
            set meas = SetBitValue(meas, 8, ResultAsBool(M(qubits[8])));
            ResetAll(qubits);
        }
        return (c0, meas);
    }
}
