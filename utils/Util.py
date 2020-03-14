import json
from utils.excel.ExcelUtil import *


def def1():
    # records = json.load(open("/Users/wjj/Desktop/topic.json"))
    records = json.load(open("C:/Users/Administrator/Desktop/topic.json", encoding='utf-8'))
    data = []
    # for record in records:
    #     for key in record:
    #         data.append(FaceIdentificationResult(json.loads(record[key])))
    # db_session.add_all(data)
    # db_session.commit()
    # db_session.close()
    data = records
    column_keys = []
    column_key1 = ColumnKey("name", 1, "栏目")
    column_key2 = ColumnKey("id", 2, "id")
    column_key3 = ColumnKey("title", 3, "标题")
    column_key4 = ColumnKey("tag_url", 4, "跳转链接")
    column_key5 = ColumnKey("page_type", 5, "跳转类型")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    column_keys.append(column_key3)
    column_keys.append(column_key4)
    column_keys.append(column_key5)

    # column_key1 = ColumnKey("RESULT_FX", 1, "结果")
    # column_key2 = ColumnKey("RESULT_GMSFHM", 3, "公民身份号码的核查结果,校验异常时为空。枚举值：一致,不一致")
    # column_key4 = ColumnKey("RESULT_XM", 4, "姓名核查结果,校验异常时为空。枚举值：一致,不一致")
    # column_key5 = ColumnKey("RES_CODE", 0, "响应码")
    # column_key8 = ColumnKey("RES_MSG", 2, "响应信息")
    # column_key9 = ColumnKey("COMPARE_SOURCE", 5, "比对来源,1:公安,2：第三方")
    # column_keys.append(column_key1)
    # column_keys.append(column_key2)
    # column_keys.append(column_key3)
    # column_keys.append(column_key4)
    # column_keys.append(column_key5)
    # column_keys.append(column_key8)
    # column_keys.append(column_key9)
    eu = ExcelUtil()
    eu.list2excel_file(column_keys, data, "太平优视文章")


def def2():
    column_keys = []
    column_key1 = ColumnKey("name", 1, "栏目")
    column_key2 = ColumnKey("id", 2, "id")
    column_key3 = ColumnKey("title", 3, "标题")
    column_key4 = ColumnKey("tag_url", 4, "跳转链接")
    column_key5 = ColumnKey("page_type", 5, "跳转类型")
    column_key6 = ColumnKey("new_page_type", 6, "新跳转链接地址")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    column_keys.append(column_key3)
    column_keys.append(column_key4)
    column_keys.append(column_key5)
    column_keys.append(column_key6)
    return ExcelUtil.excel_file2list(column_keys, file_path="../resources/excel/太平优视文章-20200225-2.xlsx")


def def3():
    column_keys = []
    column_key1 = ColumnKey("保单归属", 1, "保单归属")
    column_key2 = ColumnKey("数量", 2, "数量")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    return column_keys


def def4():
    column_keys = []
    column_key1 = ColumnKey("JOB_CODE", 1, "JOB_CODE")
    column_key2 = ColumnKey("CLASS_1", 2, "CLASS_1")
    column_key3 = ColumnKey("CLASS_2", 3, "CLASS_2")
    column_key4 = ColumnKey("CLASS_3", 4, "CLASS_3")
    column_key5 = ColumnKey("NAME", 5, "职业")
    column_keys.append(column_key1)
    column_keys.append(column_key2)
    column_keys.append(column_key3)
    column_keys.append(column_key4)
    column_keys.append(column_key5)
    ExcelUtil.excel_file2json_file(column_keys, '../resources/excel/职业代码 .xlsx', 'job.json')


def list2excel_file(file_name, column_keys_list, json_file_path=None, data=None):
    column_keys = []
    for index, column_key_list in enumerate(column_keys_list):
        if len(column_key_list) < 2:
            column_key = ColumnKey(column_key_list[0], index)
        else:
            column_key = ColumnKey(column_key_list[0], index, column_key_list[1])
        column_keys.insert(index, column_key)
    if data is None and json_file_path is not None:
        data = json.load(open(json_file_path, encoding='utf-8'))
    eu = ExcelUtil()
    eu.list2excel_file(column_keys, data, file_name)


if __name__ == '__main__':
    # new_column_keys_list = [["userid", "用户id"], ["first_login_time", "首次登陆时间"]]
    # list2excel_file("第三方机构邀请用户表", new_column_keys_list, "../resources/excel/mdmuser.json")
    def4()
