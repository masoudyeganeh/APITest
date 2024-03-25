import customerInfoAPI
import testCase

# customerInfo = customerInfoAPI.makeCustomerInfo()
customerInfoObjectList = customerInfoAPI.callCustomerInfoAPI()

compareKeysTestResult = testCase.compareKeys(customerInfoObjectList)

print(compareKeysTestResult)