# Running Nursery Tests

To visualize nurseryTest.py, run `PYPY_GC_NURSERY=<Nursery Size> <python implementation> <path to visualizer.py> <PyPy Implementation> <path to nurseryTest.py>`. \<Nursery Size\> should be the number of megabytes the nursery will be. 

nursery.sh can also be run to test nurseryTest.py 16 times. It is recommended you comment out all the plotting in visualizer.py to reduce the time required.