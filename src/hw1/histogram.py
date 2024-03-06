import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Your data
data = [180, 176, 176, 175, 173, 173, 172, 171, 170, 169, 168, 166, 165, 193,
        191, 189, 187, 185, 185, 185, 184, 183, 182, 182, 181, 181]

# Define custom bin edges
bin_edges = np.arange(160, 196, 5)  # Start at 160, end at 185, with bin width 5

plt.hist(data, bins=bin_edges, cumulative=True, edgecolor='black')

plt.xlabel('data')
plt.ylabel('people')
plt.title('cumulative histogram')
plt.show()



def mean_root(data, r):
    n = len(data)
    if r > 0:
        mean_root = (np.sum(np.abs(data)**r * 1/n))**(1/r)
    elif r < 0:
        mean_root = 1/((np.sum((1/(np.abs(data)**-r)) * 1/n))**(-1/r))
    else:
        mean_root = stats.gmean(data)
    return mean_root

print("Mean Root for -1:", mean_root(data,-1))
print("Mean Root for 0:", mean_root(data,0))
print("Mean Root for 1:", mean_root(data,1))
print("Mean Root for 2:", mean_root(data,2))

