import json


def read_file(path):
    file = open(path, "r")
    return file.readlines()


def json_str2obj(json_str):
    return json.loads(json_str)


if __name__ == '__main__':
    l = []
    with open("../../resources/excel/userids.json") as f_obj:
        mylist = json.load(f_obj)
    for m in mylist:
        l.append(m['userid'])
    with open("../../resources/excel/userids1.json", "w") as f_obj:
        json.dump(l, f_obj)
    print(l)
