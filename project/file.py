import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ['reading_time'], show_hist = False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def mean():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    df = mean_list
    mean = statistics.mode(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

mean()
population_mean = statistics.mean(data)
print("Population mean: ", population_mean )
mean = statistics.mean(mean_list)
print("Sampling mean: ", mean)

population_sd = statistics.stdev(data)
print("Population SD: ", population_sd )
sd = statistics.stdev(mean_list)
print("Sampling SD: ", sd)

# finding the z score
z_score = (population_mean - mean)/sd
print("The z score is = ", z_score)