import matplotlib.pyplot as plt

# question 3 part a
data = [180, 176, 176, 175, 173, 173, 172, 171, 170, 169, 168, 166, 165, 193,
        191, 189, 187, 185, 185, 185, 184, 183, 182, 182, 181, 181]

data.sort()

plt.hist(data, bins=5, cumulative=True, edgecolor='black')

plt.xlabel('data')
plt.ylabel('people')
plt.title('cumulative histogram')
plt.show()
