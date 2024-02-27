import random
import matplotlib.pyplot as plt


class MartingaleSimulation:
    def __init__(self, initial_balance, initial_bet_amount, max_rounds):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.bet_amount = initial_bet_amount
        self.max_rounds = max_rounds
        self.rounds_played = 0
        self.history = []
        self.bet_history = []

    def flip_coin(self):
        return random.choice([0, 1])

    def play_round(self):
        outcome = self.flip_coin()
        if outcome == 1:
            self.balance += self.bet_amount
            self.bet_amount = initial_bet_amount  # Reset bet amount after winning
        else:
            self.balance -= self.bet_amount
            self.bet_amount *= 2

        self.rounds_played += 1
        self.history.append(self.balance)

    def simulate(self):
        while self.balance> 0 and self.rounds_played < self.max_rounds:
            self.bet_history.append(self.bet_amount)
            if self.balance - self.bet_amount >0:
                self.play_round()
            else:
                self.bet_amount = initial_bet_amount
                self.play_round()

# Example Usage:
initial_balance = 500000
initial_bet_amount = 10000
max_rounds = 50

martingale_simulation = MartingaleSimulation(initial_balance, initial_bet_amount, max_rounds)
martingale_simulation.simulate()

# Plotting the results
plt.plot(range(1, martingale_simulation.rounds_played + 1), martingale_simulation.history)
plt.xlabel('Rounds')
plt.ylabel('Balance')
plt.title('Martingale Simulation')
plt.show()

# Plotting the results
plt.plot(range(1, martingale_simulation.rounds_played + 1), martingale_simulation.bet_history)
plt.xlabel('Rounds')
plt.ylabel('Bets')
plt.title('Martingale Simulation')
plt.show()