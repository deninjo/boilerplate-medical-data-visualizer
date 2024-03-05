import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = (df['weight']/((df['height']/100)**2)).round(1)
df['overweight'] = (df['BMI'] > 25).astype(int) # This converts the boolean values to integers 1 for True and vice versa

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# Replace 0 with 'good' and 1 with 'bad'
df[['active','smoke','alco','cardio','overweight']] = df[['active','smoke','alco','cardio','overweight']].replace({0: 'good', 1: 'bad'})
# If value of cholesterol/gluc=1, make the value 0. If value > 1, make the value 1.
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].applymap(lambda x: 1 if x > 1 else 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars="cardio", value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["variable", "value", "cardio"])["value"].count()
    df_cat = pd.DataFrame(df_cat).rename(columns={"value": "total"}).reset_index()
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x = "variable", y = "total", hue = "value", kind = "bar",col = "cardio", data = df_categorical) 


    # Get the figure for the output
    fig = sns.catplot(x = "variable", y = "total", hue = "value", kind = "bar",col = "cardio", data = df_categorical) 


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
