import plotly.graph_objects as go
from plotly import offline

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
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualizing results
x_values = list(range(1,die.num_sides+1))
data = [ go.Bar(x=x_values, y = frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title' : 'Frequency of Result'}
my_layout = go.Layout(title = 'Results of rolling one D6 1000 times',
                      xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename = 'd6.html')