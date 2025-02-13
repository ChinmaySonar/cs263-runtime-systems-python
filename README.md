# Running Tests

To run the visualization tool: `<python implementation X> visualizer.py <python implementation Y> <path to test file>`

`<python implementation X>` is the Python implementation you would like to use, and should not affect the test. `<python implementation Y>` is the Python implementation you would like to test, either CPython or PyPy. Currently, it understands "python3" for CPython and "pypy3" for PyPy, but can be changed on lines 15 and 21. For CPython, the test file must run `gc.set_debug(gc.DEBUG_STATS)` to capture required output. For PyPy, the test file must set `gc.hook.on_gc_minor` to call `print ("0:", stats.duration, file=stderr)` and set `gc.hook.on_gc_collect_step` to call `print ("1:", stats.duration, file=stderr)`. threshTest.py in the CPython_Thresh_Testing folder provides an example, as well as benchmarks in Cpython-Pypy_Comparison, which should all be able to be visualized.

More specific instructions on some tests are located within their respective folders. 

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
* Compare python and pypy garbage collectors on different benchmarks. Note the qualitative difference.
* Observe effect of nursery size and L2 (last level cache) of the system for pypy garbage collector.
* Observe significant effects of changing threshold levels
### Completed
* Show that changing the threshold level of garbage collector by 1 can consistently result in large changes in time
    * Plots show that changing threshold0 in CPython_Thresh_Testing/threshTest.py from 10000001 to 10000000 increases time spent in garbage collector by almost 1.5s 
* Couldn't obtain clean trends with Nursery size and last lavel cache -- Observed that the GC does attend a local minima in terms of total time required when Nursery size is roughly 0.5 * L2. Beyond these small values, time spent and frequency of GC decreases as Nursery size is increased.
* Understood (theoretically) the incminimarc garbage collector in Pypy.

## Week 9
### Goals
* Continue comparing python and pypy garbage collectors to understand exact favorable cases for each.
* Further explore effect of Nursery size with respect to the cache size.

###
* Obtained cleaner trend for nursery size with longer custom test program with more collections
    * Data in PyPy_Nursery folder in txt files
        * First row: size of nursery for each column
        * Next 16 rows: time for 16 trials
        * Average
        * Number of minor collections
        * Number of major collection steps
    * Nursery size appears to play a large part when many collections occur, as a smaller nursery size results in fewer cache misses and less time
    * However, once nursery size increases enough for significanly less collections to occur, time decreases dramatically
    * Also tested on a couple benchmark programs, but did not see a pattern explained by cache misses, likely because program was too short with insignificant number of collections
* Compared about 15 benchmark programs on Cpython and Pypy

## Week 10
### Goals
* Work on the final presentation
* Work on the final report
