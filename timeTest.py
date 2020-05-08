import gc
import platform

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
        print ("minor duration:", stats.duration)

    def on_gc_collect_step(self, stats):
        pass

    def on_gc_collect(self, stats):
        print("arenas_count_before:", stats.arenas_count_before, "\narenas_count_after:", stats.arenas_count_after)
        print("arena_bytes:", stats.arenas_bytes)
        print("rawmalloc_bytes_before:", stats.rawmalloc_bytes_before, "\nrawmalloc_bytes_after:", stats.rawmalloc_bytes_after)
        self.done = True


if __name__=='__main__':
    imp = platform.python_implementation()
    gc.disable()

    if imp == "PyPy":
        hooks = MyHooks()
        gc.hooks.set(hooks)
    elif imp == "CPython":
        gc.set_debug(gc.DEBUG_STATS)

    for i in range(10000000):
        a2 = A()
        a2 = None
    gc.collect()
    
    if imp == "PyPy":
        print(gc.get_stats())
    elif imp == "CPython":
        gc.set_debug(0)
    