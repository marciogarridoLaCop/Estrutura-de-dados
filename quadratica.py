import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return 2*x**2 + 2*x - 6

# Calculando as raízes usando a fórmula quadrática
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)
    return x1, x2

# Valores de a, b e c
a = 2
b = 2
c = -6

# Calculando as raízes
x1, x2 = calcular_raizes(a, b, c)

# Gerando valores para x
x = np.linspace(-5, 5, 400)

# Gerando valores para y
y = f(x)

# Plotando o gráfico
plt.figure(figsize=(8,6))
plt.plot(x, y, label="y = 2x^2 + 2x - 6", color="blue")
plt.scatter([x1, x2], [f(x1), f(x2)], color="red")  # Plotando os pontos das raízes
plt.text(x1, f(x1)+2, f'x1 = {x1:.3f}', horizontalalignment='center', color="red")  # Legenda da primeira raiz
plt.text(x2, f(x2)-4, f'x2 = {x2:.3f}', horizontalalignment='center', color="red")  # Legenda da segunda raiz
plt.title("Gráfico de y = 2x^2 + 2x - 6")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()
