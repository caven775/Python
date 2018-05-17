# coding=utf-8
import json


#断言的用处: 断言一般用在调试的时候，当程序运行起来之后使用断言可以跟踪代码的执行情况
#断言的基本语法 assert (device_id), "device_id 不存在，停止继续执行"。
#语法说明 assert 后面第一个参数是指断言的条件，当条件满足时，程序会继续往下执行
#assert 后面第二个参数是当断言条件不满足时，执行的代码



class AssertTest(object):
    def __init__(self):
        super(AssertTest, self).__init__()

    def readFile(self):
        file_path = "financeAPIConfig.json"
        with open(file_path, "r", encoding="utf-8") as obj:
            return json.load(obj)

    #断言判断两者是否相等
    def assert_test_equal(self):
        file = self.readFile()
        url = file["baseURL"]

        try:
            assert (url == "https://finsuitdev.udomedia.com.cn"), "url 不相等，执行AssertionError"
        except AssertionError:
            self.assert_test_empty()
            print("断言生效，程序继续执行")







    #断言判断一个对象是否为空
    def assert_test_empty(self):
        file = self.readFile()
        device_id = file["device_id"]
        assert (device_id), "device_id 不存在，停止继续执行"
        print("符合断言的条件，继续执行，device_id == " + device_id)

    #断言判断大小
    def assert_test_size(self):
        a = 10;
        b = 20
        assert (a > b), "a 比 b 小"






exerciseTest = AssertTest()
exerciseTest.assert_test_equal()
# exerciseTest.assert_test_empty()
# exerciseTest.assert_test_size()

