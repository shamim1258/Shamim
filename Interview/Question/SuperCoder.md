# SuperCoder

**Python :**.
1. How security can be implemented in Python.
&emsp;<details>
Careful when downloading the package. - PyPl - packages issues can be reported but package added to pypl does not undergo review. We can use https://snyk.io/advisor/ to check package security health.
User python capacity for virtual environment.
Set `Debug = False` in production. - Make sure to switch debugging to False in production to prevent leaking sensitive application information to attackers.
<li>Be careful with string formatting.</li>
- (De)serialize very cautiously
Do not use the system standard version of Python - problem with build python is its not latest version.
  </details>
  
1. How security can be implemented in Django.
&emsp;<details>
  Use SSL - Deploy your site behind HTTPS.
  Changing URL - Change the default admin URL from /admin/ to something else
  Require stronger passwords
  Never run `DEBUG` in production - When DEBUG is set to True in your settings file, errors will display with full tracebacks that are likely to contain information you don't want end users to see. 
  
1.How to use cache in python.
&emsp;<details>
  The functools module in Python deals with higher-order functions, that is, functions operating on(taking as arguments) or returning functions and other such callable objects. The functools module provides a wide array of methods such as cached_property(func), cmp_to_key(func), lru_cache(func), wraps(func), etc. It is worth noting that these methods take functions as arguments.
  lru_cache() is one such function in functools module which helps in reducing the execution time of the function by using memoization technique.
  @lru_cache(maxsize=128, typed=False)

Parameters:
maxsize:This parameter sets the size of the cache, the cache can store upto maxsize most recent function calls, if maxsize is set to None, the LRU feature will be disabled and the cache can grow without any limitations
typed:
If typed is set to True, function arguments of different types will be cached separately. For example, f(3) and f(3.0) will be treated as distinct calls with distinct results and they will be stored in two separate entries in the cache
  
1.Synchronous and Asynchronous works in python.
&emsp;<details>
  On a s̲y̲n̲c̲h̲r̲o̲n̲o̲u̲s̲ request, you make the request and stop executing your program until you get a response from the HTTP server (or an error if the server can't be reached, or a timeout if the sever is taking way, way too long to reply) The interpreter is blocked until the request is completed (until you got a definitive answer of what happened with the request: did it go well? was there an error? a timeout?... ).  
  On a̲s̲y̲n̲c̲h̲r̲o̲n̲o̲u̲s̲ requests, you "launch" the request, and you kind of "forget about it", meaning: The interpreter continues executing the code after the request is made without waiting for the request to be completed.
