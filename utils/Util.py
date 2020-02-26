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


if __name__ == '__main__':
    objs = def2()
    sql_proto = "update campaigns.t_topic set link_path = '%s', tag_url = '%s' where id = %d;"
    # sql_proto = "%s, %s"
    for obj in objs:
        if obj['new_page_type'] is not None and obj['new_page_type'].strip() != '':
            print(sql_proto % (obj['new_page_type'], obj['new_page_type'], obj['id']))
            # print(sql_proto % (obj['name'], obj['title']))
