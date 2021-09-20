def greeting(name: str):                ##Print to command line only reallly helpful for referencing things
    print(f"Hello {name}")              ##Specifying name as str in the arguments will allow for type hinting
                                        ## (IE will tell you what variable type is needed)


def addition(int1=0, int2=0) -> int:    ##Return statements tend to be more useful in these instances
    return int1 + int2                  ##Setting int1 and int2 = to 0 defaults them - ie the value if
                                        ##if one of the arguments are missing
                                        ##The little arrow to int will typehint the output of the function

def many_args(*multiargs):              ##The * at the start of multiargs allows for "unlimited" arguments to be passed
    print(type(multiargs))
    total = 0
    for arg in multiargs:
        total += arg
    return total


#Good practices for functions:
#   Clearly state what it does
#   Name everything in lower case
#   All args clear in what they need, and include expected type
#   Keep them as small as possible where feasible - keeps it easier to test and better for OOP
#       Longer functions are less likely to be reused, but building lots of tiny functions takes time
#       BUT long term it is 100% worth it
#   Keep comments on the function for others and yourself