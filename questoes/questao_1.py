# 1- Faça o calculo da distancia de chebyshev dos objetos A(1, 3, 4) e (2, 2, 2)?

import numpy as np

a = np.array([1, 3, 4])
b = np.array([2, 2, 2])

cheb = max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

print("distância de chebyshev: ", cheb) # dist. de chebyshev = 2