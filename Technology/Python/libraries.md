# Working with module, libraries and file import

## Modules
-  Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes, or variables defined and implemented. They can be imported and initialized once using the import statement. If partial functionality is needed, import the requisite classes or functions using from foo import bar.
-  When a module is imported python first check if it is present in `sys.path` if present or not if not than there could be some issue with installation.
-  When importing a module python first check in the cache in `sys.modules` if present than not import and use the existing one.
-  Build-in modules which i have used.(`import <module_name>`)
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
