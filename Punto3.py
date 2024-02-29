import numpy as np

# Parameters
T = 1.0  # Total time
N = 1000  # Number of time steps
dt = T / N  # Time step

# Simulate Brownian motions
tiempos = np.linspace(0, T, N)
covs = []
corrs = []

for _ in range(500):
    dBs = np.sqrt(dt) * np.random.randn(N)
    dBt = np.sqrt(dt) * np.random.randn(N)
    Bs = np.cumsum(dBs)
    Bt = np.cumsum(dBt)
    W3 = np.zeros(N)

    for t in range(1, N):
        s = int(np.random.uniform(0, t))
        W3[t] = Bs[s] - (s/t)*Bt[t]

    # Compute increments
    delta_Bt = np.diff(Bt)
    delta_W3 = np.diff(W3)

    # Check covariance (approximate independence)
    covariance = np.cov(delta_Bt, delta_W3)[0, 1]
    correlation = np.corrcoef(delta_Bt, delta_W3)[0, 1]
    covs.append(covariance)
    corrs.append(correlation)

print(f"Mean covariance: {np.mean(covs):.10f}")
print(f"Mean correlation: {np.mean(corrs):.10f}")
