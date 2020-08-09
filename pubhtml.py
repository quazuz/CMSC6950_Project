from htmldate import find_date
import pandas as pd
import numpy as np 
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

import csv
df = pd.read_csv("dates.csv")
np_url = df['url'].values.tolist()
#print(df)
print(np_url)

dates = []
for url in np_url:
    date = find_date(url)
    dates.append(date)
    #print(date)
    for date in dates:
        print(date)

column = widgets.Dropdown(options=list(df['url']),description='Web Link')
ui = widgets.HBox([column])
def print_date(column):
    date = find_date(column)
    print(date)

out = widgets.interactive_output(print_date, {'column': column})

display(ui, out)

# df.to_csv('dates.csv')   
import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(dates, np_url)

ax.set(ylabel='URL', xlabel='Dates',
       title='PLOT SHOWING PUBLICATION DATES OF DIFFERENT WEB ARTICLES')
ax.grid()

fig.savefig("test.png")
plt.show()