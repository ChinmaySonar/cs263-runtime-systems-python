import gc
import platform
from sys import stderr

class A:
    def __init__(self):
        self.A = self  

class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, file=stderr)

    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, file=stderr)

    def on_gc_collect(self, stats):
        self.done = True

imp = platform.python_implementation()
gc.collect()

if imp == "PyPy":
    hooks = MyHooks()
    gc.hooks.set(hooks)
elif imp == "CPython":
    gc.set_debug(gc.DEBUG_STATS)
    gc.set_threshold(10000000)
    # gc.set_threshold(10000001)

for i in range(1):
    l = [A() for j in range(4999997)]
    a = A()
    a = None
    l = None

