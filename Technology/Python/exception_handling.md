# Exception Handling

- We use `try..except..finally` for exception handling in python.
- Example code
^
    try:
        print("try block")
    except:
        print("except block")
    finally:
        print("finally block")
^
-  `finally` is always executed even if we put `break` or `continue` statement in except
