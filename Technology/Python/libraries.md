# Working with module, libraries and file import

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
         -  If present in sys.module than it will refer to this and not import again.
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

-  Build-in modules which i have used.(`import <module_name>`).
   -  sys
      -  sys.prefix : Get the python installation path.
      -  sys.path : Get the list of modules installed.
      -  sys.modules : This get the cached modules imported in dictionary format of currently imported modules or sys.modules['sys'].
   -  functools
      -  reduce
   -  inspect
      -  isfunction(obj)
      -  ismethod(obj)
      -  inspect.getsource(object)
      -  inspect.getmodule(object)
      -  inspect.getcomments(object)

## Packages

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
