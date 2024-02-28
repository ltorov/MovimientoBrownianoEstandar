from StandardBrownianMotion import StandardBrownianMotion
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, kendalltau


def test_independence(bm1, bm2):
    pearson_corr = np.zeros(bm1.shape[0])
    kendall_tau = np.zeros(bm1.shape[0])

    for i in range(bm1.shape[0]):
        pearson_corr[i] = pearsonr(bm1[i], bm2[i]).pvalue
        kendall_tau[i] = kendalltau(bm1[i], bm2[i]).pvalue
        print(kendalltau(bm1[i], bm2[i]))
        # print(pearson_corr[i])

    return pearson_corr, kendall_tau


def main():
    num_trayectories = 1000
    num_steps = 500

    brownian_motion = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion.generate_brownian_motion()
    Bt = brownian_motion.brownian_motions
    t = brownian_motion.t

    brownian_motion1 = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion1.generate_brownian_motion()
    Bs = brownian_motion1.brownian_motions

    lags = np.linspace(1, 5, 5, dtype="int")

    back_cases = []
    for lag in lags:
        print(lag)
        Ws = np.zeros((num_trayectories, num_steps))
        # print(Ws)
        for time in range(lag, num_steps):
            s = time - lag
            final_array = Bs[s] - (s / time) * Bt[time]
            Ws[s] = final_array
        pearson_corr, kendall_tau = test_independence(Bt, Ws)
        mean_pearson_corr = np.mean(pearson_corr)
        mean_kendall_tau = np.mean(kendall_tau)
        print(Ws)
        print(Bt)
        print("Mean Pearson correlation coefficient:", mean_pearson_corr)
        print("Mean Kendall tau rank correlation coefficient:", mean_kendall_tau)

    # Ws = Bs-(s/t)*Bt
    # for step in range(1, num_steps):
    #     np.mean(Bt[step, :]-np.mean(Bt[step, :])*())


main()
