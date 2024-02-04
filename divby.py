def divby(n,d):
    """
    Returns True if the number n is divisible by the divisor d, otherwise returns False

    @params:
    n := number (int, float)
    d := divisor (int, float)
    """
    if n % d == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    assert divby(5,2) == False
    assert divby(5,2.5) == True
    assert divby(99.6, 100) == False
    assert divby(55,5) == True
    print("All tests passed!")
