import gc

class A:
    def setCycle(self):
        self.B = B(self)    

class B:
    def __init__(self, A):
        self.A = A

gc.disable()
gc.set_debug(gc.DEBUG_LEAK)

# With no reference cycles, gc should not have to collect any garbage
print("No reference cycle:")
a1 = A()

print("Number of unreachable objects found by garbage collector before removing reference:", gc.collect())
a1 = None
print("Number of unreachable objects found by garbage collector after removing reference:", gc.collect())
print("Saved garbage:")
print(gc.garbage)

# With a reference cycle, gc collects garbage unreachalbe by simply reference counting
print()
print("Reference cycle:")
a2 = A()
a2.setCycle()

print("Number of unreachable objects found by garbage collector before removing reference:", gc.collect())
a2 = None
print("Number of unreachable objects found by garbage collector after removing reference:", gc.collect())
print("Saved garbage:")
print(gc.garbage)

gc.set_debug(0)