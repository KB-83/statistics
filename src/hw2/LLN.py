import numpy as np

X1 = np.random.uniform(1,100,100)
X2= np.random.uniform(1,100,1000)
X3 = np.random.uniform(1,100,10000)
X4 = np.random.uniform(1,100,100000)
X5 = np.random.uniform(1,100,1000000)
X6 = np.random.uniform(1,100,10000000)


mean1 = np.mean(X1)
mean2 = np.mean(X2)
mean3 = np.mean(X3)
mean4 = np.mean(X4)
mean5 = np.mean(X5)
mean6 = np.mean(X6)


print(mean1,"-> 100")
print(mean2,"-> 1000")
print(mean3,"-> 10000")
print(mean4,"-> 100000")
print(mean5,"-> 1000000")
print(mean6,"-> 10000000")
