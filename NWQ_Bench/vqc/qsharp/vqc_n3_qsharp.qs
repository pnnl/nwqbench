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
    
    operation Circuit(): (Int, Int) {
mutable c0 = 0;
mutable meas = 0;
using(qubits = Qubit[3]) {
H(qubits[0]);
H(qubits[1]);
H(qubits[2]);
Rz(0.84751467, qubits[0]);
Rz(1.3067611, qubits[1]);
Rz(2.5281551, qubits[2]);
CNOT(qubits[0], qubits[1]);
Rz(2.012692, qubits[1]);
CNOT(qubits[0], qubits[1]);
Ry(1.3211686, qubits[0]);
CNOT(qubits[1], qubits[2]);
Rz(1.0058728, qubits[0]);
Rz(3.1257781, qubits[2]);
CNOT(qubits[1], qubits[2]);
Ry(2.2279618, qubits[1]);
Ry(0.33699867, qubits[2]);
Rz(1.2746996, qubits[1]);
Rz(1.0712587, qubits[2]);
Controlled Z([qubits[0]], (qubits[1]));
Controlled Z([qubits[0]], (qubits[2]));
Ry(2.2934377, qubits[0]);
Controlled Z([qubits[1]], (qubits[2]));
Rz(1.4841367, qubits[0]);
Ry(1.9225664, qubits[1]);
Ry(1.7857658, qubits[2]);
Rz(2.4225378, qubits[1]);
Rz(1.3689008, qubits[2]);
Controlled Z([qubits[0]], (qubits[1]));
Controlled Z([qubits[0]], (qubits[2]));
Ry(0.59639646, qubits[0]);
Controlled Z([qubits[1]], (qubits[2]));
Rz(1.2541083, qubits[0]);
Ry(2.2665371, qubits[1]);
Ry(0.026092831, qubits[2]);
Rz(2.4037987, qubits[1]);
Rz(1.8096955, qubits[2]);
Controlled Z([qubits[0]], (qubits[1]));
Controlled Z([qubits[0]], (qubits[2]));
Ry(0.24001234, qubits[0]);
Controlled Z([qubits[1]], (qubits[2]));
Rz(2.484556, qubits[0]);
Ry(2.4622526, qubits[1]);
Ry(1.9069715, qubits[2]);
Rz(0.444765, qubits[1]);
Rz(1.099548, qubits[2]);
Controlled Z([qubits[0]], (qubits[1]));
Controlled Z([qubits[0]], (qubits[2]));
Controlled Z([qubits[1]], (qubits[2]));
set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
}
return (c0, meas);
}
}
ResetAll(qubits);
        }
        return (c0, meas);
    }
}
