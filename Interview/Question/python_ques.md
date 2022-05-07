# Python Preperation Questions

1. How is memory managed in Python?  
[Python](../../Technology/Python/base.md) [Python2](../../Technology/Python/base.md) 
&emsp;<details>
Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.

2. What is pickling and unpickling?

3. Which libraries you have used?
4. How is memory managed in Python?
5. What are decorators in Python?
6. What is lambda in Python? Why is it used?
7. What are generators in Python?
8. What is the difference between .py and .pyc files?
&emsp;<details>
.py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program. We get bytecode after compilation of .py file (source code). .pyc files are not created for all the files that you run. It is only created for the files that you import.
Before executing a python program python interpreter checks for the compiled files. If the file is present, the virtual machine executes it. If not found, it checks for .py file. If found, compiles it to .pyc file and then python virtual machine executes it.
Having .pyc file saves you the compilation time.

9. Explain split() and join() functions in Python?
10. What does \*args and \*\*kwargs mean?
11. How does inheritance work in class?
12. Are access specifiers used in python?
&emsp;<details>Python does not make use of access specifiers specifically like private, public, protected, etc. However, it does not derive this from any variables. It has the concept of imitating the behaviour of variables by making use of a single (protected) or double underscore (private) as prefixed to the variable names. By default, the variables without prefixed underscores are public.

13. Why is finalize used?
&emsp;<details>Finalize method is used for freeing up the unmanaged resources and clean up before the garbage collection method is invoked. This helps in performing memory management tasks.
  
14. What is init method in python?
&emsp;<details>The method is run as soon as an object is instantiated. It is useful for initializing any attributes or default behaviour of the object at the time of instantiation.
  
15. How will you check if a class is a child of another class?
&emsp;<details>This is done by using a method called issubclass() provided by python. The method tells us if any class is a child of another class by returning true or false accordingly.
  
