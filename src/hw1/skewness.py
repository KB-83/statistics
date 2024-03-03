import matplotlib.pyplot as plt
import numpy as np
import statistics

def mode(data):
    mode = statistics.mode(data)
    return mode
def median(data):
    median = statistics.median(data)
    return median

def mean(data):
    mean = statistics.mean(data)
    return mean

# first_pearson_skewness
def fps(data,mean,mode):
    std_dev = np.std(data)
    pearson_skew =  (mean - mode) / std_dev
    return pearson_skew

# second_pearson_skewness
def sps(data,mean,median):
    std_dev = np.std(data)
    pearson_skew = 3 * (mean - median) / std_dev
    return pearson_skew
# Sample data for six arrays

data1 = [-1,1,2,3,3]
x1 = mean(data1)
m1 = median(data1)
M1 = mode(data1)
fps1 = fps(data1,x1,M1)
sps1 = sps(data1,x1,m1)

data2 = [-1,1,2,8,8]
x2 = mean(data2)
m2 = median(data2)
M2 = mode(data2)
fps2 = fps(data2,x2,M2)
sps2 = sps(data2,x2,m2)

data3 = [-15,-1,-1,0,1,2,3]
x3 = mean(data3)
m3 = median(data3)
M3 = mode(data3)
fps3 = fps(data3,x3,M3)
sps3 = sps(data3,x3,m3)


data4 = [-5,-1,-1,0,1,2,3]
x4 = mean(data4)
m4 = median(data4)
M4 = mode(data4)
fps4 = fps(data4,x4,M4)
sps4 = sps(data4,x4,m4)

data5 = [-3,-2,-1,0,1,1,15]
x5 = mean(data5)
m5 = median(data5)
M5 = mode(data5)
fps5 = fps(data5,x5,M5)
sps5 = sps(data5,x5,m5)

data6 = [-1,-1,0,1,15]
x6 = mean(data6)
m6 = median(data6)
M6 = mode(data6)
fps6 = fps(data6,x6,M6)
sps6 = sps(data6,x6,m6)

data = [data1, data2, data3, data4, data5, data6]
means = [x1, x2, x3, x4, x5, x6] 
medians = [m1, m2, m3, m4, m5, m6]
modes = [M1, M2, M3, M4, M5, M6]
fpss = [fps1,fps2,fps3,fps4,fps5,fps6]
spss = [sps1,sps2,sps3,sps4,sps5,sps6]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i in range(6):
    # Plot histogram
    row = i // 3
    col = i % 3
    axs[row, col].hist(data[i], bins=20, color='skyblue', edgecolor='black')
    axs[row, col].set_title('Data {}'.format(i+1))

    # Annotate mean and median on the histogram
    mean_val = means[i]
    median_val = medians[i]
    mode_val = modes[i]
    fps_val = fpss[i]
    sps_val = spss[i]
    axs[row, col].annotate('Mean: {:.2f}'.format(mean_val), xy=(0.5, 0.9), xycoords='axes fraction', ha='center', fontsize=10, color='#4169E1')
    axs[row, col].annotate('Median: {:.2f}'.format(median_val), xy=(0.5, 0.85), xycoords='axes fraction', ha='center', fontsize=10, color='#DC143C')
    axs[row, col].annotate('Mode: {:.2f}'.format(mode_val), xy=(0.5, 0.8), xycoords='axes fraction', ha='center', fontsize=10, color='#50C878')
    axs[row, col].annotate('FPS: {:.2f}'.format(fps_val), xy=(0.5, 0.75), xycoords='axes fraction', ha='center', fontsize=10,  color='#14141E')
    axs[row, col].annotate('SPS: {:.2f}'.format(sps_val), xy=(0.5, 0.7), xycoords='axes fraction', ha='center', fontsize=10,  color='#14141E')

    
    # Add vertical lines for mean, median, and mode
    axs[row, col].axvline(x=mean_val, color='r', linestyle='--', linewidth=2)
    axs[row, col].axvline(x=median_val, color='b', linestyle='--', linewidth=2)
    axs[row, col].axvline(x=mode_val, color='g', linestyle='--', linewidth=2)
plt.tight_layout()
plt.show()