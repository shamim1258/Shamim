# My Questions

1.  Synchronous and Asynchronous what you have used.


## Python

1.  We have list[0,1,2..9] how we can print this list in reverse order.
&emsp;<details>Use rever method of list, this will reverse the list whenever it is referred.
`list.reverse()`

1.  We have list[1,2,3,4] if input number in list is even print square of it and if odd print cube of it, output should be [1,4,27,16].
&emsp;<details>
Use % operator for getting the remainder input % 2 == 0 to get square = num**2 to get cube = num**3
    
1.  How to implement security in python.
&emsp;<details>
Careful when downloading the package PyPl-packages issues can be reported but package added to pypl does not undergo review. We can use https://snyk.io/advisor/ to check package security health.
<br>Use virtual environment - if you install a package dependency with malicious code in one project, it will not affect the others. Each project’s packages are isolated from each other.
<br>Set `Debug = False` in production - Displaying errors in our code publicly could show a weakness in our security that will be exploited.
<br>Make sure to switch debugging to False in production to prevent leaking sensitive application information to attackers.
<br>Be careful with string formatting.
<br>- (De)serialize very cautiously - When handling data deserialization in Python, I’ll recommend only deserializing data from a trusted source as its possible that a malicious arbitrary code could be hidden in the data.
<br>* Do not use the system standard version of Python - problem with build python is its not latest version.
<br> Always double check before commiting any file to git that it does not contain any password or sensitive information.
<br> Protect against SQL injections.
<br> Use abosulte import instead of relative import.
<br>&emsp;from package1 import module1 /* Absolute Import */
<br>&emsp;from .some_module import some_class /* Relative Import */
<br>Use the latest version of your HTTP requests library, confirm if the library is handling the SSL verification of the source you sent requests to, if you are using standard library urllib,  you should follow best practices to prevent request smuggling.
    
1.  What is garbage collection.  
[Memory Management](../../Technology/Python/base.md##memory-management)  
&emsp;<details>
Prior to Python version 2.0, the Python interpreter only used reference counting for memory management.
Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented.When the reference count becomes zero, the object is deallocated.
    
1.  Difference between List and Tuple.
[Difference Between List and Tuple](../../Technology/differences.md)  

1.  List and Dictonary comprehenion.
&emsp;<details>
<br>Comprehension : Creating new sequences using a given python sequence.
<br>
    
1.  What is lambda function.
    
1.  Explain methods - filter, map and reduce.
    
1.  What is Multilevel and Multiple inheritance.
    
1.  How resolution works in Multilevel and Multiple inheritance.
    
1.  What is the output of - 
def foo(a,b,c=None,d=None, *args,**kargs):
print(a,b,c,d)
foo(1,2,3,4)
foo(1,2,3,4,5,6)
foo(1,2,3,c=4).
    
1.  Explain cyclic dependency.
    
1.  What is recursion
    
1.  Write a recursive function to reverse a string.
    
1.  Difference between generators and iterators.
    
1.  Difference between Shallow copy and Deep copy.
    
1.  How break, continue and pass statement works.
    
1.  What is overriding and overloading function in python.
    
1.  What is global and local variables.

## Django

1.  Cache in django.
    
1.  Cons of django.
    
1.  What is the use of middleware in django
    
1.  What is the use of CSRF token.
    
1.  What is cookies.
    
1.  Output
students = Student.object.all()
print(students)
    
1.  In the above question when is the query executed to get data from db.
    
1.  what is queryset.
    
1.  Cycle of Request and Response.
    
1.  If we have a model with 500 million records how we can improve the performance.

1.  We want to create product hierarchy how we can do that.
    
1.  Explain signal and receivers.
    
1.  Explain what is decorator and custom decorators.
    
## Rest API

1.  If API is slow how can we improve performance.

    
## Database

1.  How to get the roundoff values without decimal in sql select statement.
&emsp;<details>
Use the ROUND() function to round of the number it takes 2 arguments Round(number, decimal) where number is the input number to be round off and decimal is no of decimal places to be round off.
`SELECT ROUND(SALARY) FROM DEPARTMENT`.

## Other
    
1.  Challenges in Remote working.
    
1.  What disturbances you face working remotely.
    
1.  Ways to improve performace and client satisfactory.

1.  What application used to connect your team.
