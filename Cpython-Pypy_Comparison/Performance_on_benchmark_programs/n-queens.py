import gc
import platform
from sys import stderr
import timeit

# benchmark code is taken from https://github.com/python/pyperformance/blob/master/pyperformance/benchmarks/bm_nqueens.py

import itertools


class MyHooks(object):
    done = False

    def on_gc_minor(self, stats):
        print ("0:", stats.duration, file=stderr)

    def on_gc_collect_step(self, stats):
        print ("1:", stats.duration, file=stderr)
        pass

    def on_gc_collect(self, stats):
        self.done = True


# Pure-Python implementation of itertools.permutations().
def permutations(iterable, r=None):
    """permutations(range(3), 2) --> (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)"""
    pool = tuple(iterable)
    n = len(pool)
    if r is None:
        r = n
    indices = list(range(n))
    cycles = list(range(n - r + 1, n + 1))[::-1]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


# Itertools permutations
def itertools_permutations(iterable):
    return list(itertools.permutations(iterable))

# From http://code.activestate.com/recipes/576647/
def n_queens(queen_count):
    """N-Queens solver.
    Args:
        queen_count: the number of queens to solve for. This is also the
            board size.
    Yields:
        Solutions to the problem. Each yielded value is looks like
        (3, 8, 2, 1, 4, ..., 6) where each number is the column position for the
        queen, and the index into the tuple indicates the row.
    """
    cols = range(queen_count)
    for vec in itertools_permutations(cols):
        if (queen_count == len(set(vec[i] + i for i in cols))
                        == len(set(vec[i] - i for i in cols))):
            yield vec
            #print("vec:", vec)


def bench_n_queens(queen_count):
    list(n_queens(queen_count))



# tesing function
if __name__ == "__main__":
    imp = platform.python_implementation()
    # gc.disable()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        gc.set_threshold(400,10,10)
        gc.set_debug(gc.DEBUG_STATS)

    queen_count = 8
    #a = timeit.timeit()
    bench_n_queens(queen_count)
    gc.collect()

    if imp == "PyPy":
        #print(gc.get_stats())
        pass    
    elif imp == "CPython":
        gc.set_debug(0)

    #b = timeit.timeit()
    #print("time:", b-a)
