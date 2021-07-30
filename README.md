# Python-Essentials-LAB-3.6.1.4-print-exception-tree

This program dumps all predefined exception classes in the form of a tree-like printout.

As a tree is a perfect example of a recursive data structure, a recursion seems to be the best tool to traverse through it. The print_exception_tree() function takes two arguments:

•	a point inside the tree from which we start traversing the tree;

•	a nesting level (we'll use it to build a simplified drawing of the tree's branches)

Let's start from the tree's root - the root of Python's exception classes is the BaseException class (it's a superclass of all other exceptions).

For each of the encountered classes, perform the same set of operations:

•	print its name, taken from the __name__ property;

•	iterate through the list of subclasses delivered by the __subclasses__() method, and recursively invoke the print_exception_tree() function, incrementing the nesting level respectively.

Note how we've drawn the branches and forks. The printout isn't sorted in any way - you can try to sort it yourself, if you want a challenge. 

**Challenge accepted. Complete code includes:**
```
def print_exception_tree(thisclass, nest = 0):
    # It is a decoration for the visual representation of a tree.
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    # This is the sort of subclasses
    subclasses = thisclass.__subclasses__()              # Get list of subclasses
    subclasses = sorted(subclasses,                      # Use sorted() with Key
               key = lambda subclass: subclass.__name__) # Use lambda to call names of classes

    # These are recursive tree-drawing calls for each subclass
    for subclass in subclasses:
        print_exception_tree(subclass, nest + 1)
```
