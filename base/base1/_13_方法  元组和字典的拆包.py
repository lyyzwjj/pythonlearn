def print_info(name, age="", gender="男"):
    print(name)
    print(age)
    print(gender)


print_info("小明")
print_info("小明", gender="女")


def cal(*args, **kwargs):
    count = 0
    for i in args:
        count += i

    print(args)
    print(count)
    print(kwargs)
    for item in kwargs:
        print(item)


cal(1, 2, 3, 3, name="小小", age=11)
list1 = [1, 2, 4, 5, 7]
tuple1 = [1, 2, 4, 5, 7]
dict1 = {"name": "小小", "age": "1"}
dict2 = {"name": "小美", "age": "2"}

#字典拆包 字典变量  需要加* 或者**
cal(*list1, **dict1)
cal(*tuple1, **dict1)



def sum_sub(a, b):
    return a + b, a - b


# 返回值默认是个元组
sum, sub = sum_sub(1, 2)
print(sum)
print(sub)
