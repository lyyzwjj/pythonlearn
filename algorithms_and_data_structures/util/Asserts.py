class Asserts:
    @classmethod
    def test(cls, value):
        try:
            if not value:
                raise Exception("测试未通过")
        except Exception as result:
            print("%s" % result)
