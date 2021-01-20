Polymorphism: "Many forms"

One thing, several forms --> function overloading.
One action, different activities --> function overloading.


================================================================
One Action                          Different Activities
-----------                         ---------------------
1. Shifting gears                   1. Forward - Drive
                                    1. Reverse

2. Click of a Mouse                 2. Open Window
                                    2. Close Window
                                    2. Minimize Window
                                    2. Get Dropdown Menu
==================================================================

Duck typing philosophy of Python:
---------------------------------
At runtime "if it walks like a duck and talks like a duck, it must be a duck," Python follows this principle. This is
called duck typing philosophy of Python. Look at PolyDuck.py

There is a problem in PolyDuck. What if the object does not contain talk function --> We would get an attribute error.
What is the solution? use function hasattr(object, attribute_name)


Overloading:
-------------
We can use the same operator or method for different purposes.

Example: + operator can be used for arithmetic addition an string concatenation
         *  Multiplication and repetition of string

Three Types of Overloading: (In Python)
----------------------------
1. Operator overloading
2. Function overloading
3. Constructor overloading

Operator Overloading:
---------------------
Same operator for different purposes, which is operator overloading. Operator overloading is supported in Python. We can
use __add__(self, other) functions. Look at Operator Overloading.py under directory called overloading.

FROM:
https://www.geeksforgeeks.org/operator-overloading-in-python/
    Binary Operators:
    ----------------
        Operator    	 Magic Method
        --------        -------------
            +	        __add__(self, other)
            –	        __sub__(self, other)
            *	        __mul__(self, other)
            /	        __truediv__(self, other)
            //	        __floordiv__(self, other)
            %	        __mod__(self, other)
            **	        __pow__(self, other)
            >>	        __rshift__(self, other)
            <<	        __lshift__(self, other)
            &	        __and__(self, other)
            |	        __or__(self, other)
            ^	        __xor__(self, other)

    Comparison Operators :
    ---------------------
          Operator	    Magic Method
          --------      -----------------
            <	        __LT__(SELF, OTHER)
            >	        __GT__(SELF, OTHER)
            <=	        __LE__(SELF, OTHER)
            >=	        __GE__(SELF, OTHER)
            ==	        __EQ__(SELF, OTHER)
            !=	_       _NE__(SELF, OTHER)

    Assignment Operators :
    ---------------------
          Operator	    Magic Method
          --------      -----------------
            -=	        __ISUB__(SELF, OTHER)
            +=	        __IADD__(SELF, OTHER)
            *=	        __IMUL__(SELF, OTHER)
            /=	        __IDIV__(SELF, OTHER)
            //=	        __IFLOORDIV__(SELF, OTHER)
            %=	        __IMOD__(SELF, OTHER)
            **=	        __IPOW__(SELF, OTHER)
            >>=	        __IRSHIFT__(SELF, OTHER)
            <<=	        __ILSHIFT__(SELF, OTHER)
            &=	        __IAND__(SELF, OTHER)
            |=	        __IOR__(SELF, OTHER)
            ^=	        __IXOR__(SELF, OTHER)

    Unary Operators :
    ----------------
          Operator      Magic Method
          -------       --------------------
            –	        __NEG__(SELF, OTHER)
            +	        __POS__(SELF, OTHER)
            ~	        __INVERT__(SELF, OTHER)

Method Overloading:
--------------------
If two methods hae the same name but different type of argument  then those method are said to be overloaded.
Example:
    m1(int a)
    m1(double d)
But, in Python method overloading is not possible. If we have two methods with the same name then the second or later
method will be considered.

Constructor Overloading:
------------------------
In Python constructor overloading is not possible. If we define multiple constructors then only the last constructor
will be considered.

Method Overriding: (The same is true for constructors.)
------------------
When we declare a child class from a parent class we can override any parent-class method by defining the same method
in the child-class. Look at Method Overridding.py under the OverRiding Folder.

Abstract Classes and Abstract Methods:
--------------------------------------
  Abstract Class:
  ---------------
    An abstract class is a class from which it is not possible to create and object. Abstract classes  simply act as a
    template for other classes. Look at abstractclass.py under the Abstract folder.
    Rule:
    ----
        1. Every Abstract Class must be derived from ABC class which is present in abc module.
        2. An abstract class must contain at least one abstract method.
    Note:
    ----
        Abstract classes can contain both abstract as well as non-abstract methods.

  Abstract Method:
  ----------------
    Sometimes we do not know about implementation but still we declare a method. Such methods are called
    "Abstract Methods." Such methods have declaration but no implementation.In Python we can declare an abstract method
    by using the @abstractmethod decorator.


Interfaces:
----------
An abstract class that contains only abstract methods then that is called and interface.

