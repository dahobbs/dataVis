import pygal
from die import Die

#create two dice
die1 = Die()
die2 = Die()

#make some rolls and store the results in a list

results=[]

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyise the results
frequencies =[]
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualise the results with pygal
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"

hist.x_labels =  list(range(2,13))
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('die_vis.svg')
