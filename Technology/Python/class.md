# Class
- Classes are created by keyword class.
- Attributes or Properties are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: ```Myclass.Myattribute```.
- An **Object** is an instance of a Class.
- **self** represents current object of class and it has be the first argument of function in class, tradinally using self but any other word can be used inplace of self.
- **__init___** method in class initize the object and takes the first argument `self` which is object of class.

## Inheritance
-  Inheritance is the capability of one class to derive or inherit the properties from another class.
-  Inheritence is useful when you want to narrow a scope in the inherited class.  
-  Advantages :
   -  It represents real-world relationships well.
   -  It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
   -  It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
-  **Parent Class** is called the base class and any class can be a base class.
^
    class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
      def printname(self):
        print(self.firstname, self.lastname)

-  **Child Class** is one which inherits from base class.
^
    class Student(Person):
    pass
    --Now the Student class has the same properties and methods as the Person class.
    x = Student("Mike", "Olsen")
    x.printname()
    
-  The child class __init__() function overrides the inheritance of the parent class __init__() function and the child class will no longer inherit the parent's __init__() function.
-  **Overriding :** If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden by child.
-  Class build in function :
   -  `super().<function or variable name>` in the child class used to inherit any given methods and properties from its parent.
   -  'isinstance()' returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.
   -  `issubclass()` return True if class interitance given in input is true.
-  **Method Resolution Order (MRO) :** describes the search path of the class which Python uses to get the appropriate method in classes that contain the multi-inheritance.
  -  `<Class_Name.mro()>` is used to see the method resolution order of a class.
  -  It follows **left(deep) to right** so it will first search first left class than all its super/parent classes than its right class if not searched yet.

### Types of Inheritance
-  **Single inheritance :**
   -  When a child class inherits from only one parent class, it is called single inheritance.
-  **Multiple inheritance :**
   -  When a child class inherits from multiple parent classes.
   -  `class child_class(parent_1, parent_2)`
-  **Multilevel inheritance :**
   -  When we have a child and grandchild relationship.
^
    class BaseClass():
    class ChildClass(BaseClass):
    class GrandChildClass(BaseClass):
^
-  **Hierarchical inheritance :**
   -  More than one derived classes are created from a single base.
-  **Hybrid inheritance :**
   -  This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
### Variable Access and Scope
-  **Private member**
   -  The private member of parent are not accessible to the child class.
   -  Use __ to make a variable private `self.__variable_name = 'value'`

### Abstract Base Class
-  An abstract base class is a class from which we want to create subclasses, but the base class is not something we can instantiate (create).
-  One canonical example is a vehicle. A vehicle is an abstraction, whereas cars and motorcycles are specific examples of vehicles. We would never want to create a “vehicle” in our code, but we certainly might want to create cars, motorcycles, bicycles, trucks, and other kinds of vehicles.
-  Abstract Base Classes (ABCs) represent abstractions.
-  To implement this we can use python built-in module **abc** `from abc import ABC, abstractmethod`
^
    from abc import ABC, abstractmethod 
 
    class Vehicle(ABC): 
        """This class inherits from (or subclasses) ABC""" 
        @abstractmethod 
        def number_of_wheels(self): 
            """This method is abstract, so the class cannot be instantiated. This method will be overridden in subclasses of Vehicle.""" 
           pass 
    class Car(Vehicle): 
        """This class inherits from the abstract base class Vehicle""" 
        def number_of_wheels(self): 
            """Override the abstract method in the base class""" 
            return 4 
    # create a car called c: SUCCEEDS 
    c = Car()  
    # print the number of wheels that c has: SUCCEEDS 
    print(c.number_of_wheels())  
    # Try to create a Vehicle: FAILS 
    v = Vehicle() 
^

### self
- We do not give a value for this parameter when we call the method, Python provides it.

### __init__ method
- __init__ method is similar to constructors used to initializing the object.
- It runs as soon as an object of a class is instantiated.
