import json
from datetime import date
from datetime import datetime


def read_file(path):
    file = open(path, "r")
    return file.readlines()


# class MyEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, datetime):
#             return o.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(o, date):
#             return o.strftime('%Y-%m-%d')
#         else:
#             return o.__dict__

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def json_str2obj(json_str):
    return json.loads(json_str)


def obj2json_str(obj):
    return json.dumps(obj)


def obj2json_str(obj, encoder):
    return json.dumps(obj, cls=encoder)


def main():
    l = []
    with open("../../resources/excel/userids.json") as f_obj:
        mylist = json.load(f_obj)
    for m in mylist:
        l.append(m['userid'])
    with open("../../resources/excel/userids1.json", "w") as f_obj:
        json.dump(l, f_obj)
    print(l)
