import random

DRINKER = 1 
MAXIMUM_TURNS = 10000000

steps = 10

for turn in range(MAXIMUM_TURNS):
  step_forward = random.randint (1, 5)
  step_backwards = random.randint (2, 4)
  steps = steps + (step_forward - step_backwards)
  
  if steps > 20:
    print ("The Drinker has reached his house, and recovered.")
    break
  
  if steps < 1:
    print ("The Drinker has fallen off of a cliff")
    break
  print (steps)
