import requests
import generalMethods
import applicationConfig as appConf


class CustomerOrders(generalMethods.Service):
    def __init__(self):
        super().__init__()
        self.name = "customerOrders"
        self.fapiUrl = "customers/orders"
        self.restUrl = "customers/orders"
        self.fapiHeader = ""
        self.restHeader = ""
        self.fapiParams = ""
        self.restParams = ""
        self.jsonBody = ""
        self.fapiResponse = ""
        self.restResponse = ""

    def setFapiParams(self, df, n):
        self.fapiParams = {}

    def setFapiHeader(self, df, n):
        self.fapiHeader = {"x-fixed-token": appConf.fapiFixToken,
                           "X-CUSTOMER-ID": str(df["customerId"][n]), "x-ds-code": appConf.dsCode}

    def setRestParams(self, df, n):
        self.restParams = {"customerId": str(df["customerId"][n]), "dsCode": appConf.dsCode}


def makecustomerOrders():
    customerOrders = CustomerOrders()
    return customerOrders


def callcustomerOrdersAPI():
    df = generalMethods.getTestData()
    n = -1
    customerOrdersObjectList = []
    for i in df["customerId"]:
        n = n + 1
        customerOrders = makecustomerOrders()
        customerOrders.setFapiParams(df, n)
        customerOrders.setFapiHeader(df, n)
        customerOrders.setRestParams(df, n)
        fapiResponse = requests.get(customerOrders.getFapiUrl(),
                                    headers=customerOrders.getFapiHeaders(), params=customerOrders.getFapiParams())

        restResponse = requests.get(customerOrders.getRestUrl(),
                                    headers=customerOrders.getRestHeaders(), params=customerOrders.getRestParams())
        customerOrders.setFapiResponse(fapiResponse.json())
        customerOrders.setRestResponse(restResponse.json())
        customerOrdersObjectList.append(customerOrders)
    return customerOrdersObjectList

