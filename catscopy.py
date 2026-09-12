import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hyp2f1
from mpl_toolkits.mplot3d import Axes3D

# Parámetros fijos
K_plus = 1.0
K_minus = 2.0

a = K_plus/(K_plus+ K_minus)
# Rango de sigma
sigma_plus = np.linspace(0.01, 1, 200)
sigma_minus = np.linspace(0.01, 1, 200)

S_plus, S_minus = np.meshgrid(sigma_plus, sigma_minus)


# Calcular <C_on>
def C_on(S_plus, S_minus):
    l1= (K_plus+ K_minus)
    return K_plus/l1 + ((K_plus*S_minus - K_minus*S_plus)/l1**3)*(1- (S_plus+ S_minus)/l1**2 )**(-1.5) 


Z = C_on(S_plus, S_minus)/a

# eliminar problemas numéricos
#Z = np.nan_to_num(Z)

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# superficie
ax.plot_surface(S_plus, S_minus, Z,
                cmap='viridis',
                alpha=0.9)

# plano Z = 1
#Z_plane = np.ones_like(Z)
#ax.plot_surface(S_plus, S_minus, Z_plane,
         #       color='red',
          #      alpha=0.25)

# curva de intersección
mask = np.isclose(Z, 1, atol=0.02)

ax.scatter(S_plus[mask],
           S_minus[mask],
           Z[mask],
           color='black',
           s=3)

ax.set_xlabel(r'$\sigma_{1,+}$')
ax.set_ylabel(r'$\sigma_{1,-}$')
ax.set_zlabel(r'$\langle C_{on} \rangle$')

ax.view_init(35,45)

plt.show()