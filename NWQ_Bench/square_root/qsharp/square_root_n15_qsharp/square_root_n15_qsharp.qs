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
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            Reset(qubits[11]);
            Reset(qubits[12]);
            Reset(qubits[13]);
            Reset(qubits[14]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[7]);
            CNOT(qubits[2], qubits[9]);
            CNOT(qubits[3], qubits[6]);
            CNOT(qubits[3], qubits[7]);
            CNOT(qubits[4], qubits[8]);
            CNOT(qubits[4], qubits[9]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            Reset(qubits[12]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            Reset(qubits[11]);
            CNOT(qubits[0], qubits[5]);
            H(qubits[0]);
            CNOT(qubits[1], qubits[7]);
            X(qubits[0]);
            H(qubits[1]);
            CNOT(qubits[2], qubits[9]);
            X(qubits[1]);
            H(qubits[2]);
            CNOT(qubits[3], qubits[6]);
            X(qubits[2]);
            CNOT(qubits[3], qubits[7]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[8]);
            X(qubits[3]);
            CNOT(qubits[4], qubits[9]);
            H(qubits[4]);
            X(qubits[4]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            Reset(qubits[12]);
            X(qubits[0]);
            X(qubits[1]);
            X(qubits[2]);
            X(qubits[3]);
            X(qubits[4]);
            Reset(qubits[11]);
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[7]);
            CNOT(qubits[2], qubits[9]);
            CNOT(qubits[3], qubits[6]);
            CNOT(qubits[3], qubits[7]);
            CNOT(qubits[4], qubits[8]);
            CNOT(qubits[4], qubits[9]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            Reset(qubits[12]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            Reset(qubits[11]);
            CNOT(qubits[0], qubits[5]);
            H(qubits[0]);
            CNOT(qubits[1], qubits[7]);
            X(qubits[0]);
            H(qubits[1]);
            CNOT(qubits[2], qubits[9]);
            X(qubits[1]);
            H(qubits[2]);
            CNOT(qubits[3], qubits[6]);
            X(qubits[2]);
            CNOT(qubits[3], qubits[7]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[8]);
            X(qubits[3]);
            CNOT(qubits[4], qubits[9]);
            H(qubits[4]);
            X(qubits[4]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            Reset(qubits[12]);
            X(qubits[0]);
            X(qubits[1]);
            X(qubits[2]);
            X(qubits[3]);
            X(qubits[4]);
            Reset(qubits[11]);
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[7]);
            CNOT(qubits[2], qubits[9]);
            CNOT(qubits[3], qubits[6]);
            CNOT(qubits[3], qubits[7]);
            CNOT(qubits[4], qubits[8]);
            CNOT(qubits[4], qubits[9]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            Reset(qubits[12]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            Reset(qubits[11]);
            CNOT(qubits[0], qubits[5]);
            H(qubits[0]);
            CNOT(qubits[1], qubits[7]);
            X(qubits[0]);
            H(qubits[1]);
            CNOT(qubits[2], qubits[9]);
            X(qubits[1]);
            H(qubits[2]);
            CNOT(qubits[3], qubits[6]);
            X(qubits[2]);
            CNOT(qubits[3], qubits[7]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[8]);
            X(qubits[3]);
            CNOT(qubits[4], qubits[9]);
            H(qubits[4]);
            X(qubits[4]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            Reset(qubits[12]);
            X(qubits[0]);
            X(qubits[1]);
            X(qubits[2]);
            X(qubits[3]);
            X(qubits[4]);
            Reset(qubits[11]);
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[7]);
            CNOT(qubits[2], qubits[9]);
            CNOT(qubits[3], qubits[6]);
            CNOT(qubits[3], qubits[7]);
            CNOT(qubits[4], qubits[8]);
            CNOT(qubits[4], qubits[9]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            Reset(qubits[12]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            Reset(qubits[11]);
            CNOT(qubits[0], qubits[5]);
            H(qubits[0]);
            CNOT(qubits[1], qubits[7]);
            X(qubits[0]);
            H(qubits[1]);
            CNOT(qubits[2], qubits[9]);
            X(qubits[1]);
            H(qubits[2]);
            CNOT(qubits[3], qubits[6]);
            X(qubits[2]);
            CNOT(qubits[3], qubits[7]);
            H(qubits[3]);
            CNOT(qubits[4], qubits[8]);
            X(qubits[3]);
            CNOT(qubits[4], qubits[9]);
            H(qubits[4]);
            X(qubits[4]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            Z(qubits[14]);
            CCNOT(qubits[13], qubits[4], qubits[14]);
            CCNOT(qubits[12], qubits[3], qubits[13]);
            Reset(qubits[14]);
            CCNOT(qubits[11], qubits[2], qubits[12]);
            Reset(qubits[13]);
            CCNOT(qubits[1], qubits[0], qubits[11]);
            Reset(qubits[12]);
            X(qubits[0]);
            X(qubits[1]);
            X(qubits[2]);
            X(qubits[3]);
            X(qubits[4]);
            Reset(qubits[11]);
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            CNOT(qubits[0], qubits[5]);
            CNOT(qubits[1], qubits[7]);
            CNOT(qubits[2], qubits[9]);
            CNOT(qubits[3], qubits[6]);
            CNOT(qubits[3], qubits[7]);
            CNOT(qubits[4], qubits[8]);
            CNOT(qubits[4], qubits[9]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CNOT(qubits[14], qubits[10]);
            CCNOT(qubits[13], qubits[9], qubits[14]);
            CCNOT(qubits[12], qubits[8], qubits[13]);
            CCNOT(qubits[11], qubits[7], qubits[12]);
            CCNOT(qubits[6], qubits[5], qubits[11]);
            X(qubits[5]);
            X(qubits[7]);
            X(qubits[8]);
            X(qubits[9]);
            set c = SetBitValue(c, 10, ResultAsBool(M(qubits[10])));
            set c = SetBitValue(c, 0, ResultAsBool(M(qubits[0])));
            set c = SetBitValue(c, 1, ResultAsBool(M(qubits[1])));
            set c = SetBitValue(c, 2, ResultAsBool(M(qubits[2])));
            set c = SetBitValue(c, 3, ResultAsBool(M(qubits[3])));
            set c = SetBitValue(c, 4, ResultAsBool(M(qubits[4])));
            set c = SetBitValue(c, 5, ResultAsBool(M(qubits[5])));
            set c = SetBitValue(c, 6, ResultAsBool(M(qubits[6])));
            set c = SetBitValue(c, 7, ResultAsBool(M(qubits[7])));
            set c = SetBitValue(c, 8, ResultAsBool(M(qubits[8])));
            set c = SetBitValue(c, 9, ResultAsBool(M(qubits[9])));
            ResetAll(qubits);
        }
        return (c);
    }
}