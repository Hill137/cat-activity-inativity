import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hyp2f1
from mpl_toolkits.mplot3d import Axes3D


# Rango de K´s
K_plus = np.linspace(0.001, 10, 200)
K_minus = np.linspace(0.001, 10, 200)

K_plus, K_minus = np.meshgrid(K_plus, K_minus)


# Calcular <C_on>
def C_on(K_plus, K_minus):
    return K_plus/(K_plus+ K_minus)


Z = C_on(K_plus, K_minus)#*(1-C_on(K_plus, K_minus))

# eliminar problemas numéricos
#Z = np.nan_to_num(Z)

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# superficie
ax.plot_surface(K_plus, K_minus, Z,
                cmap='viridis',
                alpha=0.9)


ax.set_xlabel(r'$K_{I}$')
ax.set_ylabel(r'$K_{A}$')
ax.set_zlabel(r'$\langle C_{on} \rangle$')#(r'$Var\{ C_{A} \}$')

ax.view_init(35,45)

plt.show()