import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# میانگین و واریانس
mu = 0
sigma = 1

# تولید داده‌های تصادفی از توزیع نرمال
np.random.seed(0)
X = np.random.normal(mu, sigma, 1000)

# محاسبه متغیر Y = X - μ
Y = X - mu

# مرتب‌سازی داده‌ها
X_sorted = np.sort(X)
Y_sorted = np.sort(Y)

# محاسبه percentiles
percentiles = np.linspace(0, 100, 100)
X_percentiles = np.percentile(X_sorted, percentiles)
Y_percentiles = np.percentile(Y_sorted, percentiles)

# رسم نمودار QQ-plot
plt.figure(figsize=(8, 6))
plt.scatter(X_percentiles, Y_percentiles, color='blue')
plt.plot([-3, 3], [-3, 3], color='red', linestyle='--')  # خط مورب برای مقایسه
plt.xlabel('Theoretical Quantiles of X')
plt.ylabel('Theoretical Quantiles of Y')
plt.title('QQ Plot for X and Y')
plt.grid(True)
plt.show()
