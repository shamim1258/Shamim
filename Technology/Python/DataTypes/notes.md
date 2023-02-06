# Data Types :

-  Data type tells about type of value it can hold and also what [operations](#operations) can be performed on that value.
-  Python sets the variable type based on the value that is assigned to it.
-  Use `type()` function to get the data-type of any variable.
-  Convert data-type - `str(123)`.
-  `None` is real object managed by python memory manager and all objects assigned with None will have same memroy reference.
-  Check the [Mutability](#mutability) section carefully than go through below point of deep understanding of variable assignment.
-  `sorted(iterable, key=key, reverse=true)` Sorted method can be used to sort iterables return type is sorted list.
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
   - [Mapping](#mapping)    : [dict](dictionary.md)
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
    - To convert one place decimal float number to two place decimal number -  `'{:.2f}'.format(0.4)`


## Sequence
-  Standard sequence methods.
   -  `item **in** seq`
   -  `item **not in** seq`
   -  concatenation `seq1 + seq2`, list and tuple support this but range not support this.
   -  repetition `s * n` where n is integer, list and tuple support this but range not support this.
   -  `len(s)`
   -  `min(s)` if ordering between elements is defined
   -  `max(s)`
   -  `index(i, j, k)` where i is required it will give first occurance of i in x, j is optional it is starting index to look and k is optional it is ending index till there it will look of i.
   
1.  **List**
- List is like array but item can of different data-types.
- Uses - []
- List methods are - append(), clear(), copy(), count(), extend(), pop(), remove(), reverse(), index(), insert(), sort()
- `append()` method mutate the list means when we append new item in list it will update the list object memory address information of original memory reference and not change the memory reference.
-  If we check the storage size of list using `sys.getsizeof()` when appending items in a for loop at few interval it increase the memory size of list and than after than for few item it does not increase mean it increase the memory size after few interval and in between remain same.
-  When we use list assignment like `list2 = list1` in this case id(list1) and id(list2) are different as new list object is created but the id of element will be same id(list1[0]) and id(list2[0]) will be same as both refering to same object.

2.  **Tuple**
- Tuple are immutable i.e. cannot be modified after it is created.
- Uses - ()
- Tuple methods only 2 - count(), index()
- `tpl = (1)` this is not tuple but int you can check by `type(tpl)` to make it tuple `tpl = (1,)`.
-  If we check the storage size of tuple using `sys.getsizeof()` the memory size of tuple keep on increasing with 8 byte with each new item.
-  When we use tuple assignment like `tuple2 = tuple1` in this case id(tuple1) and id(tuple2) are same as both refering to same object and items will also refer to same object.
    
2.  **Range**
- Create a sequence of number starting from 0 to n-1.
- Syntax `range(start, stop, step)`

## Mapping
- Mapping data types are key, value pair types - dict.
^
1.  [Dictionary](dictionary.md)
-  Methods - clear(), copy(), formkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
-  `dict.get('abc')` and if 'abc' is not found in keys of dict than it will not return error but None.
-  Few most common methods :
   -  items
      -  Syntax : `dict.items()`
      -  Return object type is dict_item which is view of key,value pair
      -  Example :
^
   d = {1: 300, 2:500, 3:100, 4: 200, 5:400}
   i = d.items()
   print(i)
   Output :: [(1,300), (2,500), (3,100), (4,200), (5,400)]
^

## Set
1.  **Set**
-  Set is unordered mutuable collection of objects.
-  Syntax `set_A = {1, 2, 3}`
-  In a general way it is a dictionary without keywords.
-  Defining empty set is bit tricky as set_A = {} this will not be a set but dict to create empty set - `set_A = set()`
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

## Iterable
-  It is a container type of object and we can list out elements in object one by one.
-  Iterable is not necessary a sequence type example set.

# Variable scopes
-  **Namespace** is collection of object(variable/method) and object information(value) for the given scope(built-in, global, enclosed and local).  
-  Python itself maintain Namespace in the form of python dictionary.  
-  The Namespaces are searched for scope resolution according to the LEGB rule.
-  **Scope** refers to the coding region from which a particular Python object is accessible. Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
-  When we define a variable at that point scope is not created when that variable is called at that point scope is created for that variable.
-  A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends, the lifetime of that namespace comes to an end. Hence, it is not possible to access the inner namespace objects from an outer namespace.

-  Types of Namespcae
   -  **Built-In**
      -  It contains the names of all of Python’s built-in objects. These are available at all times when Python is running.
      -  To get the list of namespace in built-in use command `dir(__builtins__)`
      -  Example : print, range, dict, list, set, dir, globals, local, id, input, len, etc.
   -  **Global**
      -  It contains any names defined at the level of the main program.
      -  Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates.
      -  There may not be the only one global namespace that exists. The interpreter also creates a global namespace for any module that your program loads with the import statement.
   -  **Enclosing**
      -  When the main program calls function f() python creates a namespace for f() is Enclosing namespace.
      -  Also called nonlocal scope.
      -  This lies between global and local scope.
   -  **Local**
      -  When the main function f() in enclosing namespace calls function g() than python create a namespace is Local namespace.

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
   -  The function plus extended scope that contains free variable together called closure.
   -  When inner function refers to its outer function variable in this case the inner function and its outer variable together called closure. In below example inner function with outer function var variable is closure
^
    def outer():
        var = 10       #Closure
        def inner():   #Closure
            print(var) #Closure
        return inner
    fn = outer()
^
   -  In above example if we want to check the if there is any close we can use `fn_.__closure__` this will return the cell memory reference and to check the free variables `fn.__code__.co_freevars`.
   -  Problem here is var variable exists in scope of outer and inner function so when inner function called the scope of outer function already ended how to get the value of var variable to solve this python as an exception identify this as closure than outer function var hold the memory address of a cell(this is memory address which hold the memory address of where actual value of var kept) and inner function also refers to this cell, so both refers to the cell and cell refers to address which holds the value of object.
     
**Global :**
-  Global scope is the module scope.
-  Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.
-  Python don't have concept of Truely Gobal scope across all modules and only exception to this is some globally available built-in objects which are `True, False, None, print, dict`

-  **Protected :**
   -  Protected attributes are attributes defined with an underscore prefixed to their identifier eg. \_sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.

-  **Private :**
   -  Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

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
-  Iterators allow us to both work with and create lazy iterables that don’t do any work until we ask them for their next item.
-  Because of their laziness, the iterators can help us to deal with infinitely long iterables. In some cases, we can’t even store all the information in the memory, so we can use an iterator which can give us the next item every time we ask it. Iterators can save us a lot of memory and CPU time.
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
   -  Iterators don’t have to be finite. It’s perfectly reasonable to write an iterator that produces an infinite stream of data.

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
- Slicing is taking some part of. Syntax ``` [start : stop : step] ```. Default values of start is 0, stop is index till where it will slice but not include stop index and step is 1.  
-  Slicing can be done on strings, arrays, lists, and tuples.
-  If index is out of range of the given sequence than also it will the output and not error out.
^
    x = 'abc'
    print(x[1:30]) #output will be bc
^
-  It always creates the new object not mutate the original object.
-  If we want to reverse a string we can use `str[::-1]` in this case python itself changes the default values to str[stop : start : -1].
-  We can also use slicing for assignment also even the number of items in assignment not required to be same also in case of assignment the list is mutate and not create new object reference.
^
    list1 = [1, 2, 3, 4, 5]
    list1[0:2] = ('a', 'b', 'c')
    #Output list1 = ['a', 'b', 'c', 3, 4, 5] here replaced 1, 2 with 'a', 'b', 'c' even number of items are not same but it works
^
- **Slice definition** is naming a slice and it will be object of type slice and instead of using [start:end] we can use slice object by `slice(start, end)` where start and end are the indexes where we exclude end index value.
^
    list1 = [1, 2, 3, 4, 5]
    s = slice(0, 2) #this is the slice object s we can also check by type(s) as slice
    list2 = list1[s] #Here we are using slice named object s 
    #output list2 = [1, 2]
^
-  **Insertion** using slice can be but the slice object should be empty like list[n:n] it will empty list [], also it will mutate the list.
^
    list1 = [1, 2, 3, 4, 5]
    list1[ 1 : 1 ] = 'abc'
    #output list1 = [1, 'a', 'b', 'c', 2, 3, 4, 5]
^

**Concatenation :**
-  Use `+` operator to concatenate 2 sequence where both object must be of same type like list1 + list2 or tuple1 + tupel
-  Concatenation does not udpate the original object but will create new object in case want to mutate original object we can use list append method.
^
    names = ['Ram', 'Shyam'] # Memory Reference 1x1002 containing Ram and Shyam
    names = names + ['Gopal'] # Memory Reference 1x1005 containing Ram, Shyam and Gopal and memory address 1x1002 also exists but names now reference to 1x1005
^

-  Example
^
    x = [1, 2]
    a = x + x
    #Output a = [1, 2, 1, 2]
^
-  The above example works fine as sequence items are immutable like x = [1, 2] where 1 and 2 are immutable if it contains string it will also work fine as string is also immutable but if items are mutable than it will create issue because concatenating same object will not copy these object to new variable but new object reference to previous object 'x' so here a will refer to x 2 times so in below example when mutable object is modified it will update it all places referencing same object.
^
    x = [[1, 2], [1, 2]]
    a = x + x
    #Output a = [[1, 2], [1, 2], [1, 2], [1, 2]]
    a[0][0] = 5
    #Output a = [[5, 2], [1, 2], [5, 2], [1, 2]]
^

**Repetition :**
-  Use `*` operator to repeat a sequence n times where n is integer.
-  Example
^
    x = [1, 2]
    a = x * 3
    #Output a = [1, 2, 1, 2, 1, 2]
^
-  The above example works fine as sequence items are immutable like x = [1, 2] where 1 and 2 are immutable if it contains string it will also work fine as string is also immutable but if items are mutable than it will create issue because repetition of same object will not copy these object to new variable but new object reference to previous object 'x' so here a will refer to x 3 times so in below example when mutable object is modified it will update it all places referencing same object.
^
    x = [[1, 2], [1, 2]]
    a = x * 2
    #Output a = [[1, 2], [1, 2]]
    a[0][0] = 5
    #Output a = [[5, 2], [5, 2]]
^

**Join :**
-  It concatenates the string items by putting between them the given string.
-  Syntax `'#'join(['a', 'b', 'c'])` Output will be `a#b#c`.
-  The sequence items must be **string only**.

**Enumerate :**
-  It takes input as iterable and output the it's index as tuple combination and each item.
-  Example : `str1 = list('ababc')` output will be `[(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b'), (5, 'c')]`

**Index :**
-  index(i, j, k) where i is required it will give first occurance of i in x, j is optional it is starting index to look and k is optional it is ending index till there it will look of i.
-  If given string in not found it will give exception error that sub-string not exists.

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
    list1 = [[1, 2], 3, 4]
    list2 = list1.copy()
    #so now if we check with id for list1 and list2 will be different but list1[0] and list2[0] will be same and list1[1] and list2[1] will also same
    list1[0].append('x')
    #output for list1 = [[1, 2, 'x'], 3, 4]
    #output for list2 = [[1, 2, 'x'], 3, 4] this will also be udpated as elements memory address is same

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
