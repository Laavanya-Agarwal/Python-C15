import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def mean():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    df = mean_list
    mean = statistics.mode(df)
    fig = ff.create_distplot([df], ["Math Score"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.15], mode="lines", name="Mean"))
    fig.show()

    population_mean = statistics.mean(data)
    print("Sampling mean: ", population_mean)
    
    population_sd = statistics.stdev(data)
    print("Sampling standard deviation: ", population_sd)
mean()