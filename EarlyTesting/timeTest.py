import gc
import platform
from sys import stderr

# python3 timeTest.py
# pypy3 timeTest.py
# pypy seems to take a shorter time but I couldn't understand the memory values it prints, 
# so idk if it's collecting the same objects

class A:
    def __init__(self):
        self.A = self  

class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, file=stderr)

    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, file=stderr)
        pass

    def on_gc_collect(self, stats):
        self.done = True


if __name__=='__main__':
    imp = platform.python_implementation()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        gc.set_debug(gc.DEBUG_STATS)

    l1 = [A() for l in range(100000)]
    for j in range(100000):
        a = A()
        a = None
    l1 = None

    gc.collect()
    
    if imp == "PyPy":
        # print(gc.get_stats())
        pass
    elif imp == "CPython":
        gc.set_debug(0)
    