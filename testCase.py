import generalMethods
import pandas as pd

df = pd.read_csv("mytestdata.csv")

print(df["customerId"])


def compareKeys(objectList):
    resultList = []
    customerId = []
    fapiKeys = []
    restKeys = []
    for i in range(len(objectList)):
        fapiKeys.append(list(dict.fromkeys(list(objectList[i].fapiResponse))))
        restKeys.append(list(dict.fromkeys(list(objectList[i].restResponse))))
        if set(fapiKeys[i]) == set(restKeys[i]):
            resultList.append("OK")
        else:
            x = list(set(fapiKeys[i]) - set(restKeys[i]))
            resultList.append(x)
            customerId.append(objectList[i].restParams["customerId"])
    # result = pd.DataFrame({'customerId': {0: [customerId]}, 'keysdiff': {0: [resultList]}})
    result = pd.DataFrame(list(zip(customerId, resultList)))
    filename = 'compareKeys.xlsx'
    result.to_excel(filename)
    return result

# def compareValues(objectList):
#     resultList = []
#     customerId = []
#     fapiValues = []
#     restValues = []
#     for i in range(len(objectList)):
#         fapiValues.append(list(dict.fromkeys(list(objectList[i].fapiResponse))))
#         restValues.append(list(dict.fromkeys(list(objectList[i].restResponse))))
#         if set(fapiValues[i]) == set(restValues[i]):
#             resultList.append("OK")
#         else:
#             x = list(set(fapiValues[i]) - set(restValues[i]))
#             resultList.append(x)
#             customerId.append(objectList[i].restParams["customerId"])
#     # result = pd.DataFrame({'customerId': {0: [customerId]}, 'keysdiff': {0: [resultList]}})
#     result = pd.DataFrame(list(zip(customerId, resultList)))
#     filename = 'compareValues.xlsx'
#     result.to_excel(filename)
#     return result
