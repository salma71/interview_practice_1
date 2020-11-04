def reverse_digit(n):
    '''
    takes an integer and return the integer corresponding to the digits of the input written in reserse order
        
    >>> reverse_digit(-42)
    -24

    >>> reverse_digit(1132)
    2311
    '''
## use the % mode to get the last digit 2
## put 2 in the front
## use // to get the remainder 113
## iterate over the remainder and repeat with the %
## return the reversed number
## generally, if k >= 0 k mode 10, subsequent is the reverse of k/10
## O(n) where n is the number of digits in k


    result, n_remaining = 0, abs(n)
    while n_remaining:
        result = result * 10 + n_remaining % 10
        n_remaining //= 10
    return -result if n < 0 else result






    
