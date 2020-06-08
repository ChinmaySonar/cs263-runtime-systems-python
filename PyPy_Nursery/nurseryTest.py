import gc
import platform
from sys import stderr

class A:
    def __init__(self):
        self.A = self 
        self.waste = bytearray(1024)

class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, "\n", file=stderr, flush=True)
        global m
    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, "\n", file=stderr, flush=True)

    def on_gc_collect(self, stats):
        self.done = True


if __name__=='__main__':
    imp = platform.python_implementation()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        gc.set_debug(gc.DEBUG_STATS)

    for i in range(100):
        l1 = [A() for l in range(100000)]
        for j in range(10000):
            a = A()
            a = None
        l1 = None

    gc.collect()
    
    if imp == "PyPy":
        # print(gc.get_stats())
        pass
    elif imp == "CPython":
        gc.set_debug(0)
    