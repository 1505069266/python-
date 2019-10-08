"""
 包
"""

import package2.a1 as c

print(c.a)

from package1.c1 import a
print(a)

from package2.a1 import *

print(a)

print(b)

print(c)