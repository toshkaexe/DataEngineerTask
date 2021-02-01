import requests
import json
import pprint
import pandas as pd

from Utils import dataParser

if __name__ == '__main__':

    curfile = "file_" + "RUB" + ".csv"
    curday = "DAY == '" +"2020-01-02" +"'"
    data = pd.read_csv(curfile)
    df = pd.DataFrame(data)
    newdf = df.query(curday)
    print(newdf)
    print(newdf['CAD'].values[0])
