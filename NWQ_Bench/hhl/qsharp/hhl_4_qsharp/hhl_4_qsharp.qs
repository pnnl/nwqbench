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
        using(qubits = Qubit[4]) {
            Rz(PI() / 4.0, qubits[0]);
            Rx(-0.054932672, qubits[1]);
            Rx(-0.054932672, qubits[2]);
            Ry(1.217116, qubits[3]);
            Ry(PI(), qubits[0]);
            Ry(-PI() / 2.0, qubits[1]);
            Ry(-PI() / 2.0, qubits[2]);
            Rz(-PI() / 4.0, qubits[0]);
            CNOT(qubits[1], qubits[0]);
            Rz(0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-PI(), qubits[0]);
            CNOT(qubits[1], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-2.5153524, qubits[1]);
            Rz(3.08666, qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Rz(0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-PI(), qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(3.08666, qubits[2]);
            Rz(3.08666, qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Rz(0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-PI(), qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-0.3183159, qubits[2]);
            Rz(6.2282526, qubits[0]);
            Ry(PI() / 2.0, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            Rz(PI() / 4.0, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            H(qubits[1]);
            Rz(-PI() / 4.0, qubits[2]);
            CNOT(qubits[2], qubits[3]);
            Ry(-0.69351723, qubits[3]);
            CNOT(qubits[1], qubits[3]);
            Ry(-0.8772791, qubits[3]);
            CNOT(qubits[2], qubits[3]);
            Ry(0.35368032, qubits[3]);
            CNOT(qubits[1], qubits[3]);
            Rx(-3.0 * PI() / 4.0, qubits[1]);
            Ry(-PI() / 2.0, qubits[1]);
            CNOT(qubits[1], qubits[2]);
            Rz(-PI() / 4.0, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            Rz(-3.08666, qubits[1]);
            Rz(-3.0 * PI() / 4.0, qubits[2]);
            Ry(PI() / 2.0, qubits[2]);
            Rz(3.1965253, qubits[2]);
            CNOT(qubits[2], qubits[0]);
            Rz(-0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(PI(), qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-3.08666, qubits[2]);
            Rz(-3.08666, qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Rz(-0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(PI(), qubits[0]);
            CNOT(qubits[2], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(-5.9648694, qubits[2]);
            Rz(-3.08666, qubits[0]);
            Ry(PI() / 2.0, qubits[2]);
            CNOT(qubits[1], qubits[0]);
            Rz(-0.054932672, qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(PI(), qubits[0]);
            CNOT(qubits[1], qubits[0]);
            Ry(0.20702763, qubits[0]);
            Rz(4.8715469, qubits[1]);
            Rz(-4.6574563, qubits[0]);
            Ry(PI() / 2.0, qubits[1]);
            set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[0])));
            ResetAll(qubits);
        }
        return (c0);
    }
}
