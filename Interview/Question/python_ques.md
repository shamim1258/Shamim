# Python Preperation Questions

## Python Basic

1. How is memory managed in Python?  
[Python](../../Technology/Python/base.md) [Python2](../../Technology/Python/base.md) 
&emsp;<details>
Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.

2. What is pickling and unpickling?

3. Which libraries you have used?
4. How is memory managed in Python?
5. What are decorators in Python?
6. What is lambda in Python? Why is it used?
7. What are generators in Python?
8. What is the difference between .py and .pyc files?
&emsp;<details>
.py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program. We get bytecode after compilation of .py file (source code). .pyc files are not created for all the files that you run. It is only created for the files that you import.
Before executing a python program python interpreter checks for the compiled files. If the file is present, the virtual machine executes it. If not found, it checks for .py file. If found, compiles it to .pyc file and then python virtual machine executes it.
Having .pyc file saves you the compilation time.

9. Explain split() and join() functions in Python?
10. What does \*args and \*\*kwargs mean?
  
## Python Class

1. How does inheritance work in class?
2. Are access specifiers used in python?
&emsp;<details>Python does not make use of access specifiers specifically like private, public, protected, etc. However, it does not derive this from any variables. It has the concept of imitating the behaviour of variables by making use of a single (protected) or double underscore (private) as prefixed to the variable names. By default, the variables without prefixed underscores are public.</details>

3. Why is finalize used?
&emsp;<details>Finalize method is used for freeing up the unmanaged resources and clean up before the garbage collection method is invoked. This helps in performing memory management tasks.
  
4. What is init method in python?
&emsp;<details>The method is run as soon as an object is instantiated. It is useful for initializing any attributes or default behaviour of the object at the time of instantiation.
  
5. How will you check if a class is a child of another class?
&emsp;<details>This is done by using a method called issubclass() provided by python. The method tells us if any class is a child of another class by returning true or false accordingly.
  
## Python Libraries
1. Differentiate between a package and a module in python?
### Pandas
1. What do you know about pandas?
2. Define pandas dataframe?
3. How will you combine different pandas dataframes?
&emsp;<details>The dataframes can be combines using the below approaches:
append() method: This is used to stack the dataframes horizontally. Syntax:
df1.append(df2)
concat() method: This is used to stack dataframes vertically. This is best used when the dataframes have the same columns and similar fields. Syntax:
pd.concat([df1, df2]) 
join() method: This is used for extracting data from various dataframes having one or more common columns.
df1.join(df2)

4. Can you create a series from the dictionary object in pandas?
&emsp;<details>One dimensional array capable of storing different data types is called a series. We can create pandas series from a dictionary object

5. How to add new column to pandas dataframe?
&emsp;<details>A new column can be added to a pandas dataframe as follows:
import pandas as pd      
data_info = {'first' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),    
       'second' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}    
df = pd.DataFrame(data_info)    
#To add new column third
df['third']=pd.Series([10,20,30],index=['a','b','c'])    
print (df)    
#To add new column fourth
df['fourth']=df['first']+info['third']    
print (df)  

  
### Numpy
  
1. What do you understand by NumPy?
2. How are NumPy arrays advantageous over python lists?
