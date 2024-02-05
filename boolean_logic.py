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
    if x == y == z:
        return 1
    return 0

def boolean_exercise_3(a,b,c,d):
    """
    Create a boolean function using AND, OR, and NOT logic that implements
    the function of four variables that is 1 if precisely two of the
    variables have the same value, 0 otherwise.

    A set() based implementation
    if len(set((a,b,c,d))) == len(tuple((a,b,c,d)))-1:
        return 1
    return 0
    """
    if a == b or a == c or a == d or b == c or b == d or c == d:
        return 1
    return 0

def boolean_exercise_4(k,j,i):
    """
    Create a boolean function using AND, OR, and NOT gates that implements
    the function of three variables that is 0 if all three inputs are
    the same, and 1 otherwise.

    A weird reuse of function 3:
    return int( not bool(boolean_exercise_2(k,j,i)))
    """
    if k == j == i:
        return 0
    return 1


def fuzzy_bool(f, cutoff=0.5):
    """
    The function accepts a float f and return True if it greater more than 0.5, otherwise return False.
    """
    if f > cutoff:
        return True
    return False


print(boolean_exercise_3(55,23,45,23) == 1)
print(boolean_exercise_3(55,23,23,45) == 1)
print(boolean_exercise_3(23,66,45,23) == 1)
print(boolean_exercise_3(55,23,45,88) == 0)

print(boolean_exercise_3(23,23,45,23) == 0)
