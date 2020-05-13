import sys
import subprocess
from subprocess import PIPE
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":
    result = subprocess.run(sys.argv[1:], stderr=PIPE, encoding="utf-8")
    extracted = re.findall("(?:generation )(\d)(?:.*?)(\d+\.\d+)(?:s elapsed)", result.stderr, re.DOTALL)
    with open("output.txt", "w") as f:
        colors = ["red", "green", "blue"]
        cumul = np.zeros(len(extracted))
        f.write(sys.argv[1])
        f.write("\n")
        for i in range(len(extracted)):
            f.write("{}: {}\n".format(extracted[i][0],extracted[i][1]))
            plt.scatter(i, float(extracted[i][1]), c=colors[int(extracted[i][0])])
            cumul[i] = cumul[i-1] + float(extracted[i][1])
        plt.plot(np.linspace(0, len(extracted)-1, len(extracted)), cumul)
        plt.savefig("plot.png")
