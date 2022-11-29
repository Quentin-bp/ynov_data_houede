import pandas as pd
import matplotlib.pyplot as plt
import json

import plotly.express as px

datas_exo = pd.read_json("./data.json")


dfJson = pd.DataFrame(datas_exo)

dfCsv = pd.read_csv('../assets/catalogue_exoplanet.csv',na_values = 'null', sep = ';')

# print(dfNasa.to_string())


def getRadiusClean(data):
    exoplanet = data[data['Radius'].notna()]
    return exoplanet
def getMassClean(data):
    exoplanet = data[data['Mass'].notna()]
    return exoplanet

def convertDataToJson(data):
    # json_string = json.dumps(result)
    data = cleanJson(data)
    df2 = pd.DataFrame.from_dict(data)
    df2.to_json("./data.json", orient='records', indent=4)


def cleanJson(data):
    result = []
    for i in range(len(data)):
        if ("radius" in data.loc[i].fields):
            obj = {
                "datasetid": data.loc[i].datasetid,
                "recordid": data.loc[i].recordid,
                "fields": data.loc[i].fields,
                "record_timestamp": data.loc[i].record_timestamp
            }
            result.append(obj)
    return result

def cleanCsv(data):
    result = []
    for i in range(len(data)):
        if ("distance" in data.loc[i]):
            result.append(data.loc[i])
    cleaned_df = pd.DataFrame(result)
    cleaned_df.to_csv("./nasa.csv")


data = getRadiusClean(dfCsv)
data = getMassClean(data)
print(data)

#data.sort_values('Radius', ascending=True, inplace=True)

data.sort_values('Mass', ascending=True, inplace=True)

#ax1 = data.plot.scatter(y="Radius",x="Discovery",yticks = range(0,1000,150))

#ax2 = data.plot.scatter(y="Mass",x="Discovery",yticks = range(0,1000,150))

ax3 = data.plot.scatter(x="Mass", y="Radius",yticks = range(0,1000,150),xticks = range(0,1000,150))
plt.show()
