from pyquil import Program, get_qc
from pyquil.gates import H, CSWAP, MEASURE, RY, RZ
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_sqrt, quil_exp, quil_cis
from pyquil.quilbase import DefGate
from functools import reduce
import numpy as np

shots = 1024

p_theta = Parameter('theta')
p_phi = Parameter('phi')

yy_array = np.array([ [quil_cos(p_theta), 0, 0, 1j*quil_sin(p_theta)], [0, quil_cos(p_theta), -1j*quil_sin(p_theta), 0], [0, -1j*quil_sin(p_theta), quil_cos(p_theta), 0], [1j*quil_sin(p_theta), 0, 0, quil_cos(p_theta)] ])
zz_array = np.array([ [ quil_exp(-1j * p_theta / 2), 0, 0, 0 ], [ 0, quil_exp(1j * p_theta / 2), 0, 0], [ 0, 0, quil_exp(1j * p_theta / 2), 0 ], [ 0, 0, 0, quil_exp(-1j * p_theta / 2) ] ])
cry_array = np.array([[ 1, 0, 0, 0 ],[ 0, 1, 0, 0 ],[ 0, 0, quil_cos(p_theta / 2), -1*quil_sin(p_theta / 2) ],[ 0, 0, quil_sin(p_theta / 2), quil_cos(p_theta / 2) ]])
crz_array = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, quil_cos(p_phi / 2) - 1j * quil_sin(p_phi / 2), 0], [0, 0, 0, quil_cos(p_phi / 2) + 1j * quil_sin(p_phi / 2)]])


yy_defgate = DefGate('yy', yy_array, [p_theta])
yy = yy_defgate.get_constructor()
zz_defgate = DefGate('zz', zz_array, [p_theta])
zz = zz_defgate.get_constructor()
cry_defgate = DefGate('cry', cry_array, [p_theta])
cry = cry_defgate.get_constructor()
crz_defgate = DefGate('crz', crz_array, [p_phi])
crz = crz_defgate.get_constructor()


p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=102)

p.inst(yy_defgate)
p.inst(zz_defgate)
p.inst(cry_defgate)
p.inst(crz_defgate)

p.inst(H(0))
p.inst(RY(1.4453634, 1))
p.inst(RY(2.1383653, 2))
p.inst(RY(4.0920637, 3))
p.inst(RY(2.4282336, 4))
p.inst(RY(5.4002712, 5))
p.inst(RY(4.3865417, 6))
p.inst(RY(4.6921768, 7))
p.inst(RY(5.4525141, 8))
p.inst(RY(0.60655041, 9))
p.inst(RY(1.2309083, 10))
p.inst(RY(0.17675434, 11))
p.inst(RY(1.2472087, 12))
p.inst(RY(6.1875423, 13))
p.inst(RY(2.1215094, 14))
p.inst(RY(5.1780347, 15))
p.inst(RY(1.4385234, 16))
p.inst(RY(3.463653, 17))
p.inst(RY(5.9164614, 18))
p.inst(RY(3.7496088, 19))
p.inst(RY(0.5457547, 20))
p.inst(RY(4.7300217, 21))
p.inst(RY(2.9379458, 22))
p.inst(RY(5.9767772, 23))
p.inst(RY(2.9581045, 24))
p.inst(RY(3.0700699, 25))
p.inst(RY(0.65770528, 26))
p.inst(RY(2.7470923, 27))
p.inst(RY(3.0712244, 28))
p.inst(RY(-1.2757521, 29))
p.inst(RY(-2.8370765, 30))
p.inst(RY(-0.44314396, 31))
p.inst(RY(0.82777467, 32))
p.inst(RY(-2.7239944, 33))
p.inst(RY(2.4547499, 34))
p.inst(RY(0.24557055, 35))
p.inst(RY(2.2552515, 36))
p.inst(RY(0.86910886, 37))
p.inst(RY(-2.550615, 38))
p.inst(RY(-2.060276, 39))
p.inst(RY(0.26746397, 40))
p.inst(RY(-0.82166689, 41))
p.inst(RY(-0.21494785, 42))
p.inst(RY(-2.5349206, 43))
p.inst(RY(1.6604066, 44))
p.inst(RY(0.93788101, 45))
p.inst(RY(-0.11825949, 46))
p.inst(RY(0.81948459, 47))
p.inst(RY(2.9728222, 48))
p.inst(RY(1.6703583, 49))
p.inst(RY(-1.6688487, 50))
p.inst(RZ(5.209615, 1))
p.inst(RZ(3.1856725, 2))
p.inst(RZ(3.6005747, 3))
p.inst(RZ(2.6392459, 4))
p.inst(RZ(1.9470694, 5))
p.inst(RZ(2.4443784, 6))
p.inst(RZ(4.5959191, 7))
p.inst(RZ(2.4976439, 8))
p.inst(RZ(5.271, 9))
p.inst(RZ(6.1865766, 10))
p.inst(RZ(0.733705, 11))
p.inst(RZ(1.8651221, 12))
p.inst(RZ(0.30996709, 13))
p.inst(RZ(0.42876944, 14))
p.inst(RZ(4.3242564, 15))
p.inst(RZ(0.4580661, 16))
p.inst(RZ(4.2064162, 17))
p.inst(RZ(2.4758525, 18))
p.inst(RZ(4.3601758, 19))
p.inst(RZ(6.0351101, 20))
p.inst(RZ(1.9403278, 21))
p.inst(RZ(1.4914686, 22))
p.inst(RZ(1.8827506, 23))
p.inst(RZ(1.3534938, 24))
p.inst(RZ(2.2054647, 25))
p.inst(RZ(-0.92115556, 26))
p.inst(RZ(1.9203504, 27))
p.inst(RZ(-1.4674279, 28))
p.inst(RZ(-2.1244229, 29))
p.inst(RZ(-1.3864448, 30))
p.inst(RZ(2.3951822, 31))
p.inst(RZ(-3.084212, 32))
p.inst(RZ(-3.0513779, 33))
p.inst(RZ(0.069608388, 34))
p.inst(RZ(-2.6550364, 35))
p.inst(RZ(-0.29517524, 36))
p.inst(RZ(-1.4574567, 37))
p.inst(RZ(-0.40737172, 38))
p.inst(RZ(1.7863141, 39))
p.inst(RZ(2.8603088, 40))
p.inst(RZ(-0.18783144, 41))
p.inst(RZ(-2.2789284, 42))
p.inst(RZ(1.9218502, 43))
p.inst(RZ(2.5670747, 44))
p.inst(RZ(0.57303858, 45))
p.inst(RZ(-1.2712555, 46))
p.inst(RZ(-0.95238218, 47))
p.inst(RZ(-2.2938746, 48))
p.inst(RZ(0.61263002, 49))
p.inst(RZ(2.4665645, 50))
p.inst(yy(4.5544619)(1, 2))
p.inst(zz(5.5961168)(1, 2))
p.inst(yy(5.5105315)(2, 3))
p.inst(zz(1.3788156)(2, 3))
p.inst(cry(0.15865312)(1, 2))
p.inst(yy(5.8540838)(3, 4))
p.inst(crz(6.0921477)(1, 2))
p.inst(zz(3.5328693)(3, 4))
p.inst(cry(3.1095433)(2, 3))
p.inst(yy(0.22592378)(4, 5))
p.inst(crz(1.71928)(2, 3))
p.inst(zz(5.1923696)(4, 5))
p.inst(cry(0.24215703)(3, 4))
p.inst(yy(4.3152997)(5, 6))
p.inst(crz(0.27494644)(3, 4))
p.inst(zz(6.1017021)(5, 6))
p.inst(cry(2.9305011)(4, 5))
p.inst(yy(2.3254305)(6, 7))
p.inst(crz(3.3481201)(4, 5))
p.inst(zz(3.2981126)(6, 7))
p.inst(cry(5.7804743)(5, 6))
p.inst(yy(3.3760111)(7, 8))
p.inst(crz(0.48195899)(5, 6))
p.inst(zz(3.8010703)(7, 8))
p.inst(cry(3.6962453)(6, 7))
p.inst(yy(2.8173043)(8, 9))
p.inst(crz(2.7969055)(6, 7))
p.inst(zz(2.3613951)(8, 9))
p.inst(cry(3.286148)(7, 8))
p.inst(yy(4.8851636)(9, 10))
p.inst(crz(4.0920841)(7, 8))
p.inst(zz(3.7731466)(9, 10))
p.inst(cry(0.88032376)(8, 9))
p.inst(yy(4.7667437)(10, 11))
p.inst(crz(0.11947222)(8, 9))
p.inst(zz(2.436951)(10, 11))
p.inst(cry(5.9486697)(9, 10))
p.inst(yy(1.4533705)(11, 12))
p.inst(crz(4.8575331)(9, 10))
p.inst(zz(0.51624107)(11, 12))
p.inst(cry(1.4645071)(10, 11))
p.inst(yy(4.295801)(12, 13))
p.inst(crz(1.6690939)(10, 11))
p.inst(zz(6.0670021)(12, 13))
p.inst(cry(1.678879)(11, 12))
p.inst(yy(5.1699641)(13, 14))
p.inst(crz(2.6040394)(11, 12))
p.inst(zz(6.005211)(13, 14))
p.inst(cry(4.2420346)(12, 13))
p.inst(yy(1.4638562)(14, 15))
p.inst(crz(3.8361496)(12, 13))
p.inst(zz(4.1840019)(14, 15))
p.inst(cry(1.4829188)(13, 14))
p.inst(yy(0.99667757)(15, 16))
p.inst(crz(2.8471283)(13, 14))
p.inst(zz(0.70688627)(15, 16))
p.inst(cry(2.2663895)(14, 15))
p.inst(yy(4.9121572)(16, 17))
p.inst(crz(1.1917127)(14, 15))
p.inst(zz(4.1452579)(16, 17))
p.inst(cry(3.1766454)(15, 16))
p.inst(yy(3.4520515)(17, 18))
p.inst(crz(4.9319342)(15, 16))
p.inst(zz(2.4645871)(17, 18))
p.inst(cry(4.1387398)(16, 17))
p.inst(yy(2.1885175)(18, 19))
p.inst(crz(5.6057718)(16, 17))
p.inst(zz(5.3738347)(18, 19))
p.inst(cry(3.0979769)(17, 18))
p.inst(yy(5.9212287)(19, 20))
p.inst(crz(0.29274723)(17, 18))
p.inst(zz(5.8889558)(19, 20))
p.inst(cry(4.160468)(18, 19))
p.inst(yy(3.5433364)(20, 21))
p.inst(crz(4.8188789)(18, 19))
p.inst(zz(2.1485059)(20, 21))
p.inst(cry(0.33166687)(19, 20))
p.inst(yy(5.9828383)(21, 22))
p.inst(crz(2.1761463)(19, 20))
p.inst(zz(2.573339)(21, 22))
p.inst(cry(1.6883253)(20, 21))
p.inst(yy(0.52493774)(22, 23))
p.inst(crz(2.0157073)(20, 21))
p.inst(zz(3.5278926)(22, 23))
p.inst(cry(3.6908522)(21, 22))
p.inst(yy(0.89828112)(23, 24))
p.inst(crz(3.7288452)(21, 22))
p.inst(zz(3.2416407)(23, 24))
p.inst(cry(5.4139755)(22, 23))
p.inst(yy(5.8893319)(24, 25))
p.inst(crz(5.4731227)(22, 23))
p.inst(zz(1.8927667)(24, 25))
p.inst(cry(4.1402198)(23, 24))
p.inst(crz(2.9838188)(23, 24))
p.inst(cry(1.8322796)(24, 25))
p.inst(crz(5.0799698)(24, 25))
p.inst(CSWAP(0, 1, 26))
p.inst(CSWAP(0, 2, 27))
p.inst(CSWAP(0, 3, 28))
p.inst(CSWAP(0, 4, 29))
p.inst(CSWAP(0, 5, 30))
p.inst(CSWAP(0, 6, 31))
p.inst(CSWAP(0, 7, 32))
p.inst(CSWAP(0, 8, 33))
p.inst(CSWAP(0, 9, 34))
p.inst(CSWAP(0, 10, 35))
p.inst(CSWAP(0, 11, 36))
p.inst(CSWAP(0, 12, 37))
p.inst(CSWAP(0, 13, 38))
p.inst(CSWAP(0, 14, 39))
p.inst(CSWAP(0, 15, 40))
p.inst(CSWAP(0, 16, 41))
p.inst(CSWAP(0, 17, 42))
p.inst(CSWAP(0, 18, 43))
p.inst(CSWAP(0, 19, 44))
p.inst(CSWAP(0, 20, 45))
p.inst(CSWAP(0, 21, 46))
p.inst(CSWAP(0, 22, 47))
p.inst(CSWAP(0, 23, 48))
p.inst(CSWAP(0, 24, 49))
p.inst(CSWAP(0, 25, 50))
p.inst(H(0))
p.inst(MEASURE(0, ro[51]))
p.inst(MEASURE(1, ro[52]))
p.inst(MEASURE(2, ro[53]))
p.inst(MEASURE(3, ro[54]))
p.inst(MEASURE(4, ro[55]))
p.inst(MEASURE(5, ro[56]))
p.inst(MEASURE(6, ro[57]))
p.inst(MEASURE(7, ro[58]))
p.inst(MEASURE(8, ro[59]))
p.inst(MEASURE(9, ro[60]))
p.inst(MEASURE(10, ro[61]))
p.inst(MEASURE(11, ro[62]))
p.inst(MEASURE(12, ro[63]))
p.inst(MEASURE(13, ro[64]))
p.inst(MEASURE(14, ro[65]))
p.inst(MEASURE(15, ro[66]))
p.inst(MEASURE(16, ro[67]))
p.inst(MEASURE(17, ro[68]))
p.inst(MEASURE(18, ro[69]))
p.inst(MEASURE(19, ro[70]))
p.inst(MEASURE(20, ro[71]))
p.inst(MEASURE(21, ro[72]))
p.inst(MEASURE(22, ro[73]))
p.inst(MEASURE(23, ro[74]))
p.inst(MEASURE(24, ro[75]))
p.inst(MEASURE(25, ro[76]))
p.inst(MEASURE(26, ro[77]))
p.inst(MEASURE(27, ro[78]))
p.inst(MEASURE(28, ro[79]))
p.inst(MEASURE(29, ro[80]))
p.inst(MEASURE(30, ro[81]))
p.inst(MEASURE(31, ro[82]))
p.inst(MEASURE(32, ro[83]))
p.inst(MEASURE(33, ro[84]))
p.inst(MEASURE(34, ro[85]))
p.inst(MEASURE(35, ro[86]))
p.inst(MEASURE(36, ro[87]))
p.inst(MEASURE(37, ro[88]))
p.inst(MEASURE(38, ro[89]))
p.inst(MEASURE(39, ro[90]))
p.inst(MEASURE(40, ro[91]))
p.inst(MEASURE(41, ro[92]))
p.inst(MEASURE(42, ro[93]))
p.inst(MEASURE(43, ro[94]))
p.inst(MEASURE(44, ro[95]))
p.inst(MEASURE(45, ro[96]))
p.inst(MEASURE(46, ro[97]))
p.inst(MEASURE(47, ro[98]))
p.inst(MEASURE(48, ro[99]))
p.inst(MEASURE(49, ro[100]))
p.inst(MEASURE(50, ro[101]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('51q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
