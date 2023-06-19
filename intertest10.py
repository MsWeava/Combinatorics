
import random

from itertools import chain
from collections import Counter

#this is the number of possible items - like...ben wants 60 here
last_num = 60

#below is a list of possible items:
items = list(range(1,last_num+1))


big_list = []
for number in range(1,24):
    sample = random.sample(items, 10)
    big_list.append(sample)

for items in big_list:
    print(items)

counts = Counter(chain.from_iterable(big_list))

print(counts)

    
