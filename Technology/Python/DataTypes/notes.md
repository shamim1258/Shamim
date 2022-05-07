# Python Data Types :

Data type tells about type of value it can hold and also what [operations](#operations) can be performed on that value.
Python sets the variable type based on the value that is assigned to it.
Use ```type()``` function to get the data-type of any variable.
Convert data-type - ```str(123)```.

- [Text](#text)    : str
- [Numeric](#numeric)    : int, float, complex
- [Sequence](#sequence)    : list, tuple, range
- [Mappingr](#mapping)    : dict
- [Set](#set)    : set, frozenset
- [Boolean](#boolean)    : bool
- [Binary](#binary)    : bytes, bytearray, memoryview

[Scope](#variable-scopes) wise variables types
- Global
- Protected
- Private

Check the [operations](#operations) on data-types.

## Text
### &emsp;str
- Strings are sequences of character data.
- Interpreting a character or sequence of characters within a string differently use ```\``` as **Escape Sequences**.
- **Raw String** - literal is preceded by r or R, which specifies that escape sequences in the associated string are not translated. The backslash character is left in the string: ```>>> print(r'foo\nbar')
foo\nbar```
- **Triple Quoted Strings** - Escape sequences still work in triple-quoted strings, but single quotes, double quotes, and newlines can be included without escaping them.

## Numeric
### &emsp;int
- In Python 3, there is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount of memory your system has.

### &emsp;float
- float values are specified with a decimal point.


## Sequence
### &emsp;List
- List is like array but item can of different data-types.
- Uses - []
    
### &emsp;Tuble
- Tuple are immutable i.e. cannot be modified after it is created.
- Uses - ()
    
### &emsp;Range
- This is range section.

# Variable scopes
### &emsp;Global
- Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.

### &emsp;Protected
- Protected attributes are attributes defined with an underscore prefixed to their identifier eg. \_sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.

### &emsp;Private
- Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

# Other objects Types

### &emsp;self
- Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.

### &emsp;__init__
- __init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a __init__ method associated with them.

### &emsp;docstring
- Represented with triple quotation marks used for documents. __doc__ attribute.
Syntax ``` ''' This is doc string. '''  ```

# Operations

### &emsp;Slicing
- Slicing is taking some part of. Syntax ``` [start : stop : step] ```. Default values of start is 0, stop is number of items and step is 1.  
Slicing can be done on strings, arrays, lists, and tuples.
