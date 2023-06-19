import itertools
import random

#this is the number of possible items - like...ben wants 60 here
last_num = 5

#below is a list of possible items:
items = list(range(1,last_num+1))

#this is the generator of combinations:
combinations = (combination for combination in itertools.combinations(items, 2))



#we need to draw the random numbers that will serve as indexes to draw samples from the generator
'''
    Sample_size - how many numbers we want to draw from the generator above - for ben it would be 24
    limit - the length of the generator - limit should be the length of the entire generator - might use numpy to get this number
'''

def random_numbers(sample_size, limit):
  counter_random = sample_size
  random_set = []   #I know this is not a set but whatever
  while True:
    index = random.randint(0, limit)
    if index not in random_set:
       random_set.append(index)
       counter_random -=1
       if counter_random ==0:
         break
  random_set.sort()
  return random_set

#test:
print(random_numbers(4,9))

#this is a function to get a certain index out of the generator:
def extract_combination(generator, index):
    for i, v in enumerate(generator):
        if i is index:
           return v
  
my_indexes = [1,3,4,8] #call the random_numbers here instead



my_counter = 0
for number in my_indexes:
   #reinitialize the generator so it does not loose items:
   combinations2 = (combination for combination in itertools.combinations(items, 2))
   print(extract_combination(combinations2,number))
   my_counter +=1
print(my_counter)


      
for number in combinations:
   print(number)
