import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Coffee",y="sleep")

        fig.show()

def getDataSource(data_path):
    sleep=[]
    coffee=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row["sleep"]))
            coffee.append(float(row["Coffee"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])

    print("correlation is: ",correlation[0,1])

def setup():
    data_path="coffeeVsSleep.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    #plotFigure(data_path)
setup()