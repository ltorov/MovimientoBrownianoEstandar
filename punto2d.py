from BridgeBrownianMotion import BridgeBrownianMotion
from GeometricBrownianMotion import GeometricBrownianMotion

import statsmodels.api as sm
from scipy.stats.distributions import norm, lognorm
import matplotlib.pyplot as plt
import numpy as np

num_trayectories = 1500
num_steps = 500  # Number of time steps
alpha = 0.5
lamda = 0.05

geometric_brownian_motion = GeometricBrownianMotion(num_trayectories, num_steps, max_time=1, alpha=alpha, lamda=lamda)
bridge_brownian_motion = BridgeBrownianMotion(num_trayectories, num_steps)
geometric_brownian_motion.generate_geometric_brownian_motion()
bridge_brownian_motion.generate_bridge_brownian_motion()
Bt = geometric_brownian_motion.geometric_brownian_motions
Br = bridge_brownian_motion.bridge_brownian_motions


final_g = []
final_b = []
for i in range(len(Br)):
    final_g.append(np.mean(Bt[i]))
    final_b.append(np.mean(Br[i]))


# # Create Q-Q plot
# fig, ax = plt.subplots()
# sm.qqplot(flattened_data, dist=lognorm, line='45', ax=ax)
# ax.set_title('Q-Q Plot of Geometric Brownian Motion')
# plt.show()


# Create histogram
plt.hist(final_b, bins=50, density=True, color='blue', alpha=0.7)
plt.title('Histogram of Geometric Brownian Motion')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Optionally, overlay the theoretical log-normal distribution for comparison
# mu_lognormal = (alpha - 0.5 * lamda**2) * 1
# sigma_lognormal = lamda * np.sqrt(1)
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = (1/(x * sigma_lognormal * np.sqrt(2 * np.pi))) * np.exp(-(np.log(x) - mu_lognormal)**2 / (2 * sigma_lognormal**2))
# plt.plot(x, p, 'k', linewidth=2)

plt.show()

