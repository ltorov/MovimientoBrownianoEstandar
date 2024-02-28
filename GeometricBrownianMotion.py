import numpy as np
import matplotlib.pyplot as plt

from StandardBrownianMotion import StandardBrownianMotion


class GeometricBrownianMotion:
    def __init__(self, num_trayectories, num_steps, max_time=1, alpha=0.5, lamda=0.2):
        self.num_trayectories = num_trayectories
        self.num_steps = num_steps
        self.dt = max_time/num_steps
        self.t = np.linspace(0, max_time, num_steps)
        self.geometric_brownian_motions = None
        self.alpha = alpha
        self.lamda = lamda

    def generate_geometric_brownian_motion(self):
        standard_brownian_motion = StandardBrownianMotion(self.num_trayectories, self.num_steps, max_time=1)
        standard_brownian_motion.generate_brownian_motion()
        brownian_motions = standard_brownian_motion.brownian_motions

        geometric_brownian_motions = np.ones((self.num_trayectories, self.num_steps))

        for i in range(self.num_trayectories):
            for j in range(1, self.num_steps):
                geometric_brownian_motions[i, j] = np.exp(self.alpha*self.t[j] + self.lamda*brownian_motions[i, j])

        self.geometric_brownian_motions = geometric_brownian_motions

    def plot(self):
        for i in range(len(self.geometric_brownian_motions)):
            plt.plot(self.t, self.geometric_brownian_motions[i, :])
        plt.title('Movimiento Browniano Geométrico')
        plt.xlabel('Tiempo')
        plt.show()


# # Parameters
# num_trayectories = 1000
# num_steps = 365  # Number of time steps

# # Generate Brownian motion
# geometric_brownian_motion = GeometricBrownianMotion(num_trayectories, num_steps, max_time=1, alpha=0.5, lamda=0.5)
# geometric_brownian_motion.generate_geometric_brownian_motion()
# geometric_brownian_motion.plot()
