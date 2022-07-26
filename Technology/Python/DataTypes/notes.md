# Data Types :

-  Data type tells about type of value it can hold and also what [operations](#operations) can be performed on that value.
-  Python sets the variable type based on the value that is assigned to it.
-  Use ```type()``` function to get the data-type of any variable.
-  Convert data-type - ```str(123)```.
-  Check the [Mutability](#mutability) section carefully than go through below point of deep understanding of variable assignment.
-  Mutable object hold the memory address and the state or value of data this address hold can be changed keeping the same memory address of variable.
-  Immutable object hold the memory address and state or value of data this address hold cannot be changed so when assigning new value it changes the memory reference to some other address where new value present and the previous memory address still having the previous value.
-  A variable actually hold the memory reference and not the actual value whether mutable or immutable. `a = 10`
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
    strb = "hello"
^

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

# Variable scopes
**Global :**
- Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.

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
