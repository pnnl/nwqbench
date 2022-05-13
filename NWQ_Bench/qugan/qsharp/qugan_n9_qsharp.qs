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
    
    operation Circuit(): (Int) {
mutable c0 = 0;
using(qubits = Qubit[9]) {
u2(0.0, PI(), qubits[0]);
Rx(PI() / 2.0, qubits[1]);
Rx(PI() / 2.0, qubits[2]);
Rx(PI() / 2.0, qubits[3]);
Rx(PI() / 2.0, qubits[4]);
Rx(PI() / 2.0, qubits[5]);
Rx(PI() / 2.0, qubits[6]);
Rx(PI() / 2.0, qubits[7]);
Rx(PI() / 2.0, qubits[8]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[5], qubits[6]);
Rz(1.724517, qubits[2]);
Rz(0.91774004, qubits[6]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[5], qubits[6]);
Rx(-PI() / 2.0, qubits[1]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[5]);
Rx(-PI() / 2.0, qubits[6]);
u3(1.4866231, 0.0, 0.0, qubits[2]);
u3(1.0598507, 0.0, 0.0, qubits[6]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[5], qubits[6]);
u3(-1.4866231, 0.0, 0.0, qubits[2]);
u3(-1.0598507, 0.0, 0.0, qubits[6]);
CNOT(qubits[1], qubits[2]);
CNOT(qubits[5], qubits[6]);
Rx(PI() / 2.0, qubits[2]);
Rx(PI() / 2.0, qubits[6]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[6], qubits[7]);
Rz(3.0154695, qubits[3]);
Rz(0.29075759, qubits[7]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[6], qubits[7]);
Rx(-PI() / 2.0, qubits[2]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[6]);
Rx(-PI() / 2.0, qubits[7]);
u3(1.0993885, 0.0, 0.0, qubits[3]);
u3(0.97412798, 0.0, 0.0, qubits[7]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[6], qubits[7]);
u3(-1.0993885, 0.0, 0.0, qubits[3]);
u3(-0.97412798, 0.0, 0.0, qubits[7]);
CNOT(qubits[2], qubits[3]);
CNOT(qubits[6], qubits[7]);
Rx(PI() / 2.0, qubits[3]);
Rx(PI() / 2.0, qubits[7]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[7], qubits[8]);
Rz(2.8434888, qubits[4]);
Rz(2.3712238, qubits[8]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[7], qubits[8]);
Rx(-PI() / 2.0, qubits[3]);
Rx(-PI() / 2.0, qubits[4]);
Rx(-PI() / 2.0, qubits[7]);
Rx(-PI() / 2.0, qubits[8]);
u3(0.26495473, 0.0, 0.0, qubits[4]);
u3(1.0987503, 0.0, 0.0, qubits[8]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[7], qubits[8]);
u3(-0.26495473, 0.0, 0.0, qubits[4]);
u3(-1.0987503, 0.0, 0.0, qubits[8]);
CNOT(qubits[3], qubits[4]);
CNOT(qubits[7], qubits[8]);
CNOT(qubits[5], qubits[1]);
CCNOT(qubits[0], qubits[1], qubits[5]);
CNOT(qubits[5], qubits[1]);
CNOT(qubits[6], qubits[2]);
CCNOT(qubits[0], qubits[2], qubits[6]);
CNOT(qubits[6], qubits[2]);
CNOT(qubits[7], qubits[3]);
CCNOT(qubits[0], qubits[3], qubits[7]);
CNOT(qubits[7], qubits[3]);
CNOT(qubits[8], qubits[4]);
CCNOT(qubits[0], qubits[4], qubits[8]);
u2(0.0, PI(), qubits[0]);
CNOT(qubits[8], qubits[4]);
set c0 = SetBitValue(c0, 0, ResultAsBool(M(qubits[5])));
set c0 = SetBitValue(c0, 1, ResultAsBool(M(qubits[6])));
set c0 = SetBitValue(c0, 2, ResultAsBool(M(qubits[7])));
set c0 = SetBitValue(c0, 3, ResultAsBool(M(qubits[8])));
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
}
return (c0);
}
}
ResetAll(qubits);
        }
        return (c0);
    }
}
