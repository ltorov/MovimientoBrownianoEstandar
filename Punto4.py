
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from Martingale import MartingaleSimulation

def simulations(initial_balance, initial_bet_amount, N=500, max_rounds=None, max_bet_amount=None):
    earnings = np.zeros(N)
    rounds_played = np.zeros(N)
    for i in range(N):
        martingale_simulation = MartingaleSimulation(initial_balance, initial_bet_amount, max_rounds)
        martingale_simulation.simulate()
        balance = martingale_simulation.balance
        rounds_played[i] = martingale_simulation.rounds_played
        earnings[i] = (balance - initial_balance) if (balance > initial_balance)  else 0

    print(stats.describe(earnings), 'median: ', np.median(earnings))
    print(stats.describe(rounds_played), 'median: ', np.median(rounds_played))

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


# A
initial_balance = 500
initial_bet_amount = 10
max_rounds = 50
simulations(initial_balance, initial_bet_amount, max_rounds=max_rounds)

# # B
# initial_balance = 500
# initial_bet_amount = 10

# simulations(initial_balance, initial_bet_amount)

# # C
# initial_balance = 500000
# initial_bet_amount = 10
# max_bet_amount = 500000

# simulations(initial_balance, initial_bet_amount, max_bet_amount = max_bet_amount)