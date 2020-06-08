import gc
from guppy import hpy

# python3 guppyTest.py
# pypy3 guppyTest.py
# guppy dumps the heap, but does not track garbage objects
# it also seems to call gc.collect within heap()

h=hpy()


class A:
    def __init__(self):
        self.A = self

def dumpHeap(phase, info):
    print("heap at gc", phase)
    print()
    print(h.heap())
    print(info)
    print()
    print()

if __name__ == '__main__':
    gc.disable()
    gc.callbacks.append(dumpHeap)
    l = []

    for i in range(100000):
        l.append(A())
    print(h.heap())
    l = None
    gc.collect()
    gc.callbacks=[]
    