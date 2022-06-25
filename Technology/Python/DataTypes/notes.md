# Python Data Types :

Data type tells about type of value it can hold and also what [operations](#operations) can be performed on that value.
Python sets the variable type based on the value that is assigned to it.
Use ```type()``` function to get the data-type of any variable.
Convert data-type - ```str(123)```.

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
^
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
### &emsp;Global
- Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.

### &emsp;Protected
- Protected attributes are attributes defined with an underscore prefixed to their identifier eg. \_sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.

### &emsp;Private
- Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

# Other objects Types

**Generator Function :**
A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.
    # A generator function that yields 1 for first time,
    # 2 second time and 3 third time
    def simpleGeneratorFun():
      yield 1            
      yield 2            
      yield 3


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
