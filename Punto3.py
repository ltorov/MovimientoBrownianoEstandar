import numpy as np
from scipy.stats import chi2_contingency

import matplotlib.pyplot as plt

# Parameters
T = 1.0  # Total time
N = 1000  # Number of time steps
dt = T / N  # Time step

# Simulate Brownian motions
tiempos = np.linspace(0, T, N)
covs = []
corrs = []
Chi2 = []
P = []
Dof = []

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

    # Create a contingency table from the two arrays
    contingency_table = np.column_stack((np.abs(Bt), np.abs(W3)))

    # Perform the Chi-squared test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    Chi2.append(chi2)
    P.append(p)
    Dof.append(dof)

# Print the results
print(f"Chi-squared statistic: {np.mean(Chi2)}")
print(f"P-value: {np.mean(P)}")
print(f"Degrees of freedom: {np.mean(Dof)}")
print(f"Mean covariance: {np.mean(covs):.10f}")
print(f"Mean correlation: {np.mean(corrs):.10f}")

plt.plot(Chi2, color = '#C8D5FA', linewidth=4)
plt.xlabel('Tiempo')
plt.ylabel('Chi2')
plt.legend()
plt.title('Estadístico Prueba de Independencia Chi2')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


plt.plot(corrs, label = 'Correlación', color = '#FFD699', linewidth=4)
plt.plot(covs, label = 'Covarianza', color = '#C8D5FA', linewidth=3)
plt.xlabel('Tiempo')
plt.legend()
plt.title('Covarianza y Correlación Promedio')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()