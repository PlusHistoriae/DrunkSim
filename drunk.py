import matplotlib.pyplot as plt
import random

MAXIMUM_TURNS = 10000000

steps = 10

data = []

for turn in range(MAXIMUM_TURNS):
  steps_back_and_forth = random.randint (-4, 3) 
  steps = steps + steps_back_and_forth
  data.append(steps)
  
  if steps > 20:
    print ("Turn:" + str(turn))
    print ("The Drinker has reached his house, and recovered.")
    break
  
  if steps < 1:
    print ("Turn:" + str(turn)) 
    print ("The Drinker has fallen off of a cliff")
    break

plt.plot(data)
plt.show()
