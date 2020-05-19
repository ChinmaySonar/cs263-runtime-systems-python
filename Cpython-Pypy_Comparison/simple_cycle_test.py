import gc
import platform
from sys import stderr


class A:
    def setCycle(self):
        self.B = B(self)    

class B:
    def __init__(self, A):
        self.A = A


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
    # gc.disable()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        gc.set_debug(gc.DEBUG_STATS)
    array1 = [0]*640000

    for i in range(640000):
        a2 = A()
        a2.setCycle()
        array1[i] = a2
   
    
    if imp == "PyPy":
         pass    
    elif imp == "CPython":
        gc.set_debug(0)
