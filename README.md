# Python module: NewBase60 by Tantek Çelik

This is a pure Python 2 implementation of NewBase60 number system.

Please refer to [Tantek's website](http://tantek.pbworks.com/w/page/19402946/NewBase60) to understand what NewBase60 is.

## Usage

```
from nb60 import nb60

n = 500
s = nb60.ntonb60(n)

m = nb60.nb60ton(s)

print "{0} = {1}, NewBase60({0}) = {2}".format(n, m, s) 
```

## Installation
This is a standard Python module, so a simple `python setup.py install` should do the trick.