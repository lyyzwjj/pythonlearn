a = "传智播客"
print(type(a))
b = a.encode()
print(type(b))
print(b)
# byte 类型字符串 b'\xe4\xbc\xa0\xe6\x99\xba\xe6\x92\xad\xe5\xae\xa2'
print(b.decode("utf-8"))
print(b.decode("utf8"))
print(b.decode("UTF8"))
print(b.decode("UTF-8"))
print(b.decode("UTF_8"))
print(a.encode("gbk"))  # b'\xb4\xab\xd6\xc7\xb2\xa5\xbf\xcd'
print(a.encode("gbk").decode("gbk"))
