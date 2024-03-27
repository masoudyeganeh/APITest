import generalMethods
import pandas as pd
from deepdiff import DeepDiff

df = pd.read_csv("mytestdata.csv")

print(df["customerId"])


def compareKeys(objectList):
    resultList = []
    onlyFapi = []
    onlyRest = []
    valuesChanged = []
    customerId = []
    fapiKeys = []
    restKeys = []
    for i in range(len(objectList)):
        ddif = DeepDiff(objectList[i].fapiResponse, objectList[i].restResponse, ignore_order=True)
        customerId.append(objectList[i].restParams["customerId"])
        if "dictionary_item_added" in ddif:
            onlyFapi.append(ddif["dictionary_item_added"].items)
        else:
            onlyFapi.append("OK")
        if "dictionary_item_removed" in ddif:
            onlyRest.append(ddif["dictionary_item_removed"].items)
        else:
            onlyRest.append("OK")
        if "values_changed" in ddif:
            valuesChanged.append(ddif["values_changed"])
        else:
            valuesChanged.append("OK")
    result = pd.DataFrame({'customerId': customerId, 'onlyFapi': onlyFapi, 'onlyRest': onlyRest, 'valuesChanged': valuesChanged})
    filename = 'compareKeys.xlsx'
    result.to_excel(filename)
    return result

