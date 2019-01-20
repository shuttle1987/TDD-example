def multiply_two(first, second):
    """Multiply the two arguments together"""
    if isinstance(first, str) or isinstance(second, str):
        raise TypeError("Strings are not allowed")
    return first * second
