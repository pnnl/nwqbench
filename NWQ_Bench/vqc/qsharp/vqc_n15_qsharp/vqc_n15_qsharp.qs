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
        using(qubits = Qubit[15]) {
            H(qubits[0]);
            H(qubits[1]);
            H(qubits[2]);
            H(qubits[3]);
            H(qubits[4]);
            H(qubits[5]);
            H(qubits[6]);
            H(qubits[7]);
            H(qubits[8]);
            H(qubits[9]);
            H(qubits[10]);
            H(qubits[11]);
            H(qubits[12]);
            H(qubits[13]);
            H(qubits[14]);
            Rz(2.5156157, qubits[0]);
            Rz(1.5082091, qubits[1]);
            Rz(1.5673957, qubits[2]);
            Rz(2.1229745, qubits[3]);
            Rz(2.4282431, qubits[4]);
            Rz(2.0779625, qubits[5]);
            Rz(2.7516676, qubits[6]);
            Rz(1.3732694, qubits[7]);
            Rz(2.2789478, qubits[8]);
            Rz(0.063588782, qubits[9]);
            Rz(0.17360377, qubits[10]);
            Rz(0.63328891, qubits[11]);
            Rz(0.89650897, qubits[12]);
            Rz(1.8402197, qubits[13]);
            Rz(0.22125055, qubits[14]);
            CNOT(qubits[0], qubits[1]);
            Rz(3.0443277, qubits[1]);
            CNOT(qubits[0], qubits[1]);
            Ry(0.12547023, qubits[0]);
            CNOT(qubits[1], qubits[2]);
            Rz(1.1420902, qubits[0]);
            Rz(1.4957737, qubits[2]);
            CNOT(qubits[1], qubits[2]);
            Ry(1.9749875, qubits[1]);
            CNOT(qubits[2], qubits[3]);
            Rz(1.918538, qubits[1]);
            Rz(0.060112245, qubits[3]);
            Controlled Z([qubits[0]], (qubits[1]));
            CNOT(qubits[2], qubits[3]);
            Ry(0.79520536, qubits[2]);
            CNOT(qubits[3], qubits[4]);
            Rz(0.93406507, qubits[2]);
            Rz(2.7879005, qubits[4]);
            Controlled Z([qubits[0]], (qubits[2]));
            CNOT(qubits[3], qubits[4]);
            Ry(2.8543398, qubits[3]);
            CNOT(qubits[4], qubits[5]);
            Rz(0.90663008, qubits[3]);
            Rz(2.0461857, qubits[5]);
            Controlled Z([qubits[0]], (qubits[3]));
            CNOT(qubits[4], qubits[5]);
            Ry(2.4197477, qubits[4]);
            CNOT(qubits[5], qubits[6]);
            Rz(1.72238, qubits[4]);
            Rz(1.946018, qubits[6]);
            Controlled Z([qubits[0]], (qubits[4]));
            CNOT(qubits[5], qubits[6]);
            Ry(0.34591488, qubits[5]);
            CNOT(qubits[6], qubits[7]);
            Rz(1.618326, qubits[5]);
            Rz(0.1583611, qubits[7]);
            Controlled Z([qubits[0]], (qubits[5]));
            CNOT(qubits[6], qubits[7]);
            Ry(0.83644293, qubits[6]);
            CNOT(qubits[7], qubits[8]);
            Rz(0.31072556, qubits[6]);
            Rz(2.2356786, qubits[8]);
            Controlled Z([qubits[0]], (qubits[6]));
            CNOT(qubits[7], qubits[8]);
            Ry(0.24167335, qubits[7]);
            CNOT(qubits[8], qubits[9]);
            Rz(0.98390069, qubits[7]);
            Rz(0.72466613, qubits[9]);
            Controlled Z([qubits[0]], (qubits[7]));
            CNOT(qubits[8], qubits[9]);
            Ry(1.0646688, qubits[8]);
            CNOT(qubits[9], qubits[10]);
            Rz(2.5930644, qubits[8]);
            Rz(0.66903133, qubits[10]);
            Controlled Z([qubits[0]], (qubits[8]));
            CNOT(qubits[9], qubits[10]);
            Ry(1.9237841, qubits[9]);
            CNOT(qubits[10], qubits[11]);
            Rz(0.22652569, qubits[9]);
            Rz(1.2695865, qubits[11]);
            Controlled Z([qubits[0]], (qubits[9]));
            CNOT(qubits[10], qubits[11]);
            Ry(1.1596208, qubits[10]);
            CNOT(qubits[11], qubits[12]);
            Rz(0.41487776, qubits[10]);
            Rz(1.2646738, qubits[12]);
            Controlled Z([qubits[0]], (qubits[10]));
            CNOT(qubits[11], qubits[12]);
            Ry(1.2702462, qubits[11]);
            CNOT(qubits[12], qubits[13]);
            Rz(2.7844251, qubits[11]);
            Rz(2.9009257, qubits[13]);
            Controlled Z([qubits[0]], (qubits[11]));
            CNOT(qubits[12], qubits[13]);
            Ry(1.2423356, qubits[12]);
            CNOT(qubits[13], qubits[14]);
            Rz(0.72405126, qubits[12]);
            Rz(1.6273523, qubits[14]);
            Controlled Z([qubits[0]], (qubits[12]));
            CNOT(qubits[13], qubits[14]);
            Ry(2.0233533, qubits[13]);
            Ry(3.0869493, qubits[14]);
            Rz(0.77422169, qubits[13]);
            Rz(0.16468555, qubits[14]);
            Controlled Z([qubits[0]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[14]));
            Ry(1.1535852, qubits[0]);
            Controlled Z([qubits[1]], (qubits[2]));
            Rz(0.12828756, qubits[0]);
            Controlled Z([qubits[1]], (qubits[3]));
            Controlled Z([qubits[1]], (qubits[4]));
            Controlled Z([qubits[1]], (qubits[5]));
            Controlled Z([qubits[1]], (qubits[6]));
            Controlled Z([qubits[1]], (qubits[7]));
            Controlled Z([qubits[1]], (qubits[8]));
            Controlled Z([qubits[1]], (qubits[9]));
            Controlled Z([qubits[1]], (qubits[10]));
            Controlled Z([qubits[1]], (qubits[11]));
            Controlled Z([qubits[1]], (qubits[12]));
            Controlled Z([qubits[1]], (qubits[13]));
            Controlled Z([qubits[1]], (qubits[14]));
            Ry(2.431352, qubits[1]);
            Controlled Z([qubits[2]], (qubits[3]));
            Rz(1.6938178, qubits[1]);
            Controlled Z([qubits[2]], (qubits[4]));
            Controlled Z([qubits[0]], (qubits[1]));
            Controlled Z([qubits[2]], (qubits[5]));
            Controlled Z([qubits[2]], (qubits[6]));
            Controlled Z([qubits[2]], (qubits[7]));
            Controlled Z([qubits[2]], (qubits[8]));
            Controlled Z([qubits[2]], (qubits[9]));
            Controlled Z([qubits[2]], (qubits[10]));
            Controlled Z([qubits[2]], (qubits[11]));
            Controlled Z([qubits[2]], (qubits[12]));
            Controlled Z([qubits[2]], (qubits[13]));
            Controlled Z([qubits[2]], (qubits[14]));
            Ry(2.161469, qubits[2]);
            Controlled Z([qubits[3]], (qubits[4]));
            Rz(2.1198771, qubits[2]);
            Controlled Z([qubits[3]], (qubits[5]));
            Controlled Z([qubits[0]], (qubits[2]));
            Controlled Z([qubits[3]], (qubits[6]));
            Controlled Z([qubits[3]], (qubits[7]));
            Controlled Z([qubits[3]], (qubits[8]));
            Controlled Z([qubits[3]], (qubits[9]));
            Controlled Z([qubits[3]], (qubits[10]));
            Controlled Z([qubits[3]], (qubits[11]));
            Controlled Z([qubits[3]], (qubits[12]));
            Controlled Z([qubits[3]], (qubits[13]));
            Controlled Z([qubits[3]], (qubits[14]));
            Ry(1.429698, qubits[3]);
            Controlled Z([qubits[4]], (qubits[5]));
            Rz(2.1545361, qubits[3]);
            Controlled Z([qubits[4]], (qubits[6]));
            Controlled Z([qubits[0]], (qubits[3]));
            Controlled Z([qubits[4]], (qubits[7]));
            Controlled Z([qubits[4]], (qubits[8]));
            Controlled Z([qubits[4]], (qubits[9]));
            Controlled Z([qubits[4]], (qubits[10]));
            Controlled Z([qubits[4]], (qubits[11]));
            Controlled Z([qubits[4]], (qubits[12]));
            Controlled Z([qubits[4]], (qubits[13]));
            Controlled Z([qubits[4]], (qubits[14]));
            Ry(1.9278428, qubits[4]);
            Controlled Z([qubits[5]], (qubits[6]));
            Rz(2.522728, qubits[4]);
            Controlled Z([qubits[5]], (qubits[7]));
            Controlled Z([qubits[0]], (qubits[4]));
            Controlled Z([qubits[5]], (qubits[8]));
            Controlled Z([qubits[5]], (qubits[9]));
            Controlled Z([qubits[5]], (qubits[10]));
            Controlled Z([qubits[5]], (qubits[11]));
            Controlled Z([qubits[5]], (qubits[12]));
            Controlled Z([qubits[5]], (qubits[13]));
            Controlled Z([qubits[5]], (qubits[14]));
            Ry(0.58897152, qubits[5]);
            Controlled Z([qubits[6]], (qubits[7]));
            Rz(0.8574871, qubits[5]);
            Controlled Z([qubits[6]], (qubits[8]));
            Controlled Z([qubits[0]], (qubits[5]));
            Controlled Z([qubits[6]], (qubits[9]));
            Controlled Z([qubits[6]], (qubits[10]));
            Controlled Z([qubits[6]], (qubits[11]));
            Controlled Z([qubits[6]], (qubits[12]));
            Controlled Z([qubits[6]], (qubits[13]));
            Controlled Z([qubits[6]], (qubits[14]));
            Ry(0.073603173, qubits[6]);
            Controlled Z([qubits[7]], (qubits[8]));
            Rz(3.0145944, qubits[6]);
            Controlled Z([qubits[7]], (qubits[9]));
            Controlled Z([qubits[0]], (qubits[6]));
            Controlled Z([qubits[7]], (qubits[10]));
            Controlled Z([qubits[7]], (qubits[11]));
            Controlled Z([qubits[7]], (qubits[12]));
            Controlled Z([qubits[7]], (qubits[13]));
            Controlled Z([qubits[7]], (qubits[14]));
            Ry(2.1583193, qubits[7]);
            Controlled Z([qubits[8]], (qubits[9]));
            Rz(1.3788067, qubits[7]);
            Controlled Z([qubits[8]], (qubits[10]));
            Controlled Z([qubits[0]], (qubits[7]));
            Controlled Z([qubits[8]], (qubits[11]));
            Controlled Z([qubits[8]], (qubits[12]));
            Controlled Z([qubits[8]], (qubits[13]));
            Controlled Z([qubits[8]], (qubits[14]));
            Ry(2.0972212, qubits[8]);
            Controlled Z([qubits[9]], (qubits[10]));
            Rz(2.1802834, qubits[8]);
            Controlled Z([qubits[9]], (qubits[11]));
            Controlled Z([qubits[0]], (qubits[8]));
            Controlled Z([qubits[9]], (qubits[12]));
            Controlled Z([qubits[9]], (qubits[13]));
            Controlled Z([qubits[9]], (qubits[14]));
            Ry(1.3961577, qubits[9]);
            Controlled Z([qubits[10]], (qubits[11]));
            Rz(0.96219182, qubits[9]);
            Controlled Z([qubits[10]], (qubits[12]));
            Controlled Z([qubits[0]], (qubits[9]));
            Controlled Z([qubits[10]], (qubits[13]));
            Controlled Z([qubits[10]], (qubits[14]));
            Ry(2.010101, qubits[10]);
            Controlled Z([qubits[11]], (qubits[12]));
            Rz(1.0068101, qubits[10]);
            Controlled Z([qubits[11]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[10]));
            Controlled Z([qubits[11]], (qubits[14]));
            Ry(1.1214107, qubits[11]);
            Controlled Z([qubits[12]], (qubits[13]));
            Rz(0.91526036, qubits[11]);
            Controlled Z([qubits[12]], (qubits[14]));
            Controlled Z([qubits[0]], (qubits[11]));
            Ry(2.938263, qubits[12]);
            Controlled Z([qubits[13]], (qubits[14]));
            Rz(3.0379128, qubits[12]);
            Ry(1.8889546, qubits[13]);
            Ry(0.88998615, qubits[14]);
            Controlled Z([qubits[0]], (qubits[12]));
            Rz(0.36787701, qubits[13]);
            Rz(1.6294565, qubits[14]);
            Controlled Z([qubits[0]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[14]));
            Ry(3.0653662, qubits[0]);
            Controlled Z([qubits[1]], (qubits[2]));
            Rz(2.8730933, qubits[0]);
            Controlled Z([qubits[1]], (qubits[3]));
            Controlled Z([qubits[1]], (qubits[4]));
            Controlled Z([qubits[1]], (qubits[5]));
            Controlled Z([qubits[1]], (qubits[6]));
            Controlled Z([qubits[1]], (qubits[7]));
            Controlled Z([qubits[1]], (qubits[8]));
            Controlled Z([qubits[1]], (qubits[9]));
            Controlled Z([qubits[1]], (qubits[10]));
            Controlled Z([qubits[1]], (qubits[11]));
            Controlled Z([qubits[1]], (qubits[12]));
            Controlled Z([qubits[1]], (qubits[13]));
            Controlled Z([qubits[1]], (qubits[14]));
            Ry(0.87957933, qubits[1]);
            Controlled Z([qubits[2]], (qubits[3]));
            Rz(2.3904406, qubits[1]);
            Controlled Z([qubits[2]], (qubits[4]));
            Controlled Z([qubits[0]], (qubits[1]));
            Controlled Z([qubits[2]], (qubits[5]));
            Controlled Z([qubits[2]], (qubits[6]));
            Controlled Z([qubits[2]], (qubits[7]));
            Controlled Z([qubits[2]], (qubits[8]));
            Controlled Z([qubits[2]], (qubits[9]));
            Controlled Z([qubits[2]], (qubits[10]));
            Controlled Z([qubits[2]], (qubits[11]));
            Controlled Z([qubits[2]], (qubits[12]));
            Controlled Z([qubits[2]], (qubits[13]));
            Controlled Z([qubits[2]], (qubits[14]));
            Ry(0.057136693, qubits[2]);
            Controlled Z([qubits[3]], (qubits[4]));
            Rz(0.76744179, qubits[2]);
            Controlled Z([qubits[3]], (qubits[5]));
            Controlled Z([qubits[0]], (qubits[2]));
            Controlled Z([qubits[3]], (qubits[6]));
            Controlled Z([qubits[3]], (qubits[7]));
            Controlled Z([qubits[3]], (qubits[8]));
            Controlled Z([qubits[3]], (qubits[9]));
            Controlled Z([qubits[3]], (qubits[10]));
            Controlled Z([qubits[3]], (qubits[11]));
            Controlled Z([qubits[3]], (qubits[12]));
            Controlled Z([qubits[3]], (qubits[13]));
            Controlled Z([qubits[3]], (qubits[14]));
            Ry(2.1754857, qubits[3]);
            Controlled Z([qubits[4]], (qubits[5]));
            Rz(0.33890995, qubits[3]);
            Controlled Z([qubits[4]], (qubits[6]));
            Controlled Z([qubits[0]], (qubits[3]));
            Controlled Z([qubits[4]], (qubits[7]));
            Controlled Z([qubits[4]], (qubits[8]));
            Controlled Z([qubits[4]], (qubits[9]));
            Controlled Z([qubits[4]], (qubits[10]));
            Controlled Z([qubits[4]], (qubits[11]));
            Controlled Z([qubits[4]], (qubits[12]));
            Controlled Z([qubits[4]], (qubits[13]));
            Controlled Z([qubits[4]], (qubits[14]));
            Ry(1.1348571, qubits[4]);
            Controlled Z([qubits[5]], (qubits[6]));
            Rz(1.9657683, qubits[4]);
            Controlled Z([qubits[5]], (qubits[7]));
            Controlled Z([qubits[0]], (qubits[4]));
            Controlled Z([qubits[5]], (qubits[8]));
            Controlled Z([qubits[5]], (qubits[9]));
            Controlled Z([qubits[5]], (qubits[10]));
            Controlled Z([qubits[5]], (qubits[11]));
            Controlled Z([qubits[5]], (qubits[12]));
            Controlled Z([qubits[5]], (qubits[13]));
            Controlled Z([qubits[5]], (qubits[14]));
            Ry(1.9834339, qubits[5]);
            Controlled Z([qubits[6]], (qubits[7]));
            Rz(3.0208973, qubits[5]);
            Controlled Z([qubits[6]], (qubits[8]));
            Controlled Z([qubits[0]], (qubits[5]));
            Controlled Z([qubits[6]], (qubits[9]));
            Controlled Z([qubits[6]], (qubits[10]));
            Controlled Z([qubits[6]], (qubits[11]));
            Controlled Z([qubits[6]], (qubits[12]));
            Controlled Z([qubits[6]], (qubits[13]));
            Controlled Z([qubits[6]], (qubits[14]));
            Ry(1.3962331, qubits[6]);
            Controlled Z([qubits[7]], (qubits[8]));
            Rz(1.07303, qubits[6]);
            Controlled Z([qubits[7]], (qubits[9]));
            Controlled Z([qubits[0]], (qubits[6]));
            Controlled Z([qubits[7]], (qubits[10]));
            Controlled Z([qubits[7]], (qubits[11]));
            Controlled Z([qubits[7]], (qubits[12]));
            Controlled Z([qubits[7]], (qubits[13]));
            Controlled Z([qubits[7]], (qubits[14]));
            Ry(0.36045754, qubits[7]);
            Controlled Z([qubits[8]], (qubits[9]));
            Rz(1.9970103, qubits[7]);
            Controlled Z([qubits[8]], (qubits[10]));
            Controlled Z([qubits[0]], (qubits[7]));
            Controlled Z([qubits[8]], (qubits[11]));
            Controlled Z([qubits[8]], (qubits[12]));
            Controlled Z([qubits[8]], (qubits[13]));
            Controlled Z([qubits[8]], (qubits[14]));
            Ry(1.3873164, qubits[8]);
            Controlled Z([qubits[9]], (qubits[10]));
            Rz(0.62152881, qubits[8]);
            Controlled Z([qubits[9]], (qubits[11]));
            Controlled Z([qubits[0]], (qubits[8]));
            Controlled Z([qubits[9]], (qubits[12]));
            Controlled Z([qubits[9]], (qubits[13]));
            Controlled Z([qubits[9]], (qubits[14]));
            Ry(2.5220023, qubits[9]);
            Controlled Z([qubits[10]], (qubits[11]));
            Rz(1.1280364, qubits[9]);
            Controlled Z([qubits[10]], (qubits[12]));
            Controlled Z([qubits[0]], (qubits[9]));
            Controlled Z([qubits[10]], (qubits[13]));
            Controlled Z([qubits[10]], (qubits[14]));
            Ry(2.8823555, qubits[10]);
            Controlled Z([qubits[11]], (qubits[12]));
            Rz(2.3800308, qubits[10]);
            Controlled Z([qubits[11]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[10]));
            Controlled Z([qubits[11]], (qubits[14]));
            Ry(1.4136561, qubits[11]);
            Controlled Z([qubits[12]], (qubits[13]));
            Rz(3.0036199, qubits[11]);
            Controlled Z([qubits[12]], (qubits[14]));
            Controlled Z([qubits[0]], (qubits[11]));
            Ry(1.2721718, qubits[12]);
            Controlled Z([qubits[13]], (qubits[14]));
            Rz(2.9194257, qubits[12]);
            Ry(0.13706241, qubits[13]);
            Ry(0.55852601, qubits[14]);
            Controlled Z([qubits[0]], (qubits[12]));
            Rz(2.5948465, qubits[13]);
            Rz(0.22056829, qubits[14]);
            Controlled Z([qubits[0]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[14]));
            Ry(1.135658, qubits[0]);
            Controlled Z([qubits[1]], (qubits[2]));
            Rz(0.50402741, qubits[0]);
            Controlled Z([qubits[1]], (qubits[3]));
            Controlled Z([qubits[1]], (qubits[4]));
            Controlled Z([qubits[1]], (qubits[5]));
            Controlled Z([qubits[1]], (qubits[6]));
            Controlled Z([qubits[1]], (qubits[7]));
            Controlled Z([qubits[1]], (qubits[8]));
            Controlled Z([qubits[1]], (qubits[9]));
            Controlled Z([qubits[1]], (qubits[10]));
            Controlled Z([qubits[1]], (qubits[11]));
            Controlled Z([qubits[1]], (qubits[12]));
            Controlled Z([qubits[1]], (qubits[13]));
            Controlled Z([qubits[1]], (qubits[14]));
            Ry(1.6670358, qubits[1]);
            Controlled Z([qubits[2]], (qubits[3]));
            Rz(0.059332798, qubits[1]);
            Controlled Z([qubits[2]], (qubits[4]));
            Controlled Z([qubits[0]], (qubits[1]));
            Controlled Z([qubits[2]], (qubits[5]));
            Controlled Z([qubits[2]], (qubits[6]));
            Controlled Z([qubits[2]], (qubits[7]));
            Controlled Z([qubits[2]], (qubits[8]));
            Controlled Z([qubits[2]], (qubits[9]));
            Controlled Z([qubits[2]], (qubits[10]));
            Controlled Z([qubits[2]], (qubits[11]));
            Controlled Z([qubits[2]], (qubits[12]));
            Controlled Z([qubits[2]], (qubits[13]));
            Controlled Z([qubits[2]], (qubits[14]));
            Ry(1.6216529, qubits[2]);
            Controlled Z([qubits[3]], (qubits[4]));
            Rz(2.0388228, qubits[2]);
            Controlled Z([qubits[3]], (qubits[5]));
            Controlled Z([qubits[0]], (qubits[2]));
            Controlled Z([qubits[3]], (qubits[6]));
            Controlled Z([qubits[3]], (qubits[7]));
            Controlled Z([qubits[3]], (qubits[8]));
            Controlled Z([qubits[3]], (qubits[9]));
            Controlled Z([qubits[3]], (qubits[10]));
            Controlled Z([qubits[3]], (qubits[11]));
            Controlled Z([qubits[3]], (qubits[12]));
            Controlled Z([qubits[3]], (qubits[13]));
            Controlled Z([qubits[3]], (qubits[14]));
            Ry(1.1769293, qubits[3]);
            Controlled Z([qubits[4]], (qubits[5]));
            Rz(2.7835686, qubits[3]);
            Controlled Z([qubits[4]], (qubits[6]));
            Controlled Z([qubits[0]], (qubits[3]));
            Controlled Z([qubits[4]], (qubits[7]));
            Controlled Z([qubits[4]], (qubits[8]));
            Controlled Z([qubits[4]], (qubits[9]));
            Controlled Z([qubits[4]], (qubits[10]));
            Controlled Z([qubits[4]], (qubits[11]));
            Controlled Z([qubits[4]], (qubits[12]));
            Controlled Z([qubits[4]], (qubits[13]));
            Controlled Z([qubits[4]], (qubits[14]));
            Ry(1.4078831, qubits[4]);
            Controlled Z([qubits[5]], (qubits[6]));
            Rz(2.5237245, qubits[4]);
            Controlled Z([qubits[5]], (qubits[7]));
            Controlled Z([qubits[0]], (qubits[4]));
            Controlled Z([qubits[5]], (qubits[8]));
            Controlled Z([qubits[5]], (qubits[9]));
            Controlled Z([qubits[5]], (qubits[10]));
            Controlled Z([qubits[5]], (qubits[11]));
            Controlled Z([qubits[5]], (qubits[12]));
            Controlled Z([qubits[5]], (qubits[13]));
            Controlled Z([qubits[5]], (qubits[14]));
            Ry(3.0032051, qubits[5]);
            Controlled Z([qubits[6]], (qubits[7]));
            Rz(1.90216, qubits[5]);
            Controlled Z([qubits[6]], (qubits[8]));
            Controlled Z([qubits[0]], (qubits[5]));
            Controlled Z([qubits[6]], (qubits[9]));
            Controlled Z([qubits[6]], (qubits[10]));
            Controlled Z([qubits[6]], (qubits[11]));
            Controlled Z([qubits[6]], (qubits[12]));
            Controlled Z([qubits[6]], (qubits[13]));
            Controlled Z([qubits[6]], (qubits[14]));
            Ry(1.8008253, qubits[6]);
            Controlled Z([qubits[7]], (qubits[8]));
            Rz(1.8522674, qubits[6]);
            Controlled Z([qubits[7]], (qubits[9]));
            Controlled Z([qubits[0]], (qubits[6]));
            Controlled Z([qubits[7]], (qubits[10]));
            Controlled Z([qubits[7]], (qubits[11]));
            Controlled Z([qubits[7]], (qubits[12]));
            Controlled Z([qubits[7]], (qubits[13]));
            Controlled Z([qubits[7]], (qubits[14]));
            Ry(0.56633861, qubits[7]);
            Controlled Z([qubits[8]], (qubits[9]));
            Rz(0.57593017, qubits[7]);
            Controlled Z([qubits[8]], (qubits[10]));
            Controlled Z([qubits[0]], (qubits[7]));
            Controlled Z([qubits[8]], (qubits[11]));
            Controlled Z([qubits[8]], (qubits[12]));
            Controlled Z([qubits[8]], (qubits[13]));
            Controlled Z([qubits[8]], (qubits[14]));
            Ry(0.49058986, qubits[8]);
            Controlled Z([qubits[9]], (qubits[10]));
            Rz(2.2015657, qubits[8]);
            Controlled Z([qubits[9]], (qubits[11]));
            Controlled Z([qubits[0]], (qubits[8]));
            Controlled Z([qubits[9]], (qubits[12]));
            Controlled Z([qubits[9]], (qubits[13]));
            Controlled Z([qubits[9]], (qubits[14]));
            Ry(1.910039, qubits[9]);
            Controlled Z([qubits[10]], (qubits[11]));
            Rz(0.95992321, qubits[9]);
            Controlled Z([qubits[10]], (qubits[12]));
            Controlled Z([qubits[0]], (qubits[9]));
            Controlled Z([qubits[10]], (qubits[13]));
            Controlled Z([qubits[10]], (qubits[14]));
            Ry(1.0434417, qubits[10]);
            Controlled Z([qubits[11]], (qubits[12]));
            Rz(2.8412874, qubits[10]);
            Controlled Z([qubits[11]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[10]));
            Controlled Z([qubits[11]], (qubits[14]));
            Ry(2.345931, qubits[11]);
            Controlled Z([qubits[12]], (qubits[13]));
            Rz(1.3866938, qubits[11]);
            Controlled Z([qubits[12]], (qubits[14]));
            Controlled Z([qubits[0]], (qubits[11]));
            Ry(0.27014423, qubits[12]);
            Controlled Z([qubits[13]], (qubits[14]));
            Rz(2.3213249, qubits[12]);
            Ry(1.8468924, qubits[13]);
            Ry(0.096143467, qubits[14]);
            Controlled Z([qubits[0]], (qubits[12]));
            Rz(0.22449483, qubits[13]);
            Rz(3.1120735, qubits[14]);
            Controlled Z([qubits[0]], (qubits[13]));
            Controlled Z([qubits[0]], (qubits[14]));
            Controlled Z([qubits[1]], (qubits[2]));
            Controlled Z([qubits[1]], (qubits[3]));
            Controlled Z([qubits[1]], (qubits[4]));
            Controlled Z([qubits[1]], (qubits[5]));
            Controlled Z([qubits[1]], (qubits[6]));
            Controlled Z([qubits[1]], (qubits[7]));
            Controlled Z([qubits[1]], (qubits[8]));
            Controlled Z([qubits[1]], (qubits[9]));
            Controlled Z([qubits[1]], (qubits[10]));
            Controlled Z([qubits[1]], (qubits[11]));
            Controlled Z([qubits[1]], (qubits[12]));
            Controlled Z([qubits[1]], (qubits[13]));
            Controlled Z([qubits[1]], (qubits[14]));
            Controlled Z([qubits[2]], (qubits[3]));
            Controlled Z([qubits[2]], (qubits[4]));
            Controlled Z([qubits[2]], (qubits[5]));
            Controlled Z([qubits[2]], (qubits[6]));
            Controlled Z([qubits[2]], (qubits[7]));
            Controlled Z([qubits[2]], (qubits[8]));
            Controlled Z([qubits[2]], (qubits[9]));
            Controlled Z([qubits[2]], (qubits[10]));
            Controlled Z([qubits[2]], (qubits[11]));
            Controlled Z([qubits[2]], (qubits[12]));
            Controlled Z([qubits[2]], (qubits[13]));
            Controlled Z([qubits[2]], (qubits[14]));
            Controlled Z([qubits[3]], (qubits[4]));
            Controlled Z([qubits[3]], (qubits[5]));
            Controlled Z([qubits[3]], (qubits[6]));
            Controlled Z([qubits[3]], (qubits[7]));
            Controlled Z([qubits[3]], (qubits[8]));
            Controlled Z([qubits[3]], (qubits[9]));
            Controlled Z([qubits[3]], (qubits[10]));
            Controlled Z([qubits[3]], (qubits[11]));
            Controlled Z([qubits[3]], (qubits[12]));
            Controlled Z([qubits[3]], (qubits[13]));
            Controlled Z([qubits[3]], (qubits[14]));
            Controlled Z([qubits[4]], (qubits[5]));
            Controlled Z([qubits[4]], (qubits[6]));
            Controlled Z([qubits[4]], (qubits[7]));
            Controlled Z([qubits[4]], (qubits[8]));
            Controlled Z([qubits[4]], (qubits[9]));
            Controlled Z([qubits[4]], (qubits[10]));
            Controlled Z([qubits[4]], (qubits[11]));
            Controlled Z([qubits[4]], (qubits[12]));
            Controlled Z([qubits[4]], (qubits[13]));
            Controlled Z([qubits[4]], (qubits[14]));
            Controlled Z([qubits[5]], (qubits[6]));
            Controlled Z([qubits[5]], (qubits[7]));
            Controlled Z([qubits[5]], (qubits[8]));
            Controlled Z([qubits[5]], (qubits[9]));
            Controlled Z([qubits[5]], (qubits[10]));
            Controlled Z([qubits[5]], (qubits[11]));
            Controlled Z([qubits[5]], (qubits[12]));
            Controlled Z([qubits[5]], (qubits[13]));
            Controlled Z([qubits[5]], (qubits[14]));
            Controlled Z([qubits[6]], (qubits[7]));
            Controlled Z([qubits[6]], (qubits[8]));
            Controlled Z([qubits[6]], (qubits[9]));
            Controlled Z([qubits[6]], (qubits[10]));
            Controlled Z([qubits[6]], (qubits[11]));
            Controlled Z([qubits[6]], (qubits[12]));
            Controlled Z([qubits[6]], (qubits[13]));
            Controlled Z([qubits[6]], (qubits[14]));
            Controlled Z([qubits[7]], (qubits[8]));
            Controlled Z([qubits[7]], (qubits[9]));
            Controlled Z([qubits[7]], (qubits[10]));
            Controlled Z([qubits[7]], (qubits[11]));
            Controlled Z([qubits[7]], (qubits[12]));
            Controlled Z([qubits[7]], (qubits[13]));
            Controlled Z([qubits[7]], (qubits[14]));
            Controlled Z([qubits[8]], (qubits[9]));
            Controlled Z([qubits[8]], (qubits[10]));
            Controlled Z([qubits[8]], (qubits[11]));
            Controlled Z([qubits[8]], (qubits[12]));
            Controlled Z([qubits[8]], (qubits[13]));
            Controlled Z([qubits[8]], (qubits[14]));
            Controlled Z([qubits[9]], (qubits[10]));
            Controlled Z([qubits[9]], (qubits[11]));
            Controlled Z([qubits[9]], (qubits[12]));
            Controlled Z([qubits[9]], (qubits[13]));
            Controlled Z([qubits[9]], (qubits[14]));
            Controlled Z([qubits[10]], (qubits[11]));
            Controlled Z([qubits[10]], (qubits[12]));
            Controlled Z([qubits[10]], (qubits[13]));
            Controlled Z([qubits[10]], (qubits[14]));
            Controlled Z([qubits[11]], (qubits[12]));
            Controlled Z([qubits[11]], (qubits[13]));
            Controlled Z([qubits[11]], (qubits[14]));
            Controlled Z([qubits[12]], (qubits[13]));
            Controlled Z([qubits[12]], (qubits[14]));
            Controlled Z([qubits[13]], (qubits[14]));
            set meas = SetBitValue(meas, 0, ResultAsBool(M(qubits[0])));
            set meas = SetBitValue(meas, 1, ResultAsBool(M(qubits[1])));
            set meas = SetBitValue(meas, 2, ResultAsBool(M(qubits[2])));
            set meas = SetBitValue(meas, 3, ResultAsBool(M(qubits[3])));
            set meas = SetBitValue(meas, 4, ResultAsBool(M(qubits[4])));
            set meas = SetBitValue(meas, 5, ResultAsBool(M(qubits[5])));
            set meas = SetBitValue(meas, 6, ResultAsBool(M(qubits[6])));
            set meas = SetBitValue(meas, 7, ResultAsBool(M(qubits[7])));
            set meas = SetBitValue(meas, 8, ResultAsBool(M(qubits[8])));
            set meas = SetBitValue(meas, 9, ResultAsBool(M(qubits[9])));
            set meas = SetBitValue(meas, 10, ResultAsBool(M(qubits[10])));
            set meas = SetBitValue(meas, 11, ResultAsBool(M(qubits[11])));
            set meas = SetBitValue(meas, 12, ResultAsBool(M(qubits[12])));
            set meas = SetBitValue(meas, 13, ResultAsBool(M(qubits[13])));
            set meas = SetBitValue(meas, 14, ResultAsBool(M(qubits[14])));
            ResetAll(qubits);
        }
        return (c0, meas);
    }
}
