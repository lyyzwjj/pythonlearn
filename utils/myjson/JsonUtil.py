import json


def read_file(path):
    file = open(path, "r")
    return file.readlines()


def json_str2obj(json_str):
    return json.loads(json_str)
