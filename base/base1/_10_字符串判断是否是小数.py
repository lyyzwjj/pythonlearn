# num_str="1"
# num_str="①"
num_str = '\u00b2'
num_str = '一千零一'
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())  # 可以判断unicode数字
print(num_str.isnumeric())  # 可以判断中文数字

# 去左右空格
num_str.strip()
