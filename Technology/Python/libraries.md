# Import

## Modules
-  Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes, or variables defined and implemented. They can be imported and initialized once using the import statement. If partial functionality is needed, import the requisite classes or functions using from foo import bar.
-  When a module is imported python first check if it is present in `sys.path` if present or not if not than there could be some issue with installation.
-  When importing a module python first check in the cache in `sys.modules` if present than not import and use the existing one.
-  Modules are imported when code line `import` is executed in the file and not imported in advance so if import statement in used in between code and not in starting than first the initial code is executed and when control reaches to import statement than it is executed.
-  importer are combinataion of 2 tasks
   -  finder
      -  `sys.meta_path` this will give list of finders.
   -  loader
      -  `<module_name>.__spec__` this will give loader and path details.

-  Types of importing module
   -  `import math`
      -  First check if module 'math' is present in 'sys.modules' `is math in sys.module`
         -  If present in sys.module than it will refer to this and not import again.
         -  If not present in sys.module
            -  It will import the module math and create the reference in sys.module with keyword as math.
            -  It will add math symbol in the module's global namespace referencing same object as above created in sys.module `module1.globals()`
   -  `import math as r_math`
      -  First check if module 'math' is present in 'sys.modules' `is math in sys.module`
         -  If present in sys.module than it will refer to this and not import again.
            -  It will add r_math symbol in the module's global namespace referencing same object as found above in sys.module `module1.globals()`  
         -  If not present in sys.module
            -  It will import the module math and create the reference in sys.module with keyword as math.
            -  It will add r_math symbol in the module's global namespace referencing same object as above created in sys.module `module1.globals()` even if math already present in the namespace and both will refer to same object in sys.module.
   -  `from math import sqrt`
      -  First check if module 'math' is present in 'sys.modules' `is math in sys.module`
         -  If present in sys.module than it will refer to this and not import math again.
            -  It will add sqrt symbol in the module's global namespace referencing same object math.sqrt and not add math in global namespace.   
         -  If not present in sys.module
            -  It will import the module math and create the reference in sys.module with keyword as math.
            -  It will add sqrt symbol in the module's global namespace referencing same object math.sqrt and not add math in global namespace.  
   -  `from math import sqrt as r_sqrt`
      -  First check if module 'math' is present in 'sys.modules' `is math in sys.module`
         -  If present in sys.module than it will refer to this and not import again.
            -  It will add r_sqrt symbol in the module's global namespace referencing same object math.sqrt and not add math in global namespace.   
         -  If not present in sys.module
            -  It will import the module math and create the reference in sys.module with keyword as math.
            -  It will add r_sqrt symbol in the module's global namespace referencing same object math.sqrt and not add math in global namespace.  
   -  `from math import *`
      -  First check if module 'math' is present in 'sys.modules' `is math in sys.module`
         -  If present in sys.module than it will refer to this and not import again.
            -  It will add all the function of math symbol's in the module's global namespace referencing object liek math.sqrt, math.pi, etc and not add math in global namespace.   
         -  If not present in sys.module
            -  It will import the module math and create the reference in sys.module with keyword as math.
            -  It will add all the function of math symbol's in the module's global namespace referencing object liek math.sqrt, math.pi, etc and not add math in global namespace.  
      -   Issue occur when we use 2 moduel having same function name like moduel math and cmath both having function name sqrt.
          -   In this case the in the globals() namespace only 1 keyword is created for sqrt and it will refer to the last module imported as it will referesh the namespace from sys.module, like in below example math will overwrite in namespace.
^
    from import cmath *
    from import math *
^
-  Performance wise not much difference in using `import math` and `from math import sqrt` as in both cases math is going to be imported just in case 2 sqrt namespace will be created in namespace globals().
-  Module have properties : __file__, __package__ but not have property __path__ but package have this property.

-  Build-in modules which i have used.(`import <module_name>`).
   -  sys
      -  sys.prefix : Get the python installation path.
      -  sys.path : Get the list of modules installed.
      -  sys.modules : This get the cached modules imported in dictionary format of currently imported modules or sys.modules['sys'].
      -  sys.getsizeof(object) : Get the size of object in bytes
   -  functools
      -  reduce
   -  inspect
      -  isfunction(obj)
      -  ismethod(obj)
      -  inspect.getsource(object)
      -  inspect.getmodule(object)
      -  inspect.getcomments(object)
   -  time
      -  perf_counter()
   -  timeit
      -  timeit
   -  dis
      -  dis()
      -  compile()
      -  

## Packages
-  Package is directory with __init__.py file and other python files where name of directory is package name.
-  All packages are module but all modules are not necessary package.
-  Package can contain modules and sub-packages.
-  The code of package is in __init__.py and the code is loaded, executed and cached in sys.modules with a key of package folder name.
-  The package name is added to the namespace referencing the same object.
-  Package have property '__path__' which is the directory path(absolute).
-  Property '__file__' it has path(absolute) to '__init__.py'.
-  It uses dot notation to refer a package or module in a package pack1.pack2.module3
^
    app\
        pack1\
            __init__.py
            module1.py
            module2.py
        pack2\
            __init__.py
            module3.py
            module4.py
^
-  In above example if we use `import pack1` than pack1 is added to sys.module, module1 is added to sys.module and module2 is added to sys.module.
-  If we use `import pack1.pack2.module3` than pack1 is added to sys.module, module1 is added to sys.module and module2 is added to sys.module, pack2 is added to sys.module, module3 is added to sys.module.

-  Pandas
   -  Used for data analysis.
   -  dataframe
-  NumPy
   -  Multidimentional Array
-  SciPy
   -  Algorithm to use with NumPy
-  PyMySQL
   -  MySQL connection
-  IPython
   -  powerfull shell
-  SymPy
   -  Symbolic math
-  SQLAlchemy
   -  Python SQL Toolkit
-  Seaborn
   -  Data visualization tool
-  HDF5
   -  Used to store and manipulate data
