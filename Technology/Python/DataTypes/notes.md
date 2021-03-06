# Data Types :

-  Data type tells about type of value it can hold and also what [operations](#operations) can be performed on that value.
-  Python sets the variable type based on the value that is assigned to it.
-  Use ```type()``` function to get the data-type of any variable.
-  Convert data-type - ```str(123)```.
-  `None` is real object managed by python memory manager and all objects assigned with None will have same memroy reference.
-  Check the [Mutability](#mutability) section carefully than go through below point of deep understanding of variable assignment.
-  A variable actually hold the memory reference and not the actual value whether mutable or immutable. `a = 10`
-  Mutable object hold the memory address and the state or value of data this address hold can be changed keeping the same memory address of variable.
-  Immutable object hold the memory address and state or value of data this address hold cannot be changed so when assigning new value it changes the memory reference to some other address where new value present and the previous memory address still having the previous value.
-  **Immutable** object assignment.
   -  In below example a hold memory reference for 10 and when we do `b = a` this does not copy the value 10 to b but b will also have same memory reference as a, As a = 10 and it is interger type which is immutable.
^
    a = 10
    b = a
^
   -  When more than one variable having same the variable not actually have same value but all such variable are having memory reference to same address and this task of assigning memory reference is done by python memory manager.
^
    a = 10
    b = 10
    stra = "hello"
    strb = "hello"an
^
-  **Mutable** object assignment.
   -  (ReConfirm not sure about this point)Even if two variable have same value the memory address is different because if one variable value is changed it will update the value in the meory address and not change the memory address and keeping such variable memory different will avoid over writing of other variable when one is updated.
^
    list_A = [1, 2, 3]
    list_B = [1, 2, 3]
^
-  **Interning** is resuing objects on-demand \
   - At startup python(CPython) pre-loads(cache) a global list of integers in range(-5:256) so anytime integer is referenced in this range python will reuse the address reference of cached version of object.
   - Python also cache some strings but not all.
     - As python code compiled identifier are interned which includes : variable name, function name, class name and identifier which are like start with _ or letter and only contains letter and number.
     - Some string literal also interned which looks like identifier example 'hello_world'
-  
-  **Python Data Types :**
   - [Text](#text)    : str
   - [Numeric](#numeric)    : int, float, complex
   - [Sequence](#sequence)    : list, tuple, range
   - [Mapping](#mapping)    : dict
   - [Set](#set)    : set, frozenset
   - [Boolean](#boolean)    : bool
   - [Binary](#binary)    : bytes, bytearray, memoryview

[Scope](#variable-scopes) wise variables types
- Global
- Protected
- Private

Check the [operations](#operations) on data-types.
Check the [Mutability](#mutability) on data-types.

**Variable Equality :**
-  Can you `is` operator to compare the memory address of two variable this is similar to `==` operator.
-  Can you `is not` operator which is similar to `!=` operator.
-  `is` compare the memory address only so not always works well.
-  `==` compare the object memory address values this is more trust worthy.

## Text
1.  **str**
    - Strings are sequences of character data.
    - Interpreting a character or sequence of characters within a string differently use ```\``` as **Escape Sequences**.
    - **Raw String** - literal is preceded by r or R, which specifies that escape sequences in the associated string are not translated. The backslash character is left in the string:
    `>>> print(r'foo\nbar')`  
    `foo\nbar`
    - **Triple Quoted Strings** - Escape sequences still work in triple-quoted strings, but single quotes, double quotes, and newlines can be included without escaping them.
    -  All string methods returns new values. They do not change the original string.
    -  Various [methos](https://www.w3schools.com/python/python_ref_string.asp) on string.
    -  string comparsion with operation `==` is done character by character and `is` operator compares the memory reference.
    -  We can manually intern the string by using `sys.intern('new string here')` method and now for this string we can use the `is` operator to compare which will make the comparision faster.

## Numeric
-  Various methods on numberic data types - min(n1,n2,n3..), max(n1,n2,n3..), abs(x), pow(x,y), round(x), sqrt(x).
-  Variable hold the memory reference where the actual value present.
1.  **int**
    -  In Python 3, there is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount of memory your system has.

2.  **float**
    - float values are specified with a decimal point.


## Sequence
1.  **List**
- List is like array but item can of different data-types.
- Uses - []
- List methods are - append(), clear(), copy(), count(), extend(), pop(), remove(), reverse(), index(), insert(), sort()

2.  **Tuple**
- Tuple are immutable i.e. cannot be modified after it is created.
- Uses - ()
- Tuple methods only 2 - count(), index()
- `tpl = (1)` this is not tuple but int you can check by `type(tpl)` to make it tuple `tpl = (1,)`.
    
2.  **Range**
- Create a sequence of number starting from 0 to n-1.
- Syntax `range(start, stop, step)`

## Mapping
- Mapping data types are key, value pair types - dict.
^
1.  **dict**
- Methods - clear(), copy(), formkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()

## Set
1.  **Set**
- Methods - add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), isdisjoint(), issubset(), isuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update().

2.  **FronzenSet**
- It return set of unchangeable objects.
- Methods - 

## Boolean
1.  **bool**
- Boolean type have 2 values -```True or False```.
- Return boolean value of given expression - `bool(1)`
- If no parameter is given default return value is `False`.
- `bool` is subclass of `int` and we can check this also `issubclass(bool, int)`

# Variable scopes
-  **Namespace** is collection of object(variable) and object information(value) for the given scope(built-in, global, local).  
-  An object can be variable or method.
-  A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends, the lifetime of that namespace comes to an end. Hence, it is not possible to access the inner namespace???s objects from an outer namespace.
-  Python itself maintain Namespace in the form of python dictionary.  
-  Types of Namespcae
   -  Built-In
      -  It contains the names of all of Python???s built-in objects. These are available at all times when Python is running.
      -  To get the list of namespace in built-in use command `dir(__builtins__)`
   -  Global
      -  It contains any names defined at the level of the main program.
      -  Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates.
      -  There may not be the only one global namespace that exists. The interpreter also creates a global namespace for any module that your program loads with the import statement.
   -  Enclosing
      -  When the main program calls function f() python creates a namespace for f() is Enclosing namespace.
   -  Local
      -  When the main function f() in enclosing namespace calls function g() than python create a namespace is Local namespace.
-  **Scope** refers to the coding region from which a particular Python object is accessible. Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
-  When we define a variable at that point scope is not created when that variable is called at that point scope is created for that variable.
-  New scope is created every time a function is called and new scope is created every time same function is called.
-  **LEGB Rule / Order of namespace :**
   -  LEGB - Local, Enclosing, Global, Built-in.
   -  Suppose we have a variable with same name in all the namespaces than python will search the variable in exists in the order 
      1.  Local
      2.  Enclosing
      3.  Global
      4.  Built-In
-  If an object is present in built-in and if we declare same in local that local will overwrite that object in the local scope.
^
    print = lambda x : 'hello ' + x, x
    print('world') # this will overwrite the print function in local scope but outside this scope the print function will as default functionality
^
-  We can use `nonlocal` similar like `global` to refer to nonlocal variable which will search variable from inner most in the only local scope and will not search in global scope.
-  **Closure :**
   -  When inner function refers to its outer function variable in this case the inner function and its outer variable together called closure. In below example inner function with outer function var variable is closure
^
    def outer():
        var = 10       #Closure
        def inner():   #Closure
            print(var) #Closure
        return inner
^
   -  Problem here is var variable exists in scope of outer and inner function so when inner function called the scope of outer function already ended how to get the value of var variable to solve this python as an exception identify this as closure than outer function var hold the memory address of a cell(this is memory address which hold the memory address of where actual value of var kept) and inner function also refers to this cell, so both refers to the cell and cell refers to address which holds the value of object.
     
**Global :**
-  Global scope is the module scope.
-  Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.
-  Python don't have concept of Truely Gobal scope across all modules and only exception to this is some globally available built-in objects which are `True, False, None, print, dict`

**Protected :**
- Protected attributes are attributes defined with an underscore prefixed to their identifier eg. \_sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.

**Private :**
- Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

## Mutability
-  Data-types holds the memory reference and that memory hold the data-type and value.
-  Mutability tells if the state of the data-type can be changed or not.
-  Immutables
   -  Numbers(int, float, Boolean, etc.)
   -  Strings
   -  Tuples
   -  Frozen Sets
   -  User-defined classes
-  Mutables
   -  Lists
   -  Sets
   -  Dictionaries
   -  User-defined classes
-  Tuple is immutable but it can have mutable elements like list where we can say tuple is immutable but it's element are mutable.
-  When tuple passed as function parameter the original tuple will remain unchanged.
-  When list passed as function parameter the original list will get changed in function update the list.

# Other objects Types

**Iterator :**
-  Iterator is an object that contains countable number of values.
-  Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.
-  Iterators allow us to both work with and create lazy iterables that don???t do any work until we ask them for their next item.
-  Because of their laziness, the iterators can help us to deal with infinitely long iterables. In some cases, we can???t even store all the information in the memory, so we can use an iterator which can give us the next item every time we ask it. Iterators can save us a lot of memory and CPU time.
-  Creating iterators :
   -  Applying the **`iter()`** built-in function to an iterable.
   -  Create **custom iterator** by defining a class that has `__init__, __next__, and __iter__` methods.
   -  **Generators Function** it looks like normal function except it uses `yield` instead of `return` expression.
   -  **Generator Expression** it return an iterator, it looks like normal expression followed by a `for` expression defining loop variable,range and an optional multiple `if` expression(s).  
^
    numbers = [1, 2, 3, 4, 5]  
    squares = (number**2 for number in numbers if number % 2 == 0) if number % 4 == 0  
    
-  The `__iter__()` method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
-  **next()**
   -  This method returns the next item from the container. If there are no further items, raise the `StopIteration` exception.
   -  We can directly use `next()` function or `__next__()` method to traverse the elements.
   -  When this is used for first time it will get the first element.
   -  Iterators don???t have to be finite. It???s perfectly reasonable to write an iterator that produces an infinite stream of data.

**yield :**
- It temperory suspend the processing remembering the location execution state (including local variables and pending try-statements).
- When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

**self :**
- Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.

**__init__ :**
- __init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a __init__ method associated with them.

**docstring :**
- Represented with triple quotation marks used for documents. __doc__ attribute.
Syntax ``` ''' This is doc string. '''  ```

# Operations

**Slicing :**
- Slicing is taking some part of. Syntax ``` [start : stop : step] ```. Default values of start is 0, stop is number of items and step is 1.  
Slicing can be done on strings, arrays, lists, and tuples.

**Copying object by assignment :**
- When an object is assigned to new object it does not create copy value to new object but new object holds the reference to old object.
- If any changes made to the value using new object or old object both objects value will show the new updated value.
^
    list_A = [1,2,3,4,5]
    list_B = list_A
-  Copying objects
^
    import copy
    copy.copy(x)
    copy.deepcopy(x)
    
**Shallo Copy :**
-  A shallow copy creates a new object which stores the reference of the original elements.

**Deep Copy :**
-  The deep copy creates independent copy of original object and all its nested objects.


**Links :**  
[Lambda Function](../functions.md)

**Unpacking of iterable :**
-  Assigning a tuple items to values in a single line.
-  `a, b, c = [1, 2, 3]`
-  `a, b, c = 1, 2, 3`

**Comprehension :**
-  List
   -  List can be created using another list.
      -  `List_B = List_A[n:m]`
   -  List can be created using lambda with map method.
      -  `List_B = list(map(lambda x:x**2, list_A))`
   -  List comprehension alternative to filter method. Below for way will get same output.
^
    List_A = [1, 2, 3, 4]
    filter_fun = list(filter(lambda x : x %% 2 == 0, List_A))
    list_comph = (x for x in List_A if x %% 2 == 0 )
^
