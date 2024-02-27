from StandardBrownianMotion import StandardBrownianMotion
import numpy as np
import matplotlib.pyplot as plt

num_trayectories = 1000
num_steps = 500

brownian_motions = StandardBrownianMotion(num_trayectories, num_steps, max_time=1/4)
brownian_motions.generate_brownian_motion()

t = brownian_motions.t

diffs = np.zeros(num_steps)

for step in range(1, num_steps):
    diffs[step] = (1-4*t[step])**(-1/2)-np.mean(np.exp(2*brownian_motions.brownian_motions[step, :]**2))

plt.plot(t, diffs)
plt.show()
