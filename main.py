from API import customerInfoAPI, customerOrdersAPI
import testCase

customerInfoObjectList = customerInfoAPI.callCustomerInfoAPI()

customerInfoCompareKeysTestResult = testCase.compareKeys(customerInfoObjectList)

customerOrdersObjectList = customerOrdersAPI.callcustomerOrdersAPI()

customerOrdersCompareKeysTestResult = testCase.compareKeys(customerOrdersObjectList)
