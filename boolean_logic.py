def boolean_exercise_1(x,y):
    """
    Give a Boolean formula using only AND, OR, and NOT for the function
    of two Boolean variables x and y that is true if and only if x == y.
    Give the corresponding truth table
    T and T = T
    F and F = T
    F and T = F
    T and F = F
    """
    if x == y:
        return True
    return False


def boolean_exercise_2(x,y,z):
    """
    Create a boolean function using AND, OR, and NOT gates that implements
    the function of three variables that is 1 if all three inputs are
    the same, and 0 otherwise.

    """
    pass

def boolean_exercise_3(a,b,c,d):
    """
    Create a boolean function using AND, OR, and NOT gates that implements
    the function of four variables that is 1 if precisely two of the
    variables have the same value, 0 otherwise.
    """
    pass

def boolean_exercise_4(k,j,i):
    """
    Create a boolean function using AND, OR, and NOT gates that implements
    the function of three variables that is 0 if all three inputs are
    the same, and 1 otherwise.
    """
    pass

def fuzzy_bool(f, cutoff=0.5):
    """
    The function accepts a float f and return True if it greater more than 0.5, otherwise return False.
    """
    if f > cutoff:
        return True
    return False


print(boolean_exercise_1(True, True) == True)
print(boolean_exercise_1(False, False) == True)
print(boolean_exercise_1(True, False) == False)
