We take all the benchmark programmes from -- 
https://github.com/python/pyperformance/blob/master/pyperformance/benchmarks

We append the benchmarks to our framework to produce plots for time spent in each GC round and 
overall time spent in garbage collection.


## Pypy GC outperform in the following cases:
  * Simple reference cycles
  * bechmark-deltablue.py
  * benchmark-float.py
  * benchmark-hexiom.py
  
## Cpython GC outperform in the following cases:
  * n-queens.py (puzzle of placing n independent queens on a chessboard)
  * benchmark-go.py
 
