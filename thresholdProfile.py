import gc
import timeit

class A:
    def __init__(self):
        self.B = B(self)    

class B:
    def __init__(self, A):
        self.A = A

gc.set_debug(gc.DEBUG_SAVEALL)

def testThreshold(t0=700, t1=10, t2=10):
    gc.set_threshold(t0, t1, t2)
    for i in range(1000000):
        a = A()
    gc.collect()

# For some reason the for loop always gets slower each iteration not sure why

#Testing garbage collection at different 0 generation thresholds
# for i in range(20, -1, -1):
#     gc.collect()
#     print("i =", 2**i)
#     n = timeit.timeit(stmt="testThreshold({0})".format(2**i), setup="from __main__ import testThreshold; gc.enable()", number=1)
#     print(n)

print(timeit.timeit(stmt="testThreshold({0})".format(1), setup="from __main__ import testThreshold; gc.enable()", number=1))