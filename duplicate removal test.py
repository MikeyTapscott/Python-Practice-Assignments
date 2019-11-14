# Python code to remove duplicate elements 
from collections import OrderedDict
def Remove(duplicate): 
    return list(OrderedDict.fromkeys(duplicate))
      
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate))