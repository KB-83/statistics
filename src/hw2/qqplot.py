import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

mu = 0
sigma = 2
X = np.random.normal(mu,sigma**2,1000)
Y = (X-mu)/sigma

# Create Q-Q plot
fig, ax = plt.subplots()
sm.qqplot_2samples(X, Y,ax = ax)
ax.plot(2,1,'ro')
ax.legend()

ax.set_title('Q-Q Plot of Variable 1 vs. Variable 2')

plt.show()
