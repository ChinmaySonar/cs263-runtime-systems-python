#!/bin/sh
for i in 1 2
do
  for i in 1 2 3 4 5 6 7 8
  do
    PYPY_GC_NURSERY=1024m python3 ../visualizer.py pypy3 nurseryTest.py
  done
done