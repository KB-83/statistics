import numpy as np
import matplotlib.pyplot as plt

n = 30# Sample size
num_samples = 10000
mu = 50
lb = 0
ub = 100

random_vars = np.random.uniform(lb, ub, (num_samples, n))
sample_means = np.mean(random_vars, axis=1)
# variance of uniform distribution 0 to 100 is 2500/3
variance = 2500/3
Z = (sample_means - mu) / (np.sqrt(variance) / np.sqrt(n))

plt.hist(Z, bins=30, density=True, edgecolor='black', alpha=0.7)

x = np.linspace(-3, 3, 1000)
standard_normal = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, standard_normal, color='red', linestyle='dashed')

plt.legend()
plt.grid(True)
plt.show()
