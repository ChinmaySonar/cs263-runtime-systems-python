We repeat the experiment for different loads (different array sizes) with default garbage collection settings for both
Cypython, pypy, and observe:
  * Pypy's GC is about 7.5 times faster than Cpython with reference cycles
  * Pypy's GC just over 2 times faster than Cpython without reference cycles
  * Pypy's GC never stops program for large amount of time even in major collections (due to incremental major collection in pypy)
