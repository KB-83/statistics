import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

mu = 4
sigma = 2
X = np.random.normal(mu,sigma**2,1000)
Y = (X-mu)/sigma


fig, ax = plt.subplots()
sm.qqplot_2samples(X, Y,ax = ax)

plt.show()
