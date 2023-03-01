import pyfpgrowth
from interface import *

def fpGrowth(x,y,z):
    patterns = pyfpgrowth.find_frequent_patterns(x, y)
    rules = pyfpgrowth.generate_association_rules(patterns, z)
    return rules


