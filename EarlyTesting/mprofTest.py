import gc
from memory_profiler import profile

# installed memory_profiler
# to profile:
#   mprof run compare.py
#   mprof run pypy3 compare.py
# to plot:
#   mprof plot

class A:
    def __init__(self):
        self.largeArray = bytearray(100000)

    def setCycle(self):
        self.A = self  

if __name__ == '__main__':
    print(gc.get_stats())

    for i in range(1000000):
        a2 = A()
        a2.setCycle()
        a2 = None

    print(gc.get_stats())
    