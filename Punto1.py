
import numpy as np
import matplotlib.pyplot as plt
from StandardBrownianMotion import StandardBrownianMotion

num_trayectories = 10000
num_steps = 50

brownian_motions = StandardBrownianMotion(num_trayectories, num_steps, max_time=1/4)
brownian_motions.generate_brownian_motion()
Bt = brownian_motions.brownian_motions

t = brownian_motions.t

theoretical = np.zeros(num_steps)
experimental = np.zeros(num_steps)

for step in range(1, num_steps):
    theoretical[step] = (1-4*t[step])**(-1/2)
    # print(np.size(Bt[:,step]))
    experimental[step] = np.mean(np.exp(2*(Bt[:, step]**2)), axis=0)

plt.plot(t, theoretical, label='Teórico', color='#FFD699', linewidth=4)
plt.plot(t, experimental, label='Experimental',  color='#C8D5FA', linewidth=3)
plt.xlabel('Tiempo')
plt.legend()
plt.title('Simulación Movimiento Browniano Estándar(50 pasos)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
