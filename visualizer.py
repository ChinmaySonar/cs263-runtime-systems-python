import sys
import subprocess
from subprocess import PIPE
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np

if __name__=="__main__":
    result = subprocess.run(sys.argv[1:], stderr=PIPE, encoding="utf-8")
    legend = []
    if sys.argv[1] == "python3":
        extracted = re.findall("(?:generation )(\d)(?:.*?)(\d+\.\d+)(?:s elapsed)", result.stderr, re.DOTALL)
        legend = [mpatches.Patch(color="red", label="gen0"), 
            mpatches.Patch(color="green", label="gen1"), 
            mpatches.Patch(color="blue", label="gen2"),
            Line2D([0], [0], label="cumulative")]
    elif sys.argv[1] == "pypy3":
        extracted = re.findall("(\d)(?:: )([\w\-\.]*)", result.stderr)
        legend = [mpatches.Patch(color="red", label="minor"), 
            mpatches.Patch(color="green", label="major-step"),
            Line2D([0], [0], label="cumulative")]
    with open("output.txt", "w") as f:
        colors = ["red", "green", "blue"]
        cumul = np.zeros(len(extracted))
        f.write(sys.argv[1])
        f.write("\n")
        for i in range(len(extracted)):
            f.write("{}: {}\n".format(extracted[i][0],extracted[i][1]))
            plt.scatter(i, float(extracted[i][1]), s=1, c=colors[int(extracted[i][0])])
            cumul[i] = cumul[i-1] + float(extracted[i][1])
        plt.title(sys.argv[1])
        plt.xlabel("Collection Number")
        plt.ylabel("Time")
        plt.legend(handles=legend)
        plt.plot(np.linspace(0, len(extracted)-1, len(extracted)), cumul)
        plt.savefig("plot.png")
        print(cumul[-1])
