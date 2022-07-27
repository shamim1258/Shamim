# Advance Python

**Important Points to Remember :**
-  [Higher Order Function](#high-order-function.md)
   -  Function like `map(), filter(), sorted()` are not executed when called with arguments but it is executed when the calling variable is used to retrive the output values.
^
    var = map(lambda x : x ** 2, (1, 2, 3))
    print(var)   # map function is not executed here it will give output <map object at 0x00012>
    for i in var:
        print(i) # here we are retiving output values so here map function is executed to be exact.
^
