'''
A palindromic string is one which reads the same forwards and backwards, e.g., "redivider". 
In this problem, you are to write a program which determines if the decimal representation of an integer is a palindromic string. 
For example, your program should return true for the inputs 0, 1", 7, 17, 727, 333, a: nd21.4744741.2, 
and false for the inputs -'1, 12, 100, and 2147483647.

Write a Program that takes an integer and determines if that integer's representation as a decimal string is a palindrome.
'''

def palindrome_int(n):
    '''
    >>> palindrome_int(1)
    True
    
    >>> palindrome_int(727)
    True
    
    >>> palindrome_int(333)
    True
    
    >>> palindrome_int(100)
    False
     
    '''
    # using the method we did before
    # import reverse_digit 
    # while n > 0:
        # if n == reverse_digit.reverse_digit(n):
            # return 'true'
        # else:
            # return 'false'
    # return 'false'
    
    # using the log10 method
    # get # of digits in n by taking the (log n) + 1
    # leading = n mod 10 
    # tail = n/10^(n -1)
    # if leading == tail -> true 
    # iterate and remove lead, tail from inner number
    # else false
    # complexity O(n), space O(1)
    import math
    num_digit = math.floor(math.log10(n)) + 1
    tail = 10**(num_digit - 1)
    # for i in range(num_digit // 2):
    if n // tail != n % 10:
        return False
        # if they are equal -> go deeper
        # remove lead
    n //= 10
    # remove tail 
    n %= 10**(num_digit - 1)
    # decrement by two digits 
    tail //= 100
    return True
