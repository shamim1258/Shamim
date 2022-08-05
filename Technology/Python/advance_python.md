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

**Concatenation :**
-  Use `+` operator to concatenate 2 sequence.
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
    #Output a = [[1, 2], [1, 2]]
    a[0][0] = 5
    #Output a = [[5, 2], [5, 2]]
^

