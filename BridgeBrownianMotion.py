import numpy as np
import matplotlib.pyplot as plt

from StandardBrownianMotion import StandardBrownianMotion

class BridgeBrownianMotion:
    def __init__(self, num_trayectories, num_steps, max_time=1):
        self.num_trayectories = num_trayectories
        self.num_steps = num_steps
        self.dt = max_time/num_steps
        self.t = np.linspace(0, max_time, num_steps)
        self.bridge_brownian_motions = None

    def generate_bridge_brownian_motion(self):
        standard_brownian_motion = StandardBrownianMotion(self.num_trayectories, self.num_steps, max_time=1)
        standard_brownian_motion.generate_brownian_motion()
        brownian_motions = standard_brownian_motion.brownian_motions

        bridge_brownian_motions = np.zeros((self.num_trayectories, self.num_steps))

        for i in range(self.num_trayectories):
            for j in range(1, self.num_steps):
                bridge_brownian_motions[i, j] = brownian_motions[i, j] - self.t[j]*brownian_motions[i, -1]

        self.bridge_brownian_motions = bridge_brownian_motions

    def plot(self):
        for i in range(len(self.bridge_brownian_motions)):
            plt.plot(self.t, self.bridge_brownian_motions[i, :])
        plt.title('Movimiento Browniano Bridge')
        plt.xlabel('Tiempo')
        plt.show()


# Parameters
num_trayectories = 1000
num_steps = 365  # Number of time steps

# Generate Brownian motion
bridge_brownian_motion = BridgeBrownianMotion(num_trayectories, num_steps, max_time=1)
bridge_brownian_motion.generate_bridge_brownian_motion()
bridge_brownian_motion.plot()
