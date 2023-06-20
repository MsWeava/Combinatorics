
import random

from itertools import chain
from collections import Counter
import numpy as np

#this is the number of possible items (60 in this case)
last_num = 60

#this is how many integers will be in each group
num_per_line = 10

#How many samples you would like:
sample_number = 24

#below is a list of possible items:
items = list(range(1,last_num+1))

'''
In the function below:

last_num = int - all numbers - could do with just the list, but im specially lazy today
items = list of last_num
primary_dict = dict of weights ordered by value (lowest to highest)
'''

def create_weights(last_num,items,primary_dict):
  #get first key (the lowest). It will have highest weight on the next draw:
  lowest_freq = list(primary_dict)[0]

  #get last key (highest). Will not appear in the next sequence:
  highest_freq = list(primary_dict)[-1]
  
  counter = 0                        #get rid of counter eventually, don't need it
  weights = []
  for number in items:
    counter += 1
    if number == lowest_freq:
      weight= .5
      weights.append(weight)
    elif number == highest_freq:
      weight=0
      weights.append(weight)
    else:
      weight = .5/ (last_num-2)
      weights.append(weight)
  return weights



#get 24 samples of numbers 1-60 with 10 cases in each sample
big_list = []
for number in range(1,sample_number):
    if len(big_list) >1:
        #check the frequency of each number once we have two samples in:
        counts = dict(Counter(chain.from_iterable(big_list)))
        #sort the dict by value:
        sorted_counts = dict(sorted(counts.items(), key=lambda x:x[1]))
        
        #get first key (the lowest). It will have highest weight on the next draw:
        lowest_freq = list(sorted_counts)[0]

        #get last key (highest). Will not appear in the next sequence:
        highest_freq = list(sorted_counts)[-1]
        
        #create weights for frequencies so far
        my_weights = create_weights(last_num,items,sorted_counts)
        
        #create new balanced sample and add to big list:
        my_sample = np.random.choice(items,size=num_per_line,replace=False, p=my_weights)
        big_list.append(my_sample)

        #print(lowest_freq, highest_freq)
        #print(sorted_counts)
        #print(my_weights)
        #print(len(my_weights))
        #print(my_weights[42])
    #first two samples are drawn randomly without weights
    else:
        sample = random.sample(items, num_per_line)
        big_list.append(sample)
    
    #get all frequencies of the overal sample so that we can check it out:
    counts = Counter(chain.from_iterable(big_list))

for items in big_list:
    print(items)


#get all frequencies for future balancing:
counts = Counter(chain.from_iterable(big_list))

sorted_counts = dict(sorted(counts.items(), key=lambda x:x[1]))
#print(counts)
print(sorted_counts)
print(len(sorted_counts))
#print('lengh items:' + str(len(items)))
items_to_print = list(range(1,last_num+1))
print(len(items_to_print))    
