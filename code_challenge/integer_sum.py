""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""
def integers_sum(n):
    '''
    generate integer series up to input num.
    get the sum of this series
    return 0 if the input isnot integer
    
    >>> integers_sum(4)
    10
    >>> integers_sum('')
    0
    '''
    try:
        result = sum(range(n + 1))
    except TypeError:
        result =  0
    return result