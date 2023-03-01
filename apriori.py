from efficient_apriori import apriori
from interface import *


def apr(x,y,z):
    itemsets, rules = apriori(x, min_support=y, min_confidence=z, output_transaction_ids=True)
    return rules

