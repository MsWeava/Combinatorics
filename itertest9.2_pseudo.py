import itertools
import random

items = [1,2,3]
combinations = (combination for combination in itertools.combinations(items, 2))

#we need to draw the random numbers that will serve as indexes to be drawn from the generator.
def random_numbers(sample_size, limit):
  counter_random = sample_size
  random_set = []
  while True:
    index = random.randint(0, limit)
    if index not in random_set:
       random_set.append(index)
       counter_random -=1
       if counter_random ==0:
         break
  random_set.sort()
  return random_set
    
print(random_numbers(3,5))
    
  
'''    
    samples.append(next(generator))
    print(samples)

'''

'''
print(random_sample(combinations,2))

counter = 0
for number in combinations:
  print(number)
  counter += 1
  if counter == 10:
    break
    print(number)
'''