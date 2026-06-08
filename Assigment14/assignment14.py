'''Assignment 14: Create a scenario where objects are "dead" but still have a reference count higher than zero, then force the Garbage Collector to clean them up. Do in python only. 

Implementation Steps:

Create a Node class with a name and a link attribute.

Create a Cycle: Instantiate Node A and Node B.

Set A.link = B and B.link = A.

Check References: Use sys.getrefcount() to show that both objects have multiple references.

The "Deletion": Use del A and del B.

The Investigation: Use the gc module to show that these objects still exist in memory because of the cycle, even though you can no longer access them from your code.

The Cleanup: Call gc.collect() and print the number of "unreachable" objects collected.'''


import sys
import gc
class Node:
    def __init__(self,name):
        self.name=name
        self.link=None


A = Node("Kaushal")
B = Node("Alok")
#both object are pointing to each other this is called circular reference/reference cylcle
A.link=B
B.link=A
d=A

#python create extra referrnce while calling the function
#temporary reference is created by getrefcount()
sysa=sys.getrefcount(A)
sysb=sys.getrefcount(B)
print(sysa)
print(sysb)


del A


del B

del d


print(gc.collect())
print(gc.garbage)
