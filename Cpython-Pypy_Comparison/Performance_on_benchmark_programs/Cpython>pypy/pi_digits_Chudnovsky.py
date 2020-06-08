# generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
# https://github.com/microice333/Python-projects/blob/master/n_digit_pi.py

import gc
import platform
from sys import stderr
import timeit
import decimal

class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, file=stderr)

    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, file=stderr)
        pass

    def on_gc_collect(self, stats):
        self.done = True



def compute_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi


while True:
    n = 2000
    if n >= 0 and n <= 5000:
        break



if __name__ == "__main__":
    
    imp = platform.python_implementation()
    gc.disable()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        #gc.set_threshold(5,10,10)
        gc.set_debug(gc.DEBUG_STATS)
    a = timeit.timeit()
    compute_pi(n)
    b = timeit.timeit()
    print("time: ", b-a)
    

    if imp == "PyPy":
        #print(gc.get_stats())
        pass    
    elif imp == "CPython":
        gc.set_debug(0)
