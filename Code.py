# libraries
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Create a dataset
df = pd.read_csv (r'Area.csv')
print (df)
# Create a grid : initialize it
g = sns.FacetGrid(df, col='Country', hue='Country', col_wrap=4, )
# Add the line over the area with the plot function
g = g.map(plt.plot, 'Years', 'Value')
# Fill the area with fill_between
g = g.map(plt.fill_between, 'Years', 'Value', alpha=0.2).set_titles("{col_name} Country")
# Control the title of each facet
g = g.set_titles("{col_name}")
# Add a title for the whole plo
plt.subplots_adjust(top=0.92)
g = g.fig.suptitle('Evolution of the value in eight countries')
plt.show()
