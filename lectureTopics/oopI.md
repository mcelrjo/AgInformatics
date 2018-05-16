
### Object Oriented Programming, Part I

And now we come to the part that really seems to throw people for a loop when learning programming with Python.  Until this point the _syntax_ has been intuitive (for the most part).  Basically what we have learned to do is developed logical statements - _if, then, therefore_ type logical statements or _while_ this thing is True, do this thing.  While it probably took some time to get comfortable with the _syntax_ of these type statements, they really are intuitive in many ways.  We make these type of logical decisions everyday.  Now you are just learning to write them in a computer language.

##### And now for something completely different ..... The __CLASS__ Statement

What make this next part is the _syntax_.  We are moving into an area that is very _computer sciency_ - The Class Statement.  Remember the first thing I said in the module for this class -- __Everything is an object__ and objects are of a specific type.  Classes allow you to define a new type of objects.  

To understand this, let's consider what the _math_ module is actually doing.  When you import the math module, you import along with it a suite of functions that can be used along with it.  The math modules groups a bunch of similar things together.

```python
import math

math.sqrt(25)

>>>5.0

```
I think of the math module as being a class, and the methods associated with that class as being the the functions that are defined with that class.  That is basically what we are going to do.  We are going to start off defining a new class name.  

```python
class Soil(object):
	'''This is my soil class used to monitor important properties related to the soil health.
	'''
	def __init__(self, basicType, P, K):
		self.basicType = basicType
		self.P = P
		self.K = K
```

So what is going on here?  First, I have established a new class I am calling "Soil" and I passing the "object" to soil.  This is a little tricky to understand.  Basically this sets up "Soil" as a _superclass_ that does not inherit from any other classes, only directly from the top-most class _object_.  This is my way of explaining it.    

Second, inside the class the first thing that is done is to _instantiate_ the class by using the Python special method "__init__".  "__init__" is used to define new attributes assocaited with the class.  This is the first special method you are going to learn about but there are many more.  The first argument passed to __init__ is "self", in other words it is the object itself that is the first thing.  _self_ is actually pointing to the instance of the class.  The next three are defined by the person setting up the class -- in this case "basicType", "P", and "K".  These are _instance variables_.  These arguments are the only three passed when setting up a new instance of that class.  Here is how you set up an instance.

```python
field7 = Soil("clay", 140, 50)

print field7.basicType
print field7.P
print field7.K
print field7
```
In this case, an _instance_ of the object soil was established (instantiated) and bound to the name "field7".  Using the "." operator (dot notation), the instance variables can be accessed.  But notice what happens when you print instance itself.  No information is returned, only information identifying the object instance and where it is stored in data.  Understand that this is a new object that has been created and that as many objects as you want can be created using this new class.

```python
field8 = Soil("loam",120, 60)

print field8.basicType
print field8.P
print field8.K

print field8
print field7
print field7.basicType
```

### Abstraction and Decompisition

Before going any further it is important to understand an important concept -- __Abstraction__.  In the above example, I created a new class called "Soil".  If you think about the dirt underneath you feet there are many aspects that are important with regard to soil -- the type of soil, nutrient levels, crop grown on it, slope, moisture level, color, texture, use, etc.  The variables themselves do not create actual soil, they are just important factors or measurements that we can evaluate for a given soil.  In this list, what we have created is an _abstraction_ of soil.  If we are trying to create a computer program to represent soil, we do not have to create every aspect of soil, just the variables we are interested in.  

I swipped this definition of abstraction from Google dictionary"

```
abstraction - the process of considering something independently of its associations, attributes, or concrete accompaniments.
```
The problem with the way I have defined abstraction is that is not quite how computer scientist think about it.  The end goal of abstraction is to create a black box program that hides detail so as not to confused the user.  Inputs go in and outputs come out, but how the process works is hidden from the user.  But in order to do this one has to consider what are the important aspects that need to go into the class.  For the "Soil" class, if the purpose is to model P and K fluxes in the soil, then microbial activity, the prill size of fertilizer used, or the tractor driven across the field are not going to be important, so it is better to leave those aspects out and only focus on details that matter.

In the abtraction process, comes __decomposition__ which is when we break down the program into independent parts that function separately from each other.  While we have defined _instance variables_ using the "__init__" method (they can be defined in other ways as well), method within a class or functions (using _def_) can create structure in the class and keep components separate.

Object oriented program is really brilliant.  It creates reusable code that is well defined and structured.  The bad part is that you really have to think ahead before jumping in and start writing code.  

### Defining Methods

Let's further expand the "Soil" class by defining methods.  One aspect we want to avoid is accessing the _instance variables_ directly, instead we want to create some definitions that avoid this.  

```python
class Soil(object):
	'''This is my soil class used to monitor important properties related to the soil health.
	'''
	def __init__(self, basicType, P, K):
		self.basicType = basicType
		self.P = P
		self.K = K

	def getPvalue(self)
		return self.P

	def getKvalue(self):
		return self.K

	def fertilize(self, Pfert, Kfert, amount):
		'''Increase the predicted amount of P and K in the soil based on the fertilizer applied.
		PFERT: float, percentage of P in fertilizer
		KFERT: float, percentage of K in fertilizer
		AMOUNT: float, lbs of fertilizer per acre
		'''
		self.P = self.P + int(Pfert * amount)
		self.K = self.K + int(Kfert + amount)

	def checkMinimum(self):
		'''Determine if soil is at minimum level for crop growth.  
		Minimum P: 120
		Mimimum K: 80
		'''
		if self.getPvalue() >= 120
			print "P levels are adequate.  Current level: " + str(self.getPvalue())
		else:
			print "P levels are low.  Current level: " + str(self.getPvalue())

		if self.getKvalue() >= 80
			print "K levels are adequate.  Current level: " + str(self.getKvalue())
		else:
			print "K levels are low.  Current level: " + str(self.getKvalue())

	def monthlyLoss(self, rainPerMo)
		'''Calculate the monthly loss based on rainfall.  Assume a 2 point loss for every inch of rain for K and a 0.25 point loss for every inch of rain for 
		'''
		self.K = self.getKvalue() - int(2 * rainPerMo)
		self.P = self.getPvalue() - int(0.25 * rainPerMo)
```

In the _soil_ class, three new methods have been added.  The first method, Soil.checkMimimum(), checks levels based on a mimimum value and returns a status based on the P and K levels.  Notice that there is no need to provide inputs to this method because it can access the instance variables because they already exist within the class.

The second two methods, fertilize() and monthlyloss() are going to modify the two instance varialbes, K and P, to increase or decrease based on new inputs from the user.  In the case of fertilize(), the amount of fertilizer along with the percentage of P and K in the fertilizer are provided.  

When you think about this class, it provides an ability to track two components in the soil and to adjust those levels based on new user inputs.  Instead of identifying every component that would need to be represented to create an authentic soil, the soil was abstracted to identify only the components needed.  After that decomposition was used to create methods that can exist as stand alone functions.  

### Problem #1

Let's create a different check minimum class function that evaluates the P and K class variable levels and outputs the based on a crop input.  Think about how we/you should do this.  There is more than one way to accomplish this goal.

##### Problem #2

To improve your understanding of how classes work, consider that you have the following lists of fertilizer and rainfall for the next 12 months.  Print the resulting P and K levels for each month.

```
fertilizer = [100, 0, 0, 100, 50, 0, 0, 0, 0, 0, 0, 0]

perK = [0.2, 0, 0, 0.2, 0.5, 0, 0, 0, 0, 0, 0, 0]

perP = [0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

rainfall = [0, 2, 4, 16, 14, 1, 2, 3, 4, 9, 5, 3]
```

### Understanding where we are going.

If you happened to buy the book "The Self-Taught Progammer", I highly recommend you read chapter _ on the differnt types of programming and what make object-oriented programming so different.  It is a great read and really explains what we have been building toward with "Classes"

But to really understand OOP and Classes, you need to create one on your own.  For the next problem you are going to create your own Class -- from scratch.  

##### Problem #3

Create a class for _students_ called the Student class.  Students will have an id, a set of homework grades, exam grades, and attendance.  

##### Additional Info:

The work that MITx puts online is some of the absolute best.  Really fabulous teachers and lecture information.  If you want more info on abstraction and decomposition I highly recommend this [lecture](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-4-decomposition-abstraction-and-functions/). 