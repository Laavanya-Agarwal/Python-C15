import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv('School3.csv')
data = df['Math_score'].tolist()

fig = ff.create_distplot([data], ['Math Score'], show_hist = False)
fig.show()

mean = statistics.mean(data)
print('Mean: ' + mean)
sd = statistics.stdev(data)
print('Mean: ' + sd)