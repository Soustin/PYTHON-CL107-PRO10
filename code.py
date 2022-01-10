import csv
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('attempts-level.csv')
size = pd.read_csv('size.csv')
# attempt = df["attempt"]

mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
print(mean)

# bFig=go.Figure(go.Bar(e 
#     x = mean,
#     y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
#     orientation = 'h'
# ))

# bFig.show()

scFig = px.scatter(df,x = "student_id", y = "level", size = size, color = "attempt")
scFig.show()

# I will not be needing anything after this

# def plotFigure(data_path):
#     with open(data_path) as csv_file:
#         df = csv.DictReader(csv_file)
#         fig = px.scatter(df,x="levels", y="attempts")
#         fig.show()

# def getDataSource(data_path):
#     level = []
#     attempt = []
#     with open(data_path) as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             level.append(float(row["level"]))
#             attempt.append(float(row["attempt"]))

#     return {"x" : level, "y": attempt}

# def findCorrelation(datasource):
#     correlation = np.corrcoef(datasource["x"], datasource["y"])
#     print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

# def setup():
#     data_path  = mean

#     datasource = getDataSource(data_path)
#     findCorrelation(datasource)
#     plotFigure(data_path)

# setup()