### Overview of Python :
-  Python is an **interpreted**, object-oriented, high-level programming language with **dynamic semantics**. Its high-level built in data structures, combined with **dynamic typing** and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
- **Interpreted Langugae** - Python have compiler which convert python source code into byte code unlike traditional compiler which convert source code into machine code and this byte code is saved in .pyc file python virtual machine don't run the source code but run this byte code here the python virtual machine act as interpreter which convert the byte code line by line into machine code which is executed by operating system. Also unlike traditional interpreter language which convert one line of byte code than wait for os to ask for next line but python interpreter keeps on converting byte code in a file and don't wait for os to complete execution on previous line.
-  Python uses **dynamic semantics**, meaning that its variables are dynamic objects which means variable type is decided in run time dynamically.
- Python is a **Dynamically Typed Language** which means types are assigned based on the value it is referring to, as in python variable is not associated with the data-type but it have the memory reference and that memory holds the data and its type, so when we reassign the variable its memory reference and type also changes. `variable_name = "value"`.
- **.pyc file -** A \*.pyc file is created by the Python interpreter when a \*.py file is imported into any other python file. The \*.pyc file contains the “compiled bytecode” of the imported module or program so that the “translation” from source code to bytecode can be skipped on subsequent imports of the \*.py file. Having a \*.pyc file saves the compilation time of converting the python source code to byte code, every time the file is imported. Thus speeding startup a little. But it’s still interpreted. Once the \*.pyc file is generated, there is no need for the \*.py file, unless the \*.py file is modified. In Python 3.2, the compiled files (.pyc) are placed in a __pycache__ subdirectory
- Also .pyc file is not created for every py file unless it is not importing any module or other .py file except for build in modules like os and .pyc file is saved in sub-directory named __pycache__ in the same path where py file present.
- It support objects, modules, threads, exception-handling, and **automatic memory management**.
- Python is simple, easy-to-learn syntax that emphasizes readability, is capable of scripting, is completely open-source, and supports third-party packages encouraging modularity and code reuse.
- Its high-level data structures, combined with dynamic typing and dynamic binding, Rapid Application Development and deployment.
- .pyc files are created by the Python interpreter when a .py file is imported. They contain the "compiled bytecode" of the imported module/program so that the "translation" from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. But it's still interpreted. Once the *.pyc file is generated, there is no need of /*.py file, unless you edit it.
-  **PEP-8** is a document that provides guidelines and best practices on how to write Python code.
   -  PEP stands for Python Enhancement Proposal.
   -  The primary focus of PEP 8 is to improve the readability and consistency of Python code.
   -  Follow the naming conventions.
   -  Provide proper comments.

**Links :**  
- [Data Types](DataTypes/notes.md)  
- [Loop](loop.md)  
- [Exception Handling](exception_handling.md)  
- [Functions](functions.md)  
- [Classes](class.md)  
- [Libraries Packages](libraries.md)    
- [Keywords/Commands](commands.md)  
- [Working on File](working_on_files.md)  
- [Advance Python Concept](advance_python.md)  

### Memory Management

-  Python objects and variables stored in the memory address and variable holds the address of memory and not actual value.
-  To get the memory address of any object `id(variable_name)`
-  Python uses two strategies for memory allocation :
   1.  Reference Counting
   1.  Garbage Collection
-  Prior to Python version 2.0, the Python interpreter only used reference counting for memory management.
-  **Reference Counting :**
   -  Reference counting is tracking number of times a memory address is being used by different objects.
   -  When references to an object are removed, the reference count for an object is decremented.
   -  When the reference count is zero, the object is deleted from the system by the **garbage collection**.
   -  Getting the reference count :
      -  To get the reference count of any memory address - `sys.getrefcount(variable_name)` but downside to this is it also increase the reference count by 1.
      -  By using `ctypes.c_long.from_address(address).value` here we are not passing variable name but its memory address and it will give the exact count without increasing it.
      -  If count like `ctypes.c_long.from_address(id(variable_name)).value` than it will not increase the count by 1 even if we are taking parameter as variable_name because when from_address will run by that time id(variable_name) is already executed and release its memory also this will work same way as `ctypes.c_long.from_address(address).value`
-  **Garbage Collection :**
   -  Garbage collection is implemented in Python in two ways: reference counting and generational. When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately. If you have a cycle, reference count doesn’t reach zero, you wait for the generational garbage collection algorithm to run and clean the object.
   -  Garbage Collection is memory management utility which runs automatically to deallocated the memory space of non-usable objects and also take care of cyclic dependency.
   -  This runs automatically and can be also be triggered manually and handles the cyclic dependency.
   -  In below example reference count for the list created is two. However, since it cannot be reached from inside Python and cannot possibly be used again, it is considered garbage. In the current version of Python, this list is never freed.
^
    x = []
    x.append(l)
    x.append(2)
    del x
^
   -  It can be controlled programmitacally using gc module to do your own clean up.
   -  By default it is turned ON.
   -  We can turn it OFF if you are sure that your code does not create circular reference.
   -  Before python-3.4 garbage collection does not handle the circular reference so it is recommended to use Python-3.5 and above.
   -  **Automatic Garbage Collection of Cycles :**
      -  Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations is greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) by importing the gc module and asking for garbage collection thresholds.\
^
    import gc
    print("Garbage collection thresholds:",gc.get_threshold())
    **Output:**
    Garbage collection thresholds: (700, 10, 10)
    Here, the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run.
    
   -  **Manual Garbage Collection :**
      -  Invoking the garbage collector manually during the execution of a program can be a good idea on how to handle memory being consumed by reference cycles. 
The garbage collection can be invoked manually in the following way :
^
    import gc
    collected = gc.collect()
    print("Garbage collector: collected","%d objects." % collected)
    
-  **Reference Cycles / Circular Reference :**
   -  Cyclic Reference is created when A object calls B object and B also calls A.
   -  It is created when there is no way the reference count of the object can reach zero.
   -  It involving lists, tuples, instances, classes, dictionaries, and functions are common.
   -  The easiest way to create a reference cycle is to create an object which refers to itself.
   -  This cannot be handled by reference counting and but can be handled by **Garbage Collector**.
^
    def functionA():
        functionB()
    def functionB():
        functionA()
^
    
-  **Python Optimizations - Peephole :** pre-calculate or cache the expression for optimization purpose.
   -  **Contact expression**
      -  Numeric calculation `25 * 60` python will pre-calculate.
      -  Short sequence with length < 20 `lst = [1,2,3]`
   -  Membership test : Mutable object converted to immutable object
      -  list to tuple
      -  set to frozenset
      -  Example below list_A with list elements immutable will get converted to tuple but list_B having variable elements this will not get converted.
^
    list_A = [1, 2, 3]
    list_B = [variable_a, 2, 3]
^
   -  set element comparision is much faster than list and tuple.

-  **Context Manager :**
   -  To overcome the problem of memory leak(external resource like files, locks, network connection when opened will kept open for forever if not closed) python have Context Manager.
   -  Python have 2 approches to deal with memeory management.
      -  `try..finally`
         -  putting file close statement in finally will gurantee that file will get properly closed.
      -  `with`
         -  It created run time context where group of statements executed within control of context manager.
         -  The context manager object results from evaluating the expression after with. In other words, expression must return an object that implements the context management protocol. This protocol consists of two special methods.
            -  __enter__() is called by the with statement to enter the runtime context.
            -  __exit__() is called when the execution leaves the with code block.

-  **OOPs Concept in Python :**
   -  Class
      -  Class is blueprint or prototype from which objects are created.
   -  Objects
      -  The object is an entity that has a state and behavior associated with it. 
   -  Polymorphism
      -  This is a concept which is one function or method can take more than one form mean function can take behaives different based on different arguments passed.
      -  Example `print(1 + 2)` and `print('1' + '2')`
   -  Encapsulation
   -  Inheritance
   -  Data Abstraction
