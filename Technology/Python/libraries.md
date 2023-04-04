**Links :**
-  [NumPy](library_numpy.md)
-  [Pandas](library_pandas.md)
-  [Pandas Example](pandas_example.md)
-  [Matplotlib](library_matplotlib.md)

## Modules
-  Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes, or variables defined and implemented. They can be imported and initialized once using the import statement.
-  Modules can be imported partially to import a given class or function using `from foo import bar`.
-  **Separate namespaces** you can define separate namespaces to avoid collisions between identifiers in different parts of your application.
-  When a module is imported python first check if it is present in `sys.path` if present or not if not than there could be some issue with installation.
-  When importing a module python first check in the cache in `sys.modules` if present than not import and use the existing one.
-  Modules are imported when code line `import` is executed in the file and not imported in advance so if import statement in used in between code and not in starting than first the initial code is executed and when control reaches to import statement than it is executed.
-  importer are combinataion of 2 tasks
   -  finder
      -  `sys.meta_path` this will give list of finders.
   -  loader
      -  `<module_name>.__spec__` this will give loader and path details.
-  Modules are good way to implement modularity and code organization in small modules.
-  **Types of importing module :**
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

### Build-in Modules 
- The build-in modules which i have used.
   -  sys
      -  sys.prefix : Get the python installation path.
      -  sys.path : Get the list of modules installed.
      -  sys.modules : This get the cached modules imported in dictionary format of currently imported modules or sys.modules['sys'].
      -  sys.getsizeof(object) : Get the size of object in bytes
      -  sys.getrefcount(object) : To get the reference count of object and it will be incremented by 1 with this statement.
   -  functools
      -  reduce
   -  os
      -  os.getcwd() : to get present working directory path.
      -  os.listdir() : to get a list of all files and folder in given directory.
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
   -  copy
      -  copy : Shallow copy
      -  deepcopy : Deep copy
   -  traceback
      -  format_exc
   -  random
      -  randint(int1, int2) : To generate any random number between given range
      -  choice(sequnce) : To generate random number from given sequence input
   -  re
   -  abc : To implement abstract base class
      -  ABC
      -  ABCMeta
      -  abstractmethod
   -  keyword
      -  kwlist : To get all python reserved keywords
      -  iskeyword : To check if given string is python reserved keyword or not
   -  json - for working on json files
      -  load(file_object) : It takes input a json file object and convert it into respective python object list or dict.
      -  loads(content_string) : It takes input a string containing json data but not file and convert it into respective python object.
      -  dumps(python_object) : It is used to convert or serialize python object into json object.
      -  dump(python_object) : It is used to convert or serialize python object and write it into a json file.
         -  For above both methods load and load conversion or serialization from json to python done as below :
            -  JSON OBJECT	PYTHON OBJECT
               object	dict
               array	list
               string	str
               null	None
               number (int)	int
               number (real)	float
               true	True
               false	False
         -  items() : to read key, values
   -  difflib
      -  SequenceMatcher : To get similarity between two strings.
         -  `SequenceMatcher(a = str_1, b = str_2)`
         -  Return object use `ratio()` to get similarity ratio.
         -   ratio of identical characters in the two strings
      -  Differ().compare(s1,s2) : To compare two strings and get the difference between them.
      -  unified_diff : To compare two files
         -  `unified_diff(str_1, str_2)`
         -  class accepts two strings of data and then returns each word that was either inserted or deleted from the first.
      -  context_diff(s1,s2) : Only difference from unified_diff method is that it returns changes lines with `!`
   -  shutil : To perform basic operation on file like copy, move, delete etc.
      -  shutil.copy(source, destination) : Copy file from source file to destination file or path
      -  shutil.copy2(source, destination) : Same as above copy method only difference is this also copy the file metadata.

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

-  [Pandas](library_pandas.md)
-  [NumPy](library_numpy.md)
-  [Matplotlib](library_matplotlib.md)
-  SciPy
   -  Algorithm to use with NumPy
-  **openpyxl**
   -  To work on excel file.
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
-  Threading : Used for multi-threading
   -  thread
-  json2html
   -  convert(json = jsonfileobject) : To convert json file into html table

## Libraries
-  Libraries generally referred as collection of packages.
-  Libraries can be interchangeble be used for package also as package is collection of modules and sub-packages.

## Django Libraries
-  Django packages and libraries i have used.
   -  `from django.shortcuts import render`
   -  `from django.http import HttpResponse`
   -  `django.contrib.admin.models`
      -  `LogEntry`
   -  `django-cors-headers`
