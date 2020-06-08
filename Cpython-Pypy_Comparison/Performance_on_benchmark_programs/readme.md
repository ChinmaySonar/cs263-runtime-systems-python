We take all the benchmark programmes from -- 
https://github.com/python/pyperformance/blob/master/pyperformance/benchmarks

We append the benchmarks to our framework to produce plots for time spent in each GC round and 
overall time spent in garbage collection.

Unless mentioned otherwise, all the results are produced with default Garbage Collector Setting in both CPython and PyPy.
For some programs, the title of the image specifies the particular setting used to produce the plot.

Pyperformance suite has its own testing framework. To get around that, we remove any tester code from each of the benchmark programs. Next, we add the following piece of code to each benchmark code file (class MyHooks is for PyPy GC, and the main function is to detect compiler and run the benchmark program):


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
    
    "Add main function from the benchmark program code here"
    
    if imp == "PyPy":
         pass    
    elif imp == "CPython":
        gc.set_debug(0)

### Summary of results:

## Pypy GC outperform in the following cases:
  * bechamrk-float
  * bechmark-deltablue
  * benchmark-hexiom
  * simple_reference_cycle
## Cpython GC outperform in the following cases:
  * benchamrk-n-queens (puzzle of placing n independent queens on a chessboard)
  * benchmark-pidigits
  * benchmark-fannkuch
  * benchmark-go
  * benchmark-raytrace
 
