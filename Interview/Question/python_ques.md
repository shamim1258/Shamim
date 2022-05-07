# Python Preperation Questions

1. How is memory managed in Python?  
[Python](../../Technology/Python/base.md) [Python2](../../Technology/Python/base.md) 
&emsp;<details><summary>Click here</summary>
Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.
</details>

2. What is pickling and unpickling?

3. Which libraries you have used?
4. How is memory managed in Python?
5. What are decorators in Python?
6. What is lambda in Python? Why is it used?
7. What are generators in Python?
8. What is the difference between .py and .pyc files?
&emsp;
.py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program. We get bytecode after compilation of .py file (source code). .pyc files are not created for all the files that you run. It is only created for the files that you import.
Before executing a python program python interpreter checks for the compiled files. If the file is present, the virtual machine executes it. If not found, it checks for .py file. If found, compiles it to .pyc file and then python virtual machine executes it.
Having .pyc file saves you the compilation time.

9. Explain split() and join() functions in Python?
10. What does \*args and \*\*kwargs mean?
11. How does inheritance work in class?
