import gc
import platform
from sys import stderr


"""
Artificial, floating point-heavy benchmark originally used by Factor.
"""
#import pyperf

from math import sin, cos, sqrt


POINTS = 100000


class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, file=stderr)

    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, file=stderr)
        pass

    def on_gc_collect(self, stats):
        self.done = True

class Point(object):
    __slots__ = ('x', 'y', 'z')

    def __init__(self, i):
        self.x = x = sin(i)
        self.y = cos(i) * 3
        self.z = (x * x) / 2

    def __repr__(self):
        return "<Point: x=%s, y=%s, z=%s>" % (self.x, self.y, self.z)

    def normalize(self):
        x = self.x
        y = self.y
        z = self.z
        norm = sqrt(x * x + y * y + z * z)
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def maximize(self, other):
        self.x = self.x if self.x > other.x else other.x
        self.y = self.y if self.y > other.y else other.y
        self.z = self.z if self.z > other.z else other.z
        return self


def maximize(points):
    next = points[0]
    for p in points[1:]:
        next = next.maximize(p)
    return next


def benchmark(n):
    points = [None] * n
    for i in range(n):
        points[i] = Point(i)
    for p in points:
        p.normalize()
    return maximize(points)

if __name__=='__main__':
    imp = platform.python_implementation()
    # gc.disable()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        #gc.set_threshold(50,10,100)
        gc.set_debug(gc.DEBUG_STATS)
    benchmark(1000000)
    
    

    if imp == "PyPy":
        #print(gc.get_stats())
        pass    
    elif imp == "CPython":
        gc.set_debug(0)

