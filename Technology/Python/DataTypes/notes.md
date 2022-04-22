# Python Data Types :

Data type tells about type of value it can hold and also what operations can be performed on that value.
Python sets the variable type based on the value that is assigned to it.
Use ```type()``` function to get the data-type of any variable.
Convert data-type - str(123)

- [Text](#Text)    : str
- [Numeric](#Numeric)    : int, float, complex
- [Sequence](#Sequence)    : list, tuple, range
- [Mappingr](#Mapping)    : dict
- [Set](#Set)    : set, frozenset
- [Boolean](#Boolean)    : bool
- [Binary](#Binary)    : bytes, bytearray, memoryview

Scope wise variables types
- [Global](#Global)
- [Protected](Protected)
- [Private](##Private)

[Private](Private)
[Private](private)

## Text
  
## Sequence
  ### List
    List is like array but item can of different data-types.
    Uses - []
    
### Tuble
    Tuple are immutable i.e. cannot be modified after it is created.
    Uses - ()
    
### &emsp;Range
&emsp;&emsp; This is range section.

# Variable scopes
# Global
Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.

# Protected
Protected attributes are attributes defined with an underscore prefixed to their identifier eg. \_sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.

## Private
Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

## #Private
Private attributes are attributes with double underscore prefixed to their identifier eg. \_\_ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made

# Other types or objects

### Self
Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.

### __init__
__init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a __init__ method associated with them.
