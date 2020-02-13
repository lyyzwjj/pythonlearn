import json
from utils.ExcelUtil import *


def read_file(path):
    file = open(path, "r")
    return file.readlines()


def json_str2obj(json_str):
    return json.loads(json_str)


if __name__ == '__main__':
    records = json.load(open("/Users/wjj/Desktop/无标题.json"))
    data = []
    for record in records:
        for key in record:
            data.append(json.loads(record[key]))
    column_keys = []
    column_key1 = ColumnKey("RESULT_FX", 1, "结果")
    column_key2 = ColumnKey("RESULT_GMSFHM", 3, "公民身份号码的核查结果,校验异常时为空。枚举值：一致,不一致")
    column_key4 = ColumnKey("RESULT_XM", 4, "姓名核查结果,校验异常时为空。枚举值：一致,不一致")
    column_key5 = ColumnKey("RES_CODE", 0, "响应码")
    column_key8 = ColumnKey("RES_MSG", 2, "响应信息")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    column_keys.append(column_key4)
    column_keys.append(column_key5)
    column_keys.append(column_key8)
    eu = ExcelUtil()
    eu.list2excel_file(column_keys, data, "人脸识别错误")

