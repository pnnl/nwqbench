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
        using(qubits = Qubit[3]) {
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            CNOT(qubits[0], qubits[1]);
            Rz(0.42211821, qubits[1]);
            CNOT(qubits[0], qubits[1]);
            CNOT(qubits[1], qubits[2]);
            Rz(1.9338127, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[1], qubits[2]);
            Rz(1.3191528, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            CNOT(qubits[0], qubits[1]);
            Rz(0.045029159, qubits[2]);
            Rz(1.4449089, qubits[1]);
            H(qubits[2]);
            CNOT(qubits[0], qubits[1]);
            Rz(2.8656361, qubits[0]);
            Rz(1.8271938, qubits[1]);
            H(qubits[0]);
            H(qubits[1]);
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            ResetAll(qubits);
        }
        return (c0, meas);
    }
}
