import numpy as np
from math import pi, sin, cos


def DFT(coeffs):
    n = len(coeffs)
    if n <= 1:
        return coeffs
    A0 = DFT(coeffs[0:: 2])
    A1 = DFT(coeffs[1:: 2]) * np.array([(cos(2 * pi * k / n) + 1j * sin(2 * pi * k / n))
                                        for k in range(n // 2)])
    return np.hstack((A0 + A1, A0 - A1))


coeffs = list(map(float, input().strip().split()))
result = DFT(coeffs)
print(' '.join(f'{x.real},{x.imag}' for x in result))