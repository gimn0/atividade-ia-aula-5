# 4 - De posse do script em python da aula 5, faça uma regressão com os seguintes dados:
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [10, -1, 3, 70, 20, 71, 22, 29, 66, 91]
# Ainda avalie com a métrica EQM ou MSE dado pelo módulo e biblioteca de:
# "from sklearn.metrics import mean_squared_error".

# -*- coding: utf-8 -*-
"""Aula_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RIVmnQ7_9QZtESdI7yTTFPp9_0qmjkDZ
"""

# Analise Regressão
# y = alpha + Beta*x  Regressão Linear Simples
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score # r²
from sklearn.metrics import mean_squared_error # mse

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([10, -1, 3, 70, 20, 71, 22, 29, 66, 91])

F = np.polyfit(x, y, 9) # função que encontra o coeficiente de um polinomio

yy = np.polyval(F,x) # saida da função como predição do modelo

plt.plot(x,y,'r*', label= 'Real') # plot dos dados reais
plt.plot(x, yy, 'g--', label = 'Predição')
plt.xlabel('x')
plt.ylabel('y')
plt.title('REGRESSÃO')
plt.show()

r2 = r2_score(y,yy) # calculo do R²
print("r2: ", r2)

mse = mean_squared_error(y,yy) # calculo do erro quadratico médio
print("erro quadrático médio: ", mse)

# rmse = np.sqrt(mse) # calculo da raíz do erro quadratico médio
# print("raíz do erro quadrático médio: ", rmse)