import plotly.express as px

from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visualize the results in bar (it could be line or scattered)
title = "Results of Rolling two D6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of Result'}
fig = px.bar(poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()
