from StandardBrownianMotion import StandardBrownianMotion
import numpy as np
import matplotlib.pyplot as plt

def distributional_properties(motion):
    
    return 


def distributional_properties(motion_a, motion_b):
    mean = np.mean(motion_a)
    variance = np.var(motion_a)
    covariance = np.cov(motion_a, motion_b)
    correlation = np.corrcoef(motion_a, motion_b)
    return mean, variance,covariance, correlation


def main():
    num_trayectories = 1
    num_steps = 500
    sigma = 0.4

    brownian_motion = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion.generate_brownian_motion()
    Bt = brownian_motion.brownian_motion
    Wt_a = Bt**3 - np.exp(sigma * Bt)
    brownian_motion = StandardBrownianMotion(num_trayectories, num_steps)
    brownian_motion.generate_brownian_motion()
    Bt = brownian_motion.brownian_motion
    Wt_b = Bt**3 - np.exp(sigma * Bt)

    mean, variance, covariance, correlation = distributional_properties(Wt_a, Wt_b)
    print(mean, variance, covariance, correlation)

main()