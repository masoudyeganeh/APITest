import generalMethods
import pandas as pd

df = pd.read_csv("mytestdata.csv")

print(df["customerId"])


def compareKeys(objectList):
    resultList = []
    onlyFapi = []
    onlyRest = []
    customerId = []
    fapiKeys = []
    restKeys = []
    for i in range(len(objectList)):
        fapiKeys.append(list(generalMethods.get_keys(objectList[i].fapiResponse)))
        restKeys.append(list(generalMethods.get_keys(objectList[i].restResponse)))
        if set(fapiKeys[i]) == set(restKeys[i]):
            onlyFapi.append("OK")
            onlyRest.append("OK")
            customerId.append(objectList[i].restParams["customerId"])
        else:
            # x = list(set(fapiKeys[i]) - set(restKeys[i])) + list(set(restKeys[i]) - set(fapiKeys[i]))
            onlyFapi.append(list(set(fapiKeys[i]) - set(restKeys[i])))
            onlyRest.append(list(set(restKeys[i]) - set(fapiKeys[i])))
            customerId.append(objectList[i].restParams["customerId"])
    result = pd.DataFrame({'customerId': customerId, 'onlyFapi': onlyFapi, 'onlyRest': onlyRest})
    filename = 'compareKeys.xlsx'
    result.to_excel(filename)
    return result

