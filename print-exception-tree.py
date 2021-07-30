# This is the Python Essentials 2 LAB 3.6.1.4 print exception tree
# It uses the recursive function print_exception_tree() to build a tree of exceptions.
# It uses the sorted () function with Key to sort the branches of the tree by name.
# It uses a lambda function to call the __name__ of the classes during sorting.
# It uses some simple code to remove duplicates from exceptions list

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

##    # Code V1
##    final_list = []
##    name_list = []
##    for subclass in subclasses:
##        name_to_append = subclass.__name__
##        if name_to_append not in name_list:
##            name_list.append(name_to_append)
##            final_list.append(subclass)
##    subclasses = final_list

    # This is version 2 of code to remove duplicates from subclasses list
    # The list of subclasses is sorted, so we can simply compare names of two adjacent items
    final_list = []                             # Initiate a new list to store unique subclasses
    prev_subclass_name = ""                      # Initiate a variable to keep the previous name
    for subclass in subclasses:                   # Loop through the list of subclasses
        if subclass.__name__ != prev_subclass_name:# If two adjacent entries have diff. names
            final_list.append(subclass)            # Store current subclass in final_list
        prev_subclass_name = subclass.__name__     # And remember name of current subclass
    subclasses = final_list                        # After all, we got a list of unique subclasses

    # These are recursive tree-drawing calls for each subclass
    for subclass in subclasses:
        print_exception_tree(subclass, nest + 1)


# Main
if __name__ == "__main__":
    print_exception_tree(BaseException)
