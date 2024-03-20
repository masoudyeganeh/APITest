# compare fapi keys with rest keys
def compareKeys(object):
    fapiKeys = list(dict.fromkeys(list(object.getFapiKeys())))
    restKeys = list(dict.fromkeys(list(object.getRestKeys())))
    if fapiKeys == restKeys:
        return
    else:
        return list(set(fapiKeys) - set(restKeys))


# compare fapi values with rest values
def compareValues(object):
    fapiValues = list(dict.fromkeys(list(object.getFapiVales())))
    restValues = list(dict.fromkeys(list(object.getRestVales())))
    if fapiValues == restValues:
        return
    else:
        return list(set(fapiValues) - set(restValues))
