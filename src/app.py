import pandas as pd
import matplotlib.pyplot as plt
import json

datas_exo = pd.read_json("./data.json")


dfJson = pd.DataFrame(datas_exo)

dfCsv = pd.read_csv('../assets/catalogue_exoplanet.csv',na_values = 'null', sep = ';')

# print(dfNasa.to_string())


def getRadiusClean(data):
    exoplanet = data[data['Radius'].notna()]
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



# convertDataToCSV(dfJson)

#convertDataToJson(dfJson)

#clean_json_data = cleanJson(dfJson)
#clean_json_data = pd.DataFrame(clean_json_data)
#cleanDf = pd.read_csv("../assets/exo_nasa.csv", sep=';', names=['sy_dist']) pd.read_json("./catalogue_exoplnet.xlsx")
#radiuses = pd.json_normalize(clean_json_data, record_path=['fields'], meta=['radius'])

#radiuses = pd.json_normalize(clean_json_data, record_path=["fields"],meta=["radius"])

#print(clean_json_data)

data = getRadiusClean(dfCsv)
data.sort_values('Radius', ascending=True, inplace=True)
ax1 = data.plot.scatter(y="Radius",x="Discovery",yticks = range(0,1000,150))

plt.show()