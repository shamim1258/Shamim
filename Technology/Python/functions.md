# Functions

## Normal Function
- `def` keyword used to create function.

## Lambda Function
-  Anonymous function means that a function is without a name.
-  `lambda` keyword is used to create anonymous functions.
-  Syntax    
    - `lambda arguments : expression`.
-  Example - Here `myfun(3)` 3 is argument for function myfunc not lambda `mydoubler(10,20)` is arguments to lambda function.
^
    def myfunc(n):  
      return lambda a,b : a * n * b
    mydoubler = myfunc(3)
    print(mydoubler(10,20))
   
-  It can have any number of arguments but only one expression, which is evaluated and returned.
-  If we directly call lambda it will return the lambda object not it's return value.
   -  `print(lambda a : a + 1)`
-  To get the return value call this with the arguments.
   -  Calling directly
      -  `print((lambda a : a + 1)(5))`
   -  Calling via variable  
^
    x = lambda a : a + 1
    print(x(5))
    
   -  Calling inside function is above Example point-3
      
-  The power of lambda is better shown when you use them inside another function.

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
  -  `eval()`&emsp;- Evaluates a Python expression.
  -  `len()`&emsp;- Returns the length of an object.
  -  `filter()`
     -  Takes input as list, tuple, set or container of iterator.
     -  Takes each element of input and if evelautes to True or not.
     -  **Returns iterator** that is filtered.
     -  It is normally used with Lambda functions to separate list, tuple, or sets.
     -  Example `filter(lambda x: x % 2 != 0, [0,1,2,3,4])`
