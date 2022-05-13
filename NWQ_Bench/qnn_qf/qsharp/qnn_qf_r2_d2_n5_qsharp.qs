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
mutable c = 0;
using(qubits = Qubit[5]) {
Ry(0.74112722, qubits[0]);
Ry(1.1897021, qubits[1]);
Ry(1.6820708, qubits[2]);
Controlled Ry([qubits[0]], (0.95224137, qubits[1]));
Controlled Ry([qubits[1]], (0.68008628, qubits[2]));
Controlled Ry([qubits[2]], (1.9511137, qubits[0]));
Ry(0.75913465, qubits[0]);
Ry(2.0517674, qubits[1]);
Ry(2.3983248, qubits[2]);
Controlled Ry([qubits[0]], (1.3839028, qubits[1]));
Controlled Ry([qubits[1]], (2.7005981, qubits[2]));
Controlled Ry([qubits[2]], (1.1385292, qubits[0]));
Ry(2.3976709, qubits[0]);
Ry(1.7424099, qubits[1]);
Ry(2.352948, qubits[2]);
Controlled Ry([qubits[0]], (3.0359317, qubits[3]));
Controlled Ry([qubits[1]], (2.5548187, qubits[3]));
Controlled Ry([qubits[2]], (0.52892069, qubits[3]));
Controlled Ry([qubits[0]], (2.9779363, qubits[4]));
Controlled Ry([qubits[1]], (0.52004459, qubits[4]));
Controlled Ry([qubits[2]], (0.22143418, qubits[4]));
set c = SetBitValue(c, 0, ResultAsBool(M(qubits[3])));
set c = SetBitValue(c, 1, ResultAsBool(M(qubits[4])));
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
}
return (c);
}
}
ResetAll(qubits);
        }
        return (c);
    }
}
