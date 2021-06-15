import random

DRINKER = 1 
MAXIMUM_TURNS = 10000000

steps = 10

for turn in range(MAXIMUM_TURNS):
  steps_back_and_forth = random.randint (-3, 3) 
  steps = steps + steps_back_and_forth
  
  if steps > 20:
    print ("The Drinker has reached his house, and recovered.")
    break
  
  if steps < 1:
    print ("The Drinker has fallen off of a cliff")
    break
  print (steps)
