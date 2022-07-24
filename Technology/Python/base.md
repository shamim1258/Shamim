### Overview of Python :
- Python is an **interpreted language** means executes each statement line by line and thus type-checking is done on the fly, during execution.
- Python is a **Dynamically Typed Language**. Example of interpreted languages are Python, Javascript, R, PHP. Programs written in an interpreted language runs directly from the source code, **with no intermediary compilation step**.
- It support objects, modules, threads, exception-handling, and **automatic memory management**.
- Python is simple, easy-to-learn syntax that emphasizes readability, is capable of scripting, is completely open-source, and supports third-party packages encouraging modularity and code reuse.
- Its high-level data structures, combined with dynamic typing and dynamic binding, Rapid Application Development and deployment.

**Links :**  
- [Data Types](DataTypes/notes.md)  
- [Loop](loop.md)  
- [Exception Handling](exception_handling.md)  
- [Functions](functions.md)  
- [Classes](class.md)  
- [Libraries Packages](libraries.md)    
- [Keywords/Commands](commands.md)  
- [Working on File](working_on_files.md)  

### Memory Management

-  Python uses two strategies for memory allocation :
   1.  Reference Counting
   1.  Garbage Collection
-  Prior to Python version 2.0, the Python interpreter only used reference counting for memory management.
-  **Reference Counting :**
   -  Reference counting works by counting the number of times an object is referenced by other objects in the system.
   -  When references to an object are removed, the reference count for an object is decremented.
   -  When the reference count becomes zero, the object is deallocated.
-  **Garbage Collection :**
   -  The reference count for the list created is now two. However, since it cannot be reached from inside Python and cannot possibly be used again, it is considered garbage. In the current version of Python, this list is never freed.
^
    x = []
    x.append(l)
    x.append(2)
    del x
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
    
-  **Reference Cycles :**
   -  It is created when there is no way the reference count of the object can reach.
   -  It involving lists, tuples, instances, classes, dictionaries, and functions are common.
   -  The easiest way to create a reference cycle is to create an object which refers to itself.
^
    Because create_cycle() creates an object x which refers to itself, the object x will not automatically be freed when the function returns. This will cause the memory that x is using to be held onto until the Python garbage collector is invoked.
    def create_cycle():
      x = [ ]
      x.append(x)
    create_cycle()
    
