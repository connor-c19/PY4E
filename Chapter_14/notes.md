# Object Oriented Programming Basics

- Programs are made up of lots of objects, instead of having a sequential program that takes in input, processes, and outputs data, objects are made that have sovereignty over their own data/properties, and communicate with other objects.

- The key aspect of OOP is to break a problem into smaller understandable parts, and each part forms a loose collective that solves the problem.

- Objects also offer a layer of abstraction, users don't have to worry about the implementation.

- Definitions

  - **Class**: template of an object. Ex: Dog
  - **Method** or Message: Defined capability, function that lives inside of class. Ex: bark()
  - **Field** or Attribute: a bit of data in a class. Ex: name
  - **Object** or Instance: a particular instance of a class. Ex: Chili

- Sample code:

```
class PartyAnimal:
  def __init(self)__:
    self.x = 0
  def party(self) :
    self.x = self.x + 1
    print("So far",self.x)

an = PartyAnimal()
an.party()
# or
PartyAnimal.party(an)

```

- **init(self)** is a **constructor** method, or one that initializes a given instance of an object and associates it with a variable.

- `dir()` function lists capabilities of an object

  - `__xx__` methods are usually reserved as internal methods used by Python

- `type()` function reveals what template, or class an object instance belongs to

# Object Lifecycle

- Objects are created, used, and discarded.

- Constructor: Code called upon instance creation, set up any initial values of instance variables when a new instance is created.

  - Again, denoted with `def __init__(self)`

  - Can be set up with additional parameters: `def __init__(self, name)`

- Destructor: Called on object destruction, any instructions to be run at the deletion of an object.

  - This is denoted with `def __del__(self)`

  - Reassigning the object variable to an arbritrary value can trigger this functionality since the interpreter is throwing away the previous assignment of the variable.

# Inheritance

- Extending, or sub-classing, an existing class. A form of store and reuse

- This leads to parent-child relationship, where a class inherits all of the functionality of a given class but adds some functionality in a new class.

- This is done by passing the parent class as a parameter:

```
class Child(Parent):
  def __init__(self, name):
    # utilizes the constructor from the parent class
    super().__init__(name)
```
