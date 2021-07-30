# This is the Python Essentials 2 LAB 3.6.1.4 print exception tree
# It uses the recursive function print_exception_tree() to build a tree of exceptions.
# It uses the sorted () function with Key to sort the branches of the tree by name.
# It uses a lambda function to call the __name__ of the classes during sorting.

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

    # This is to remove duplicates


    # These are recursive tree-drawing calls for each subclass
    for subclass in subclasses:
        print_exception_tree(subclass, nest + 1)





# Main
if __name__ == "__main__":
    print_exception_tree(BaseException)
