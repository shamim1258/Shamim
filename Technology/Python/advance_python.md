# Advance Python

**Important Points to Remember :**
-  [Higher Order Function](functions.md)  
   -  These function return iterables so cannot be resued and return value only once so to store get this in list `list(map())`
   -  Function like `map(), filter(), sorted(), zip()` are not executed when called with arguments but it is executed when the calling variable is used to retrive the output values.
^
    var = map(lambda x : x ** 2, (1, 2, 3))
    print(var)   # map function is not executed here it will give output <map object at 0x00012>
    for i in var:
        print(i) # here we are retiving output values so here map function is executed to be exact.
^
   -  Filter with None function example
^
    var = list(filter(None, [1, 'a', 0, '', None, 'b', false])
    print(var) #Output [1, 'a', 'b']
^
