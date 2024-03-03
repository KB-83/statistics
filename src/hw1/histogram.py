import matplotlib.pyplot as plt
import numpy as np

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
