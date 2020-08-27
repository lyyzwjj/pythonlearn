from utils.myjson.JsonUtil import *
from utils.excel.ExcelUtil import ExcelUtil, ColumnKey


class Json5Base():
    def __init__(self, type, description):
        self.type = type
        self.description = description


class Json5Mock:
    def __init__(self, mock):
        self.mock = mock


class Json5Field(Json5Base):
    def __init__(self, type, description, mock):
        super().__init__(type, description)
        self.mock = Json5Mock(mock)


class Json5Object(Json5Base):
    def __init__(self, description, properties, required):
        super().__init__("object", description)
        self.properties = properties
        self.required = required


class Json5Array(Json5Base):
    def __init__(self, description, items):
        super().__init__("array", description)
        self.items = items


def json_2_json5(base_str, data_str, column_dict):
    base_str = base_str.replace("{", "{{").replace("}", "}}").replace("#===#", "{}")
    data = json_str2obj(data_str)
    data = data2json5(data, column_dict)
    data_format = obj2json_str(data, MyEncoder)[1:-1]
    return base_str.format(data_format)


def get_column_dict(excel_name):
    eu = ExcelUtil()
    column_keys = []
    # column_key1 = ColumnKey("no", 0, "序号")
    column_key1 = ColumnKey("field", 1, "字段")
    column_key2 = ColumnKey("desc", 2, "描述")
    column_key3 = ColumnKey("type", 3, "类型")
    column_key4 = ColumnKey("isNeed", 4, "是否必须")
    column_key5 = ColumnKey("remark", 5, "备注")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    column_keys.append(column_key3)
    column_keys.append(column_key4)
    column_keys.append(column_key5)
    list = eu.excel_file2list(column_keys, "../../../resources/excel/interfaces/" + excel_name + ".xlsx")
    column_dict = {}
    for value in list:
        print(value)
        column_dict[value['field']] = value
    return column_dict


def filter_keys(keys, column_dict):
    new_keys = []
    for key in keys:
        try:
            excel = column_dict[key]
            isNeed = excel['isNeed']
            if "是" == isNeed.strip():
                new_keys.append(key)
        except Exception as e:
            print(column_dict)
            print(key)
            raise e
    return new_keys


def data2json5(data, column_dict, obj_flag=False):
    for item in data.keys():
        value = data[item]
        excel = column_dict[item]
        remark = excel['remark']
        desc = excel['desc']
        dr = desc if remark is None or remark.strip() == '' else desc
        if isinstance(value, str):
            data[item] = Json5Field("string", dr, value)
        elif isinstance(value, bool):
            data[item] = Json5Field("boolean", dr, value)
        elif isinstance(value, int):
            data[item] = Json5Field("integer", dr, value)
        elif isinstance(value, float):
            data[item] = Json5Field("number", dr, value)
        elif isinstance(value, (list, tuple)):
            if len(value) > 0:
                data[item] = Json5Array(dr, data2json5(value[0], column_dict, True))
            else:
                pass
        else:
            required = filter_keys(value.keys(), column_dict)
            properties = data2json5(value, column_dict)
            data[item] = Json5Object(dr, properties, required)
    if obj_flag:
        required = filter_keys(data.keys(), column_dict)
        return Json5Object("", data, required)
    else:
        return data


class Interface:
    def __init__(self, excel_name, data_str, base_str=None):
        self.excel_name = excel_name
        self.data_str = data_str
        self.base_str = base_str


def main2(interface):
    base_str = '{"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"appId":{"type":"string","description":"appId，接口接入的appId","mock":{"mock":"10001"}},"timestamp":{"type":"string","description":"时间戳，校验60秒内时延； 格式精确到秒 举例：new Date().getTime()/1000","mock":{"mock":"1554262690"}},"sign":{"type":"string","description":"加密串，加密后的字符串，加密规则如下： Md5(appId+appSecret+timestamp+data)， 加密后转换大写 注： 1，appSecret为分配密钥 2，data为data对象的json字符串","mock":{"mock":"xxxxxx"}},#===#},"required":["appId","timestamp","sign","data"]}'
    excel_name = interface.excel_name
    data_str_format = '{{"data":{}}}'
    data_str = data_str_format.format(interface.data_str)
    print(data_str)
    if interface.base_str is not None:
        base_str = interface.base_str
    column_dict = get_column_dict(excel_name)
    format = json_2_json5(base_str, data_str, column_dict)
    print("%s的json5是:  %s" % (excel_name, format))
    #
    # # data_str = '{"memberId":"xxx","productName":"xxx","storeId":"xxx","numOfPoint":"xxx","typeCode":"xxx","txnChannel":"Web"}'
    # # data_str = '{"memberId":"11047554920","posId":"104","transId":"2","storeNo":"106","orderNo":"2001190106104000002","businessDate":"2020/01/31","accounts":[{"accId":1000,"earnValue":2,"rdmValue":0},{"accId":1111,"earnValue":2,"rdmValue":0}]}'
    #
    # data_str = '{"memberId":"11047554920","posId":"104","transId":"2","storeNo":"106","orderNo":"2001190106104000002","businessDate":"2020/01/31","accounts":[{"accId":1000,"earnValue":2,"rdmValue":0},{"accId":1111,"earnValue":2,"rdmValue":0}]}'
    # data_str = data_str_format.format(data_str)
    # excel_name = "serialize"
    # column_dict = get_column_dict(excel_name)
    # format = json_2_json5(base_str, data_str, column_dict)
    # print(format)


if __name__ == '__main__':
    interfaces_arr = []
    # interfaces_arr.append(["3.4.1.queryPoint",
    #                        '{"memberNumber":"11007861119","pointFlag":"1000"}'])
    # interfaces_arr.append(["3.4.2.adjustment",
    #                        '{"typeCode":"Redemption","memberNumber":11000000004,"txnChannel":"Web","subTypeCode":"Manual Debit","storeId":"1","posID":"4","transID":"40","businessDate":"2019-12-23 12:00:00","productName":"PointAdjustment_MKT_Test","comments":"PointAdjustment_MKT_Junit_Test_dev_only","pointFlag":"10001001","points":[{"pointFlag":"1000","numOfPoint":"2"},{"pointFlag":"1001","numOfPoint":"3"}]}'])
    # interfaces_arr.append(["3.4.3.accIdsAdjustment",
    #                        '{"appId":"10001","timestamp":"1554262690","sign":"xxxxxx","data":{"memberId":"11047554920","posId":"104","transId":"2","storeNo":"106","orderNo":"2001190106104000002","businessDate":"2020/01/31","accounts":[{"accId":1000,"earnValue":2,"rdmValue":0},{"accId":1111,"earnValue":2,"rdmValue":0}]}}'])
    # interfaces_arr.append(["3.4.4.productPointAdjust",
    #                        '{"memberId":"xxx","productName":"xxx","storeId":"xxx","numOfPoint":"xxx","typeCode":"xxx","txnChannel":"Web"}'])
    # interfaces_arr.append(["3.1.1.query",
    #                        '{"bindType":"meituan","queryId":"11111111"}'])
    # interfaces_arr.append(["3.1.1.query.result",
    ##                       '{"memberNumber":"11000000004","mobileNo":"xxx","cardStatus":"Issued","memberStatus":"Active","memberSubStatus":"Registered","tierName":"Base","firstName":"xx","lastName":"林","gender":"F","pointValue":"14620","registerDate":"06/20/2012","expirationPoints":[],"serialNumber":null,"birthday":"08/20/1992","tierStartDate":"09/26/2019","tierEndDate":"06/19/2020","memberClass":"","vipPlusEndDate":"","joinDate":"06/20/2012","employeeFlag":"N","employeePointValue":"0","segments":[{"segmentNo":"4","segmentName":"4","segmentStartDate":"","segmentEndDate":"","segmentType":"Customer Segment","businessType":null},{"segmentNo":"105","segmentName":"aaaaabbb","segmentStartDate":"02/11/2017","segmentEndDate":"","segmentType":"POS Segment","businessType":null},{"segmentNo":"112","segmentName":"112","segmentStartDate":"04/29/2019","segmentEndDate":"","segmentType":"POS Segment","businessType":null}],"accounts":[{"accId":1000,"accValue":14620},{"accId":1001,"accValue":0},{"accId":3000,"accValue":0},{"accId":4000,"accValue":0},{"accId":1120,"accValue":100},{"accId":1121,"accValue":100},{"accId":1101,"accValue":100}]}'])
    # interfaces_arr.append(["3.1.2.queryBindShip",
    #                        '{"bindId":"oL9xvwiJofVPVPSXbixDvqPbWGwY"}'])
    # interfaces_arr.append(["3.1.2.queryBindShip.result",
    ##                     '{"bindId":"oL9xvwiJofVPVPSXbixDvqPbWGwY"}'])
    # interfaces_arr.append(["3.1.3.bind",
    #                      '{"memberNumber":"11000000004","bindType":"meituan","bindId":"11111111"}'])
    # interfaces_arr.append(["3.1.3.bind",
    #                     '{"memberNumber":"11000000004","bindType":"meituan","bindId":"11111111"}'])
    # interfaces_arr.append(["3.1.5cardSortList",
    #                     '{"queryId":"oL9xvwuceaA6lgMgOfjJKRoPVboQ","thxEndDate":"12/31/2099","thxStartDate":"12/31/2009","type":"openId","cacheType":"1","cardNum":"10"}'])
    # interfaces_arr.append(["3.1.5cardSortList.result",
    #                        '{"activationChannel":"Web","memberNumber":"19200000000","mobileNo":"xxxxxx","contactLastName":"xxxxxx","contactFirstName":"xxxxxx","gender":"F","birthday":"01/31/2020","email":"vip@watsons.com.cn","zipCode":"510000","country":"China","province":"Fujian","city":"Xiamen","addressLine":"天河区","addressLine2":"天河北路","addressLine3":"西街123号","personalIncome":"4001 - 5000","householdIncome":"4001 - 5000","jobType":[{"jobStatus":"Y","jobValue":"Student"},{"jobStatus":"N","jobValue":"Miscellaneous / Others"}],"maritalStatus":"Single","childNum":"0","receivePromotionFlag":"Y","internMailFlag":"Y","internEmailFlag":"Y","internSmsFlag":"Y","privacyAgreeFlag":"Y","agree":"1","skinType":"SkinType1","subClub":"subclub1","weiboName":"test weibo","renrenName":"test renren","tmallName":"test tmall","alipayName":"test alipay"}'])
    # interfaces_arr.append(["3.3.1.activation",
    #                       '{"activationChannel":"Web","memberNumber":"19200000000","mobileNo":"xxxxxx","contactLastName":"xxxxxx","contactFirstName":"xxxxxx","gender":"F","birthday":"01/31/2020","email":"vip@watsons.com.cn","zipCode":"510000","country":"China","province":"Fujian","city":"Xiamen","addressLine":"天河区","addressLine2":"天河北路","addressLine3":"西街123号","personalIncome":"4001 - 5000","householdIncome":"4001 - 5000","jobTypes":[{"jobStatus":"Y","jobValue":"Student"},{"jobStatus":"N","jobValue":"Miscellaneous / Others"}],"maritalStatus":"Single","childNum":"0","receivePromotionFlag":"Y","internMailFlag":"Y","internEmailFlag":"Y","internSmsFlag":"Y","privacyAgreeFlag":"Y","agree":"1","skinType":"SkinType1","subClub":"subclub1","weiboName":"test weibo","renrenName":"test renren","tmallName":"test tmall","alipayName":"test alipay"}'])
    interfaces_arr.append(["3.3.3.segment",
                           '{"memberNumber":"19200000000","businessType":"newmember","action":"CREATE","segmentName":"xxx","segmentStartDate":"01/31/2020","segmentEndDate":"03/31/2020"}'])

    for i in interfaces_arr:
        main2(Interface(i[0], i[1]))
