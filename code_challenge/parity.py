
# The parity of a binary word is 1 if the number of 1s in the word is odd
# otherwise, it is 0. 
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0. 
# Parity checks are used to detect single bit errors in data storage and communication. 
# It is fairly straightforward to write code that computes the parity of a single 64-bit word.
# How would you compute the parity of a very large number of 64-bit words?
# Hint: use a lookup table, but don't use 264 entries!

def parity(x):
    '''
    >>> parity(1011)
    1
    '''
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res
    
    
    
    
    
    




    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
