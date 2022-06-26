# Functions

## Normal Function
- `def` keyword used to create function.

## Lambda Function
-  Anonymous function means that a function is without a name.
-  `lambda` keyword is used to create anonymous functions.
-  Syntax  
   -  `lambda arguments : expression`.  
   -  def myfunc(n):  
^
    return lambda a,b : a * n * b
    mydoubler = myfunc(3)
    print(mydoubler(10,20))
      
-  It can have any number of arguments but only one expression, which is evaluated and returned.


## Build-in Function
- The Python interpreter supports many functions that are built-in: sixty-eight, as of Python 3.6.


### Math
  -  ```max()```&emsp;- Returns the largest of the given arguments or items in an iterable.
  -  ```min()```&emsp;- Returns the smallest of the given arguments or items in an iterable.  


### Type Conversion
  -  ```str()```&emsp;- Returns a string version of an object.
  -  ```ord()```&emsp;- Returns integer representation of a character.
  -  ```type()```&emsp;- Returns the type of an object or creates a new type object.  


### Iterables and Iterators
  -  ```all()```&emsp;- Returns True if all elements of an iterable are true.
  -  ```len()```&emsp;- Returns the length of an object.
  -  ```zip()```&emsp;- Creates an iterator that aggregates elements from iterables.


### Input Output
  -  ```open()```&emsp;- Opens a file and returns a file object.
  -  ```print()```&emsp;- Prints to a text stream or the console.


### Miscellaneous
  -  ```eval()```&emsp;- Evaluates a Python expression.
  -  ```len()```&emsp;- Returns the length of an object.
