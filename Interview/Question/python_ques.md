# Python Preperation Questions

1. How is memory managed in Python?  
[Python](../../Technology/Python/base.md) [Python2](../../Technology/Python/base.md) 
&emsp;<details><summary>Click here</summary>
Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.
</details>

2. What is pickling and unpickling?
