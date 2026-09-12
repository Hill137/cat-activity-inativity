import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hyp2f1

# Parámetros
K_plus = 1.0
K_minus = 2.0

a = K_plus/(K_plus+ K_minus)

# Rango de sigmas
sigma_plus = np.linspace(0.01, 1, 200)
sigma_minus = np.linspace(0.01, 1, 200)

S_plus, S_minus = np.meshgrid(sigma_plus, sigma_minus)

# Calcular alphas
alpha_plus = K_plus / S_plus
alpha_minus = K_minus / S_minus

# argumento de la hipergeométrica
z = 1 - (S_plus / S_minus)

def C_on(alpha_minus, alpha_plus, z):
    
    l1 = alpha_plus / (alpha_plus + alpha_minus)

    # valor general
    val = l1 * hyp2f1(1, alpha_minus, alpha_plus + alpha_minus + 1, z)

    # manejar el caso z=0
    val = np.where(np.abs(z) < 1e-12, l1, val)

    return val

# calcular superficie
Z = C_on(alpha_minus, alpha_plus, z)/a

# crear plano Z=1
Z_plane = np.ones_like(S_plus)



# gráfica
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# dibujar el plano
#ax.plot_surface(S_plus, S_minus, Z_plane, 
               # color='green', alpha=0.09)

# curva de intersección
mask = np.isclose(Z, 1, atol=0.02)

ax.scatter(S_plus[mask],
           S_minus[mask],
           Z[mask],
           color='black',
           s=2)

ax.plot_surface(S_plus, S_minus, Z, cmap='viridis')

ax.set_xlabel(r'$\sigma_{I}$',fontsize=15)
ax.set_ylabel(r'$\sigma_{A}$',fontsize=15)
ax.set_zlabel(r'$\frac{\langle C_{A} \rangle_{pf}}{\langle C_{A} \rangle}$',fontsize=15)


plt.show()