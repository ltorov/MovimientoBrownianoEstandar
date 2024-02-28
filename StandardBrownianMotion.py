import numpy as np
import matplotlib.pyplot as plt


class StandardBrownianMotion:
    def __init__(self, num_trayectories, num_steps, max_time=1):
        self.num_trayectories = num_trayectories
        self.num_steps = num_steps
        self.dt = max_time/num_steps
        self.t = np.linspace(0, max_time, num_steps)
        self.brownian_motions = None

    def generate_brownian_motion(self):
        brownian_motions = np.zeros((self.num_trayectories, self.num_steps))

        for i in range(self.num_trayectories):
            for j in range(1, self.num_steps):
                brownian_motions[i, j] = brownian_motions[i, j-1] + np.random.normal(0, np.sqrt(self.dt))

        self.brownian_motions = brownian_motions

    def plot(self):
        for i in range(len(self.brownian_motions)):
            plt.plot(self.t, self.brownian_motions[i, :])
        plt.title('Movimiento Browniano Estándar')
        plt.xlabel('Tiempo')
        plt.show()

# # Parameters
# num_trayectories = 1000
# num_steps = 365  # Number of time steps

# # Generate Brownian motion
# brownian_motion = StandardBrownianMotion(num_trayectories, num_steps, max_time=1/4)
# brownian_motion.generate_brownian_motion()
# brownian_motion.plot()
