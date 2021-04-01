import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="tv",y="time")

        fig.show()

def getDataSource(data_path):
    time=[]
    tv=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            time.append(float(row["time"]))
            tv.append(float(row["tv"]))
    return {"x":tv,"y":time}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])

    print("correlation is: ",correlation[0,1])

def setup():
    data_path="tvVsTime.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    #plotFigure(data_path)
setup()