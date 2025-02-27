import plotly.express as px

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visualize the results in bar (it could be line or scattered)
title = "Results of Rolling One D6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of Result'}
fig = px.bar(poss_results, y=frequencies, title=title, labels=labels)
fig.show()
