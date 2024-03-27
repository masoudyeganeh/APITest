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
    fapiValues = []
    restValues = []
    for i in range(len(objectList)):
        fapiKeys.append(list(generalMethods.get_keys(objectList[i].fapiResponse)))
        restKeys.append(list(generalMethods.get_keys(objectList[i].restResponse)))
        fapiValues.append(list(generalMethods.get_values(objectList[i].fapiResponse)))
        restValues.append(list(generalMethods.get_values(objectList[i].restResponse)))
        # for key in fapiKeys[i]:
        #     if restKeys[i] == fapiKeys[i]:
        #         onlyRest.append("OK")
        #         onlyFapi.append("OK")

        if set(fapiKeys[i]) == set(restKeys[i]):
            onlyFapi.append("OK")
            onlyRest.append("OK")
            customerId.append(objectList[i].restParams["customerId"])
        else:
            # x = list(set(fapiKeys[i]) - set(restKeys[i])) + list(set(restKeys[i]) - set(fapiKeys[i]))
            x = 0
            for ele in list(set(restKeys[i]) - set(fapiKeys[i])):
                if restValues[i][restKeys[i].index(ele)] is None:
                    x = x + 1
            if x == len(list(set(restKeys[i]) - set(fapiKeys[i]))):
                onlyRest.append("OK")
            else:
                onlyRest.append(list(set(restKeys[i]) - set(fapiKeys[i])))
            onlyFapi.append(list(set(fapiKeys[i]) - set(restKeys[i])))
            customerId.append(objectList[i].restParams["customerId"])
    result = pd.DataFrame({'customerId': customerId, 'onlyFapi': onlyFapi, 'onlyRest': onlyRest})
    filename = 'compareKeys.xlsx'
    result.to_excel(filename)
    return result

