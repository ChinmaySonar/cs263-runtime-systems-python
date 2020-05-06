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
* Tried memory profiling using [mprof](https://pypi.org/project/memory-profiler/) and created some graphs
* Failed to understand why the graphs are the way they are :'(

