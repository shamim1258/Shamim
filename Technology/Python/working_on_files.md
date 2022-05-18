# Working on Files

### open function
You don't really have to close it - Python will do it automatically either during garbage collection or at program exit. But as @delnan noted, it's better practice to explicitly close it for various reasons.
```with open('pagehead.section.htm', 'r') as f:
    output = f.read()```
