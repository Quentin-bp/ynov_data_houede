import pandas as pd

datas_exo = pd.read_json("../assets/catalogue_exoplanet.json")
datas_nasa = pd.read_csv("../assets/exo_nasa.csv",sep=';')
dfJson = pd.DataFrame(datas_exo)
dfNasa = pd.DataFrame(datas_nasa)

print(dfNasa)
#print(dfNasa.to_string())

def convertDataToCSV(df):
    
    print(df)
    result = []
    for i in range(len(df)):
        if("radius" in df.loc[i].fields):
            result.append(df.loc[i])
    cleaned_df = pd.DataFrame(result)
    cleaned_df.to_json("./sample.json", orient="records", indent=4)
    print(cleaned_df)


#convertDataToCSV(dfJson)
