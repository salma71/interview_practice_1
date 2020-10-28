'''
find the closest pair of points 


1. we need to use the Eucliedian distance between pairs
2. return this distance squared

add some test cases run python3 -m doctest closestSquaredDistance.py -v in the terminal

>>> closestSquaredDistance([0, 3, 15], [0,  3, 30])
225.0
'''
# Euclidean distance = sqrt(sum i to N(x1_i - x2_i)^2)
# the smaller the E.D, the closer is the pair - more similar
# calculate the EU distance btween two vectors
from math import pow
from math import dist
def closestSquaredDistance(x, y):
    return pow(dist(x, y), 2)





