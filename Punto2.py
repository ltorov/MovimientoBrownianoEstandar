import numpy as np
import math
from StandardBrownianMotion import StandardBrownianMotion
from BridgeBrownianMotion import BridgeBrownianMotion
from GeometricBrownianMotion import GeometricBrownianMotion
import matplotlib.pyplot as plt
import random


def distributional_properties(motion_a):
    mean = np.mean(motion_a, axis=0)
    variance = np.var(motion_a, axis=0)
    # covariance = np.cov(motion_a, motion_b)
    # correlation = np.corrcoef(motion_a, motion_b)
    return mean, variance  # , covariance, correlation


def plot_compare_theoric_real(
    t, real_values, theoric_values, compared_value, type_of_motion
):
    plt.plot(t, real_values, label=compared_value, color="blue", marker="o")
    plt.plot(
        t,
        theoric_values,
        label="Theoretical " + compared_value,
        color="red",
        marker="x",
    )

    plt.xlabel("Time")
    plt.ylabel("Mean")
    plt.title(
        f"Comparison of {compared_value} and Theoretical {compared_value} over Time for {type_of_motion}"
    )
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    geometric()
    bridge()
    brown_modification()


def geometric():
    num_trayectories = 1500
    num_steps = 500  # Number of time steps
    alpha = 0.5
    lamda = 0.5

    geometric_brownian_motion = GeometricBrownianMotion(
        num_trayectories, num_steps, max_time=1, alpha=0.5, lamda=0.5
    )
    geometric_brownian_motion.generate_geometric_brownian_motion()
    Bt_a = geometric_brownian_motion.geometric_brownian_motions
    t = geometric_brownian_motion.t
    t_rand = random.randrange(1, num_steps + 1)
    s_rand = random.randrange(1, num_steps + 1)

    covarianza_gr = np.cov(Bt_a[:, t_rand - 1], Bt_a[:, s_rand - 1])
    covariance = covarianza_gr[0][1]

    mean, variance = distributional_properties(Bt_a)
    theoric_mean = np.exp(alpha * t)
    theoric_variance = np.exp(2 * (alpha * t)) * (
        np.exp((lamda**2) * t) - np.ones(len(t))
    )
    theoric_covariance = np.exp(2 * alpha * (1 / s_rand + 1 / t_rand)) * (
        np.exp(min(1 / t_rand, 1 / s_rand) * (lamda**2)) - 1
    )

    plot_compare_theoric_real(t, mean, theoric_mean, "Mean", "Geometric")
    plot_compare_theoric_real(t, variance, theoric_variance, "Variance", "Geometric")
    # plot_compare_theoric_real(
    #     t, covariance, theoric_covariance, "Covariance", "Geometric"
    # )
    print("For the brownian motion modification:")
    print(f"The covariance is: {covariance}")
    print(f"The theoric covariance is: {theoric_covariance}")
    # print(f"The correlation is: {len(correlation[0])}")


def bridge():
    num_trayectories = 1500
    num_steps = 500

    bridge_brownian_motion = BridgeBrownianMotion(
        num_trayectories, num_steps, max_time=1
    )
    bridge_brownian_motion.generate_bridge_brownian_motion()
    Bt_a = bridge_brownian_motion.bridge_brownian_motions
    bridge_brownian_motion = BridgeBrownianMotion(
        num_trayectories, num_steps, max_time=1
    )
    bridge_brownian_motion.generate_bridge_brownian_motion()
    Bt_b = bridge_brownian_motion.bridge_brownian_motions
    t = bridge_brownian_motion.t

    mean, variance, covariance, correlation = distributional_properties(Bt_a, Bt_b)
    theoric_mean = 0 * t
    theoric_variance = (t) * (np.ones(len(t)) - (t))

    plot_compare_theoric_real(t, mean, theoric_mean, "Mean", "Bridge")
    plot_compare_theoric_real(t, variance, theoric_variance, "Variance", "Bridge")
    print("For the brownian motion modification:")
    print(f"The covariance is: {covariance}")
    print(f"The correlation is: {correlation}")


def brown_modification():
    num_trayectories = 1500
    num_steps = 500
    sigma = 0.4

    brownian_motion = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion.generate_brownian_motion()
    Bt = brownian_motion.brownian_motions
    Wt_a = Bt**3 - np.exp(sigma * Bt)
    brownian_motion = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion.generate_brownian_motion()
    Bt = brownian_motion.brownian_motions
    Wt_b = Bt**3 - np.exp(sigma * Bt)
    t = brownian_motion.t

    mean, variance, covariance, correlation = distributional_properties(Wt_a, Wt_b)
    theoric_mean = -np.exp(((sigma**2) * t) / 2)
    theoric_variance = (
        15 * (t**3) + np.exp(((sigma**2) * t) * 2) + (np.exp((sigma**2) * t)) - 2
    )
    plot_compare_theoric_real(
        t, mean, theoric_mean, "Mean", "Ws = Bs^3 - e^(sigma * s)"
    )
    plot_compare_theoric_real(
        t, variance, theoric_variance, "Variance", "Ws = Bs^3 - e^(sigma * s)"
    )
    print("For the brownian motion modification:")
    print(f"The covariance is: {covariance}")
    print(f"The correlation is: {correlation}")


main()
