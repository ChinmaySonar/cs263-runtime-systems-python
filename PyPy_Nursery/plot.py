import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":
    size = np.array([0.5,1,2,3,4,5,6,7,8,9,10])
    time = np.array([0.02628395,	0.02208972,	0.015576631,	0.013800412,	0.017289698,	0.015239626,	0.014301181,	0.013819277,	0.01297076,	0.01265569,	0.016005367])
    plt.scatter(size, time)
    plt.title("Time spent in gc: benchmark-n_queens.py")
    plt.xlabel("Nursery Size (MB)")
    plt.ylabel("Time (s)")
    plt.savefig("plot.png")
