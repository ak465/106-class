import plotly.express as px
import csv
import numpy as np


with open("StudentMarksVSDays.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()

def getDataSouce(data_path):
    marks_of_Student = []
    DaysPresent = []


    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
             marks_of_Student.append(float(row["Marks In Percentage"]))
             DaysPresent.append(float(row["Days Present"]))
       
           
    return {"x":marks_of_Student,"y":DaysPresent}

def findCorrelation(datasource):
   correlation=np.corrcoef(datasource["x"],datasource["y"])
   print("correalation between Marks of Student and Days Present is : ",correlation[0,1])

def setup():
     data_path="StudentMarksVSDays.csv"
     datasource=getDataSouce(data_path)
     findCorrelation(datasource)

setup()