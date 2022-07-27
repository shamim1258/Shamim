# Functions

## Normal Function
-  `def` keyword used to create function.
-  Parameter are variable in the function definition and Arguments are passed when we call function.
-  **Default Parameter**
   - We can define default parameter `def func(a, b = 100)`
   - If we give any default parameter than all the parameter after that must also be default parameter otherwise it will error out.
-  **Keyword Arguments**
   -  When we call function we can specify the actual parameter name used in function definition in argument
^
    def myfun(a, b = 1, c = 2):
        pass
    myfun(a = 0, c = 3)
^
   -  If we specify keyword argument even if parameter don't have default value than we can specify the argument in any order but here also all argument after the first argument with keyword must all have keyword.
^
    def myfun(a, b, c):
        pass
    myfun(c = 0, a = 3, b = 4)
    myfun(c = 10, 5, 20) #This will error out
^
-  **\*arg**
   -  This specify there can be 0 or more arguments.
   -  \*arg is tradition name but it can have any name but '\*' is required '\*abc' this will also work.
^
    def myfun(a, b, \*arg):
        pass
    myfun(1,2)
    myfun(1,2,3,4,5)
^
   -  \*arg is tuple not list.
   -  We cannot add more position argument after '\*arg' example `def myfun(a, b, c, *arg, d)` here we cannot add 'd'.

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

## Higher Order Function
-  A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output.
-  Decorators are the most common use of higher-order functions.
-  Example : Build-in functions - `filter()`, `map()`.

## Recursive Function
-  Recursive function are function which calls itself.
-  Example
^
    def factorial(x):
      if x==1:
        return 1
      else:
        return (x\*factorial(x-1))
-  By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in `RecursionError`.
-  Disadvantages :
   -  Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
   -  Recursive functions are hard to debug.

## Build-in Function
- The Python interpreter supports many functions that are built-in: sixty-eight, as of Python 3.6.
- Few important function are : **map(), filter(), reduce()**

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
     -  Syntax `filter (function, iterables)`
     -  Takes input as list, tuple, set or container of iterator.
     -  Takes each element of input and if evelautes to True or not.
     -  **Returns iterator** that is filtered.
     -  It is normally used with Lambda functions to separate list, tuple, or sets.
     -  Example `filter(lambda x: x % 2 != 0, [0,1,2,3,4])`
-  `map()`
   -  `map(fun, iter)`
   -  Returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.).
   -  It returns the values of the input function.
-  `reduce()`
   -  This function is defined in “functools” module.
   -  The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
   -  At first step, first two elements of sequence are picked and the result is obtained.
   -  Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
   -  This process continues till no more elements are left in the container.
   -  The final returned result is returned and printed on console
^
    import functools
    lis = [1, 3, 5, 6, 2, ]
    print(functools.reduce(lambda a, b: a+b, lis))
    # Output 17 = 1+3, 4+5, 9+6, 15+2
    
-  `dir()`
   -  It takes argument as objects and return the attributes build-in and custom for that object.
    
