from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, PHASE, MEASURE
from functools import reduce
import numpy as np

shots = 1024

p = Program()

ro = p.declare('ro', memory_type='BIT', memory_size=30)

p.inst(H(0))
p.inst(PHASE(np.pi / 4, 1))
p.inst(PHASE(np.pi / 8, 2))
p.inst(PHASE(np.pi / 16, 3))
p.inst(PHASE(np.pi / 32, 4))
p.inst(PHASE(np.pi / 64, 5))
p.inst(PHASE(np.pi / 128, 6))
p.inst(PHASE(np.pi / 256, 7))
p.inst(PHASE(np.pi / 512, 8))
p.inst(PHASE(np.pi / 1024, 9))
p.inst(PHASE(np.pi / 2048, 10))
p.inst(PHASE(np.pi / 4096, 11))
p.inst(PHASE(np.pi / 8192, 12))
p.inst(PHASE(np.pi / 16384, 13))
p.inst(PHASE(np.pi / 32768, 14))
p.inst(CNOT(1, 0))
p.inst(PHASE(-np.pi / 4, 0))
p.inst(CNOT(1, 0))
p.inst(PHASE(np.pi / 4, 0))
p.inst(H(1))
p.inst(CNOT(2, 0))
p.inst(PHASE(-np.pi / 8, 0))
p.inst(CNOT(2, 0))
p.inst(PHASE(np.pi / 8, 0))
p.inst(PHASE(np.pi / 4, 2))
p.inst(CNOT(2, 1))
p.inst(PHASE(-np.pi / 4, 1))
p.inst(CNOT(2, 1))
p.inst(PHASE(np.pi / 4, 1))
p.inst(H(2))
p.inst(CNOT(3, 0))
p.inst(PHASE(-np.pi / 16, 0))
p.inst(CNOT(3, 0))
p.inst(PHASE(np.pi / 16, 0))
p.inst(PHASE(np.pi / 8, 3))
p.inst(CNOT(3, 1))
p.inst(PHASE(-np.pi / 8, 1))
p.inst(CNOT(3, 1))
p.inst(PHASE(np.pi / 8, 1))
p.inst(PHASE(np.pi / 4, 3))
p.inst(CNOT(3, 2))
p.inst(PHASE(-np.pi / 4, 2))
p.inst(CNOT(3, 2))
p.inst(PHASE(np.pi / 4, 2))
p.inst(H(3))
p.inst(CNOT(4, 0))
p.inst(PHASE(-np.pi / 32, 0))
p.inst(CNOT(4, 0))
p.inst(PHASE(np.pi / 32, 0))
p.inst(PHASE(np.pi / 16, 4))
p.inst(CNOT(4, 1))
p.inst(PHASE(-np.pi / 16, 1))
p.inst(CNOT(4, 1))
p.inst(PHASE(np.pi / 16, 1))
p.inst(PHASE(np.pi / 8, 4))
p.inst(CNOT(4, 2))
p.inst(PHASE(-np.pi / 8, 2))
p.inst(CNOT(4, 2))
p.inst(PHASE(np.pi / 8, 2))
p.inst(PHASE(np.pi / 4, 4))
p.inst(CNOT(4, 3))
p.inst(PHASE(-np.pi / 4, 3))
p.inst(CNOT(4, 3))
p.inst(PHASE(np.pi / 4, 3))
p.inst(H(4))
p.inst(CNOT(5, 0))
p.inst(PHASE(-np.pi / 64, 0))
p.inst(CNOT(5, 0))
p.inst(PHASE(np.pi / 64, 0))
p.inst(PHASE(np.pi / 32, 5))
p.inst(CNOT(5, 1))
p.inst(PHASE(-np.pi / 32, 1))
p.inst(CNOT(5, 1))
p.inst(PHASE(np.pi / 32, 1))
p.inst(PHASE(np.pi / 16, 5))
p.inst(CNOT(5, 2))
p.inst(PHASE(-np.pi / 16, 2))
p.inst(CNOT(5, 2))
p.inst(PHASE(np.pi / 16, 2))
p.inst(PHASE(np.pi / 8, 5))
p.inst(CNOT(5, 3))
p.inst(PHASE(-np.pi / 8, 3))
p.inst(CNOT(5, 3))
p.inst(PHASE(np.pi / 8, 3))
p.inst(PHASE(np.pi / 4, 5))
p.inst(CNOT(5, 4))
p.inst(PHASE(-np.pi / 4, 4))
p.inst(CNOT(5, 4))
p.inst(PHASE(np.pi / 4, 4))
p.inst(H(5))
p.inst(CNOT(6, 0))
p.inst(PHASE(-np.pi / 128, 0))
p.inst(CNOT(6, 0))
p.inst(PHASE(np.pi / 128, 0))
p.inst(PHASE(np.pi / 64, 6))
p.inst(CNOT(6, 1))
p.inst(PHASE(-np.pi / 64, 1))
p.inst(CNOT(6, 1))
p.inst(PHASE(np.pi / 64, 1))
p.inst(PHASE(np.pi / 32, 6))
p.inst(CNOT(6, 2))
p.inst(PHASE(-np.pi / 32, 2))
p.inst(CNOT(6, 2))
p.inst(PHASE(np.pi / 32, 2))
p.inst(PHASE(np.pi / 16, 6))
p.inst(CNOT(6, 3))
p.inst(PHASE(-np.pi / 16, 3))
p.inst(CNOT(6, 3))
p.inst(PHASE(np.pi / 16, 3))
p.inst(PHASE(np.pi / 8, 6))
p.inst(CNOT(6, 4))
p.inst(PHASE(-np.pi / 8, 4))
p.inst(CNOT(6, 4))
p.inst(PHASE(np.pi / 8, 4))
p.inst(PHASE(np.pi / 4, 6))
p.inst(CNOT(6, 5))
p.inst(PHASE(-np.pi / 4, 5))
p.inst(CNOT(6, 5))
p.inst(PHASE(np.pi / 4, 5))
p.inst(H(6))
p.inst(CNOT(7, 0))
p.inst(PHASE(-np.pi / 256, 0))
p.inst(CNOT(7, 0))
p.inst(PHASE(np.pi / 256, 0))
p.inst(PHASE(np.pi / 128, 7))
p.inst(CNOT(7, 1))
p.inst(PHASE(-np.pi / 128, 1))
p.inst(CNOT(7, 1))
p.inst(PHASE(np.pi / 128, 1))
p.inst(PHASE(np.pi / 64, 7))
p.inst(CNOT(7, 2))
p.inst(PHASE(-np.pi / 64, 2))
p.inst(CNOT(7, 2))
p.inst(PHASE(np.pi / 64, 2))
p.inst(PHASE(np.pi / 32, 7))
p.inst(CNOT(7, 3))
p.inst(PHASE(-np.pi / 32, 3))
p.inst(CNOT(7, 3))
p.inst(PHASE(np.pi / 32, 3))
p.inst(PHASE(np.pi / 16, 7))
p.inst(CNOT(7, 4))
p.inst(PHASE(-np.pi / 16, 4))
p.inst(CNOT(7, 4))
p.inst(PHASE(np.pi / 16, 4))
p.inst(PHASE(np.pi / 8, 7))
p.inst(CNOT(7, 5))
p.inst(PHASE(-np.pi / 8, 5))
p.inst(CNOT(7, 5))
p.inst(PHASE(np.pi / 8, 5))
p.inst(PHASE(np.pi / 4, 7))
p.inst(CNOT(7, 6))
p.inst(PHASE(-np.pi / 4, 6))
p.inst(CNOT(7, 6))
p.inst(PHASE(np.pi / 4, 6))
p.inst(H(7))
p.inst(CNOT(8, 0))
p.inst(PHASE(-np.pi / 512, 0))
p.inst(CNOT(8, 0))
p.inst(PHASE(np.pi / 512, 0))
p.inst(PHASE(np.pi / 256, 8))
p.inst(CNOT(8, 1))
p.inst(PHASE(-np.pi / 256, 1))
p.inst(CNOT(8, 1))
p.inst(PHASE(np.pi / 256, 1))
p.inst(PHASE(np.pi / 128, 8))
p.inst(CNOT(8, 2))
p.inst(PHASE(-np.pi / 128, 2))
p.inst(CNOT(8, 2))
p.inst(PHASE(np.pi / 128, 2))
p.inst(PHASE(np.pi / 64, 8))
p.inst(CNOT(8, 3))
p.inst(PHASE(-np.pi / 64, 3))
p.inst(CNOT(8, 3))
p.inst(PHASE(np.pi / 64, 3))
p.inst(PHASE(np.pi / 32, 8))
p.inst(CNOT(8, 4))
p.inst(PHASE(-np.pi / 32, 4))
p.inst(CNOT(8, 4))
p.inst(PHASE(np.pi / 32, 4))
p.inst(PHASE(np.pi / 16, 8))
p.inst(CNOT(8, 5))
p.inst(PHASE(-np.pi / 16, 5))
p.inst(CNOT(8, 5))
p.inst(PHASE(np.pi / 16, 5))
p.inst(PHASE(np.pi / 8, 8))
p.inst(CNOT(8, 6))
p.inst(PHASE(-np.pi / 8, 6))
p.inst(CNOT(8, 6))
p.inst(PHASE(np.pi / 8, 6))
p.inst(PHASE(np.pi / 4, 8))
p.inst(CNOT(8, 7))
p.inst(PHASE(-np.pi / 4, 7))
p.inst(CNOT(8, 7))
p.inst(PHASE(np.pi / 4, 7))
p.inst(H(8))
p.inst(CNOT(9, 0))
p.inst(PHASE(-np.pi / 1024, 0))
p.inst(CNOT(9, 0))
p.inst(PHASE(np.pi / 1024, 0))
p.inst(PHASE(np.pi / 512, 9))
p.inst(CNOT(9, 1))
p.inst(PHASE(-np.pi / 512, 1))
p.inst(CNOT(9, 1))
p.inst(PHASE(np.pi / 512, 1))
p.inst(PHASE(np.pi / 256, 9))
p.inst(CNOT(9, 2))
p.inst(PHASE(-np.pi / 256, 2))
p.inst(CNOT(9, 2))
p.inst(PHASE(np.pi / 256, 2))
p.inst(PHASE(np.pi / 128, 9))
p.inst(CNOT(9, 3))
p.inst(PHASE(-np.pi / 128, 3))
p.inst(CNOT(9, 3))
p.inst(PHASE(np.pi / 128, 3))
p.inst(PHASE(np.pi / 64, 9))
p.inst(CNOT(9, 4))
p.inst(PHASE(-np.pi / 64, 4))
p.inst(CNOT(9, 4))
p.inst(PHASE(np.pi / 64, 4))
p.inst(PHASE(np.pi / 32, 9))
p.inst(CNOT(9, 5))
p.inst(PHASE(-np.pi / 32, 5))
p.inst(CNOT(9, 5))
p.inst(PHASE(np.pi / 32, 5))
p.inst(PHASE(np.pi / 16, 9))
p.inst(CNOT(9, 6))
p.inst(PHASE(-np.pi / 16, 6))
p.inst(CNOT(9, 6))
p.inst(PHASE(np.pi / 16, 6))
p.inst(PHASE(np.pi / 8, 9))
p.inst(CNOT(9, 7))
p.inst(PHASE(-np.pi / 8, 7))
p.inst(CNOT(9, 7))
p.inst(PHASE(np.pi / 8, 7))
p.inst(PHASE(np.pi / 4, 9))
p.inst(CNOT(9, 8))
p.inst(PHASE(-np.pi / 4, 8))
p.inst(CNOT(9, 8))
p.inst(PHASE(np.pi / 4, 8))
p.inst(H(9))
p.inst(CNOT(10, 0))
p.inst(PHASE(-np.pi / 2048, 0))
p.inst(CNOT(10, 0))
p.inst(PHASE(np.pi / 2048, 0))
p.inst(PHASE(np.pi / 1024, 10))
p.inst(CNOT(10, 1))
p.inst(PHASE(-np.pi / 1024, 1))
p.inst(CNOT(10, 1))
p.inst(PHASE(np.pi / 1024, 1))
p.inst(PHASE(np.pi / 512, 10))
p.inst(CNOT(10, 2))
p.inst(PHASE(-np.pi / 512, 2))
p.inst(CNOT(10, 2))
p.inst(PHASE(np.pi / 512, 2))
p.inst(PHASE(np.pi / 256, 10))
p.inst(CNOT(10, 3))
p.inst(PHASE(-np.pi / 256, 3))
p.inst(CNOT(10, 3))
p.inst(PHASE(np.pi / 256, 3))
p.inst(PHASE(np.pi / 128, 10))
p.inst(CNOT(10, 4))
p.inst(PHASE(-np.pi / 128, 4))
p.inst(CNOT(10, 4))
p.inst(PHASE(np.pi / 128, 4))
p.inst(PHASE(np.pi / 64, 10))
p.inst(CNOT(10, 5))
p.inst(PHASE(-np.pi / 64, 5))
p.inst(CNOT(10, 5))
p.inst(PHASE(np.pi / 64, 5))
p.inst(PHASE(np.pi / 32, 10))
p.inst(CNOT(10, 6))
p.inst(PHASE(-np.pi / 32, 6))
p.inst(CNOT(10, 6))
p.inst(PHASE(np.pi / 32, 6))
p.inst(PHASE(np.pi / 16, 10))
p.inst(CNOT(10, 7))
p.inst(PHASE(-np.pi / 16, 7))
p.inst(CNOT(10, 7))
p.inst(PHASE(np.pi / 16, 7))
p.inst(PHASE(np.pi / 8, 10))
p.inst(CNOT(10, 8))
p.inst(PHASE(-np.pi / 8, 8))
p.inst(CNOT(10, 8))
p.inst(PHASE(np.pi / 8, 8))
p.inst(PHASE(np.pi / 4, 10))
p.inst(CNOT(10, 9))
p.inst(PHASE(-np.pi / 4, 9))
p.inst(CNOT(10, 9))
p.inst(PHASE(np.pi / 4, 9))
p.inst(H(10))
p.inst(CNOT(11, 0))
p.inst(PHASE(-np.pi / 4096, 0))
p.inst(CNOT(11, 0))
p.inst(PHASE(np.pi / 4096, 0))
p.inst(PHASE(np.pi / 2048, 11))
p.inst(CNOT(11, 1))
p.inst(PHASE(-np.pi / 2048, 1))
p.inst(CNOT(11, 1))
p.inst(PHASE(np.pi / 2048, 1))
p.inst(PHASE(np.pi / 1024, 11))
p.inst(CNOT(11, 2))
p.inst(PHASE(-np.pi / 1024, 2))
p.inst(CNOT(11, 2))
p.inst(PHASE(np.pi / 1024, 2))
p.inst(PHASE(np.pi / 512, 11))
p.inst(CNOT(11, 3))
p.inst(PHASE(-np.pi / 512, 3))
p.inst(CNOT(11, 3))
p.inst(PHASE(np.pi / 512, 3))
p.inst(PHASE(np.pi / 256, 11))
p.inst(CNOT(11, 4))
p.inst(PHASE(-np.pi / 256, 4))
p.inst(CNOT(11, 4))
p.inst(PHASE(np.pi / 256, 4))
p.inst(PHASE(np.pi / 128, 11))
p.inst(CNOT(11, 5))
p.inst(PHASE(-np.pi / 128, 5))
p.inst(CNOT(11, 5))
p.inst(PHASE(np.pi / 128, 5))
p.inst(PHASE(np.pi / 64, 11))
p.inst(CNOT(11, 6))
p.inst(PHASE(-np.pi / 64, 6))
p.inst(CNOT(11, 6))
p.inst(PHASE(np.pi / 64, 6))
p.inst(PHASE(np.pi / 32, 11))
p.inst(CNOT(11, 7))
p.inst(PHASE(-np.pi / 32, 7))
p.inst(CNOT(11, 7))
p.inst(PHASE(np.pi / 32, 7))
p.inst(PHASE(np.pi / 16, 11))
p.inst(CNOT(11, 8))
p.inst(PHASE(-np.pi / 16, 8))
p.inst(CNOT(11, 8))
p.inst(PHASE(np.pi / 16, 8))
p.inst(PHASE(np.pi / 8, 11))
p.inst(CNOT(11, 9))
p.inst(PHASE(-np.pi / 8, 9))
p.inst(CNOT(11, 9))
p.inst(PHASE(np.pi / 8, 9))
p.inst(PHASE(np.pi / 4, 11))
p.inst(CNOT(11, 10))
p.inst(PHASE(-np.pi / 4, 10))
p.inst(CNOT(11, 10))
p.inst(PHASE(np.pi / 4, 10))
p.inst(H(11))
p.inst(CNOT(12, 0))
p.inst(PHASE(-np.pi / 8192, 0))
p.inst(CNOT(12, 0))
p.inst(PHASE(np.pi / 8192, 0))
p.inst(PHASE(np.pi / 4096, 12))
p.inst(CNOT(12, 1))
p.inst(PHASE(-np.pi / 4096, 1))
p.inst(CNOT(12, 1))
p.inst(PHASE(np.pi / 4096, 1))
p.inst(PHASE(np.pi / 2048, 12))
p.inst(CNOT(12, 2))
p.inst(PHASE(-np.pi / 2048, 2))
p.inst(CNOT(12, 2))
p.inst(PHASE(np.pi / 2048, 2))
p.inst(PHASE(np.pi / 1024, 12))
p.inst(CNOT(12, 3))
p.inst(PHASE(-np.pi / 1024, 3))
p.inst(CNOT(12, 3))
p.inst(PHASE(np.pi / 1024, 3))
p.inst(PHASE(np.pi / 512, 12))
p.inst(CNOT(12, 4))
p.inst(PHASE(-np.pi / 512, 4))
p.inst(CNOT(12, 4))
p.inst(PHASE(np.pi / 512, 4))
p.inst(PHASE(np.pi / 256, 12))
p.inst(CNOT(12, 5))
p.inst(PHASE(-np.pi / 256, 5))
p.inst(CNOT(12, 5))
p.inst(PHASE(np.pi / 256, 5))
p.inst(PHASE(np.pi / 128, 12))
p.inst(CNOT(12, 6))
p.inst(PHASE(-np.pi / 128, 6))
p.inst(CNOT(12, 6))
p.inst(PHASE(np.pi / 128, 6))
p.inst(PHASE(np.pi / 64, 12))
p.inst(CNOT(12, 7))
p.inst(PHASE(-np.pi / 64, 7))
p.inst(CNOT(12, 7))
p.inst(PHASE(np.pi / 64, 7))
p.inst(PHASE(np.pi / 32, 12))
p.inst(CNOT(12, 8))
p.inst(PHASE(-np.pi / 32, 8))
p.inst(CNOT(12, 8))
p.inst(PHASE(np.pi / 32, 8))
p.inst(PHASE(np.pi / 16, 12))
p.inst(CNOT(12, 9))
p.inst(PHASE(-np.pi / 16, 9))
p.inst(CNOT(12, 9))
p.inst(PHASE(np.pi / 16, 9))
p.inst(PHASE(np.pi / 8, 12))
p.inst(CNOT(12, 10))
p.inst(PHASE(-np.pi / 8, 10))
p.inst(CNOT(12, 10))
p.inst(PHASE(np.pi / 8, 10))
p.inst(PHASE(np.pi / 4, 12))
p.inst(CNOT(12, 11))
p.inst(PHASE(-np.pi / 4, 11))
p.inst(CNOT(12, 11))
p.inst(PHASE(np.pi / 4, 11))
p.inst(H(12))
p.inst(CNOT(13, 0))
p.inst(PHASE(-np.pi / 16384, 0))
p.inst(CNOT(13, 0))
p.inst(PHASE(np.pi / 16384, 0))
p.inst(PHASE(np.pi / 8192, 13))
p.inst(CNOT(13, 1))
p.inst(PHASE(-np.pi / 8192, 1))
p.inst(CNOT(13, 1))
p.inst(PHASE(np.pi / 8192, 1))
p.inst(PHASE(np.pi / 4096, 13))
p.inst(CNOT(13, 2))
p.inst(PHASE(-np.pi / 4096, 2))
p.inst(CNOT(13, 2))
p.inst(PHASE(np.pi / 4096, 2))
p.inst(PHASE(np.pi / 2048, 13))
p.inst(CNOT(13, 3))
p.inst(PHASE(-np.pi / 2048, 3))
p.inst(CNOT(13, 3))
p.inst(PHASE(np.pi / 2048, 3))
p.inst(PHASE(np.pi / 1024, 13))
p.inst(CNOT(13, 4))
p.inst(PHASE(-np.pi / 1024, 4))
p.inst(CNOT(13, 4))
p.inst(PHASE(np.pi / 1024, 4))
p.inst(PHASE(np.pi / 512, 13))
p.inst(CNOT(13, 5))
p.inst(PHASE(-np.pi / 512, 5))
p.inst(CNOT(13, 5))
p.inst(PHASE(np.pi / 512, 5))
p.inst(PHASE(np.pi / 256, 13))
p.inst(CNOT(13, 6))
p.inst(PHASE(-np.pi / 256, 6))
p.inst(CNOT(13, 6))
p.inst(PHASE(np.pi / 256, 6))
p.inst(PHASE(np.pi / 128, 13))
p.inst(CNOT(13, 7))
p.inst(PHASE(-np.pi / 128, 7))
p.inst(CNOT(13, 7))
p.inst(PHASE(np.pi / 128, 7))
p.inst(PHASE(np.pi / 64, 13))
p.inst(CNOT(13, 8))
p.inst(PHASE(-np.pi / 64, 8))
p.inst(CNOT(13, 8))
p.inst(PHASE(np.pi / 64, 8))
p.inst(PHASE(np.pi / 32, 13))
p.inst(CNOT(13, 9))
p.inst(PHASE(-np.pi / 32, 9))
p.inst(CNOT(13, 9))
p.inst(PHASE(np.pi / 32, 9))
p.inst(PHASE(np.pi / 16, 13))
p.inst(CNOT(13, 10))
p.inst(PHASE(-np.pi / 16, 10))
p.inst(CNOT(13, 10))
p.inst(PHASE(np.pi / 16, 10))
p.inst(PHASE(np.pi / 8, 13))
p.inst(CNOT(13, 11))
p.inst(PHASE(-np.pi / 8, 11))
p.inst(CNOT(13, 11))
p.inst(PHASE(np.pi / 8, 11))
p.inst(PHASE(np.pi / 4, 13))
p.inst(CNOT(13, 12))
p.inst(PHASE(-np.pi / 4, 12))
p.inst(CNOT(13, 12))
p.inst(PHASE(np.pi / 4, 12))
p.inst(H(13))
p.inst(CNOT(14, 0))
p.inst(PHASE(-np.pi / 32768, 0))
p.inst(CNOT(14, 0))
p.inst(PHASE(np.pi / 32768, 0))
p.inst(PHASE(np.pi / 16384, 14))
p.inst(CNOT(14, 1))
p.inst(PHASE(-np.pi / 16384, 1))
p.inst(CNOT(14, 1))
p.inst(PHASE(np.pi / 16384, 1))
p.inst(PHASE(np.pi / 8192, 14))
p.inst(CNOT(14, 2))
p.inst(PHASE(-np.pi / 8192, 2))
p.inst(CNOT(14, 2))
p.inst(PHASE(np.pi / 8192, 2))
p.inst(PHASE(np.pi / 4096, 14))
p.inst(CNOT(14, 3))
p.inst(PHASE(-np.pi / 4096, 3))
p.inst(CNOT(14, 3))
p.inst(PHASE(np.pi / 4096, 3))
p.inst(PHASE(np.pi / 2048, 14))
p.inst(CNOT(14, 4))
p.inst(PHASE(-np.pi / 2048, 4))
p.inst(CNOT(14, 4))
p.inst(PHASE(np.pi / 2048, 4))
p.inst(PHASE(np.pi / 1024, 14))
p.inst(CNOT(14, 5))
p.inst(PHASE(-np.pi / 1024, 5))
p.inst(CNOT(14, 5))
p.inst(PHASE(np.pi / 1024, 5))
p.inst(PHASE(np.pi / 512, 14))
p.inst(CNOT(14, 6))
p.inst(PHASE(-np.pi / 512, 6))
p.inst(CNOT(14, 6))
p.inst(PHASE(np.pi / 512, 6))
p.inst(PHASE(np.pi / 256, 14))
p.inst(CNOT(14, 7))
p.inst(PHASE(-np.pi / 256, 7))
p.inst(CNOT(14, 7))
p.inst(PHASE(np.pi / 256, 7))
p.inst(PHASE(np.pi / 128, 14))
p.inst(CNOT(14, 8))
p.inst(PHASE(-np.pi / 128, 8))
p.inst(CNOT(14, 8))
p.inst(PHASE(np.pi / 128, 8))
p.inst(PHASE(np.pi / 64, 14))
p.inst(CNOT(14, 9))
p.inst(PHASE(-np.pi / 64, 9))
p.inst(CNOT(14, 9))
p.inst(PHASE(np.pi / 64, 9))
p.inst(PHASE(np.pi / 32, 14))
p.inst(CNOT(14, 10))
p.inst(PHASE(-np.pi / 32, 10))
p.inst(CNOT(14, 10))
p.inst(PHASE(np.pi / 32, 10))
p.inst(PHASE(np.pi / 16, 14))
p.inst(CNOT(14, 11))
p.inst(PHASE(-np.pi / 16, 11))
p.inst(CNOT(14, 11))
p.inst(PHASE(np.pi / 16, 11))
p.inst(PHASE(np.pi / 8, 14))
p.inst(CNOT(14, 12))
p.inst(PHASE(-np.pi / 8, 12))
p.inst(CNOT(14, 12))
p.inst(PHASE(np.pi / 8, 12))
p.inst(PHASE(np.pi / 4, 14))
p.inst(CNOT(14, 13))
p.inst(PHASE(-np.pi / 4, 13))
p.inst(CNOT(14, 13))
p.inst(PHASE(np.pi / 4, 13))
p.inst(H(14))
p.inst(MEASURE(0, ro[15]))
p.inst(MEASURE(1, ro[16]))
p.inst(MEASURE(2, ro[17]))
p.inst(MEASURE(3, ro[18]))
p.inst(MEASURE(4, ro[19]))
p.inst(MEASURE(5, ro[20]))
p.inst(MEASURE(6, ro[21]))
p.inst(MEASURE(7, ro[22]))
p.inst(MEASURE(8, ro[23]))
p.inst(MEASURE(9, ro[24]))
p.inst(MEASURE(10, ro[25]))
p.inst(MEASURE(11, ro[26]))
p.inst(MEASURE(12, ro[27]))
p.inst(MEASURE(13, ro[28]))
p.inst(MEASURE(14, ro[29]))

p.wrap_in_numshots_loop(shots)

qc = get_qc('15q-qvm')
results_list = qc.run(p)
results = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1], ""), results_list))
counts = dict(zip(results,[results.count(i) for i in results]))
print(counts)
