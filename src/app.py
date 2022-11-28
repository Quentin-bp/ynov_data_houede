import pandas as pd
import json

datas_exo = pd.read_json("./data.json")
# datas_exo = pd.read_json("../assets/catalogue_exoplanet.json")
datas_nasa = pd.read_csv("../assets/exo_nasa.csv", sep=';', names=['sy_dist'])
dfJson = pd.DataFrame(datas_exo)
dfNasa = pd.DataFrame(datas_nasa)

# print(dfNasa.to_string())


def convertDataToCSV(df):

    print(df)
    result = []
    for i in range(len(df)):
        print(df[i]["sy_dist"])


def convertDataToJson(data):
    # json_string = json.dumps(result)
    data = cleanJson(data)
    df2 = pd.DataFrame.from_dict(data)
    print(df2)
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
# print(json_object)
#cleaned_df = pd.DataFrame(result)
# cleaned_df.to_json("./data.json")
##       json_string = json.dumps(obj)
    # print(json_string)


def cleanCsv(data):
    result = []
    for i in range(len(data)):
        print(data.loc[i])
        if ("distance" in data.loc[i]):
            result.append(data.loc[i])
    cleaned_df = pd.DataFrame(result)
    cleaned_df.to_csv("./nasa.csv")


# print(cleanCsv(dfNasa))
# convertDataToCSV(dfJson)

convertDataToJson(dfJson)
