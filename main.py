import customerInfoAPI
import testCase

customerInfo = customerInfoAPI.makeCustomerInfo()
customerInfoAPI.callCustomerInfoAPI()

compareKeysTestResult = testCase.compareKeys(customerInfo)
compareValuesTestResult = testCase.compareValues(customerInfo)