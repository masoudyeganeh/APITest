import customerInfoAPI
import testCase

customerInfoObjectList = customerInfoAPI.callCustomerInfoAPI()

compareKeysTestResult = testCase.compareKeys(customerInfoObjectList)

print(compareKeysTestResult)


