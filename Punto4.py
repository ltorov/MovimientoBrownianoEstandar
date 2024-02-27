from Martingale import MartingaleSimulation
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# A
initial_balance = 500
initial_bet_amount = 10
max_rounds = 50
N = 500
earnings = np.zeros(500)
rounds_played = np.zeros(500)
for i in range(N):
    martingale_simulation = MartingaleSimulation(initial_balance, initial_bet_amount, max_rounds)
    martingale_simulation.simulate()
    balance = martingale_simulation.balance
    rounds_played[i] = martingale_simulation.rounds_played
    earnings[i] = (balance - initial_balance) if (balance > initial_balance)  else 0

print(stats.describe(earnings))
print(np.median(earnings))
# Plotting the results
plt.hist(earnings, bins=10, color='blue', edgecolor='black')
plt.xlabel('Earnings')
plt.title('Martingale Simulation')
plt.show()

# Plotting the results
plt.hist(rounds_played, bins=10, color='blue', edgecolor='black')
plt.xlabel('Rounds Played')
plt.title('Martingale Simulation')
plt.show()

