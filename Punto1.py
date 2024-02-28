from StandardBrownianMotion import StandardBrownianMotion
import numpy as np
import matplotlib.pyplot as plt

num_trayectories = 1000
num_steps = 5000

brownian_motions = StandardBrownianMotion(num_trayectories, num_steps, max_time=1)
brownian_motions.generate_brownian_motion()
Bt = brownian_motions.brownian_motions

t = brownian_motions.t

teorical = np.zeros(num_steps)
experimental = np.zeros(num_steps)

for step in range(1, num_steps):
    teorical[step] = (1-4*t[step])**(-1/2)
    print(np.size(Bt[:,step]))
    experimental[step] = np.mean(np.exp(2*(Bt[:, step]**2)))

plt.plot(t, teorical, label = 'Teórico', color= '#FFD699')
plt.plot(t, experimental, label = 'Experimental',  color= '#C8D5FA')
plt.xlabel('Número de Jugadas')
plt.ylabel('Ocurrencias')
plt.title('Distribución de Número de Jugadas')
plt.grid(True, linestyle='--', alpha=0.5) 
plt.show()
