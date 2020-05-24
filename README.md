# Project Journal

## Week 4
### Goals
* Learn the details of CPython garbage collection
* Learn how to use the **gc** module
* Learn how to use some Python profilers
### Completed
* Watched [video about CPython garbage collector](https://www.youtube.com/watch?v=CLW5Lyc1FN8) and [video comparing PyPy garbage collector](https://www.youtube.com/watch?v=zQVytExlnEk) to understand what happens behind the scenes
* Experimented with **gc** module
* Looked at possible benchmark programs to base our tests on
* Read other articles about Python garbage collection (in survey.txt)

## Week 5
### Goals
* Continue experimenting with **gc** module
* Decide if or how we should analyze CPython garbage collector on its own
* Start considering how to compare with PyPy garbage collector
### Completed
* Experimented with gc performance with and without reference cycles (Python handles the two cases using different Garbage Collectors)
* Explored functionalities in **gc** module

## Week 6
### Goals
* Download and understand more about PyPy and its **gc**
* Start profiling and comparing CPython and PyPy
* Try [benchmarking programs](https://github.com/CAS-Atlantic/python-gc-benchmark/tree/master/)
### Completed
* Downloaded PyPy
* Research some other papers that focus on PyPy garbage collector
* Could not correcty set up mentioned benchmark thing
* Tried memory profiling using [mprof](https://pypi.org/project/memory-profiler/) and created some graphs
    * Failed to understand why the graphs are the way they are :'(
    * Not that usefull because tracks memory returned to OS, but memory not always returned
* Tried more memory profiling using [guppy](https://pypi.org/project/guppy3/)
    * Doesn't seem too useful as does not track garbage
* Tried tracking time spent in garbage collector for CPython and PyPy
    * Only able to track time of one single collection using **gc** 
    * Don't completely understand the memory info of PyPy [hook stats](https://doc.pypy.org/en/latest/gc_info.html#gc-hooks)
    * PyPy does run faster on timeTest.py both as a whole and claimed time in garbage collector

## Week 7
### Goals
* Look for papers testing PyPy's garbage collector
* Create tool to better log and visualize garbage collection times
* Create programs to test limits of garbage collection
### Completed
* visualizer.py plots and records time in plot.png and output.txt
    * Usage: `python3 visualizer.py <python implementation> <test file>`
    * Collects \<test file\> stderr output and matches portions that show generation and time of each collection
    * For CPython, \<test file\> must run `gc.set_debug(gc.DEBUG_STATS)` to capture required output
    * For PyPy, \<test file\> must set `gc.hook.on_gc_minor` to call `print ("0:", stats.duration, file=stderr)` and set `gc.hook.on_gc_collect_step` to call `print ("1:", stats.duration, file=stderr)`
    * Can test with `python3 visualizer.py python3/pypy3 timeTest.py`
    * Make plots look prettier
* Papers comparing pypy vs Cpython garbage collectors:
    * Quantitative overhead analysis for python -- https://ieeexplore.ieee.org/document/8573512
    * python garbage collection implementations CPython, pypy, GaS -- https://pdfs.semanticscholar.org/ed0a/1cdf9bb639084e80794b9e5a95fa616bb848.pdf

## Week 8
### Goals
* Compare python and pypy collectors on different benchmarks. Note the qualitative difference.
* Observe effect of nursery size and L2 (last level cache) of the system for pypy garbage collector.
* Observe significant effects of changing threshold levels
### Completed
* Show that changing the threshold level of garbage collector by 1 can consistently result in large changes in time
    * Plots show that changing threshold0 in CPython_Thresh_Testing/threshTest.py from 10000001 to 10000000 increases time spent in garbage collector by almost 1.5s 
* Couldn't obtain clean trends with Nursery size and last lavel cache -- Observed that the GC does attend a local minima in terms of total time required when Nursery size is roughly 0.5 * L2. Beyond these small values, time spent and frequency of GC decreases as Nursery size is increased.
* Understood (theoretically) the incminimarc garbage collector in Pypy.
