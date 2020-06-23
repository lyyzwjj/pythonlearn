stu_a = {
    "name": "A", "age": 21, "gender": 1, "hometown": "河北"
}
stu_b = {
    "name": "B", "age": 22, "gender": 0, "hometown": "山东"
}
stu_c = {
    "name": "C", "age": 20, "gender": 1, "hometown": "安徽"
}
find_name="D"
students = [stu_a, stu_c, stu_c]
for stu in students:
    print(stu)
    if stu["name"] == "A":
        print("找到了%s" % stu["name"])
        stu["name"] =={"D"}  #没有改变原来的stu_a
        break;
else:
    #如果希望在搜索列表时,所有的字典检查之后,都没有发现需要搜索的目标
    #还希望得到同意的指示
    print("抱歉没有找到%s"%find_name)
print(students)
students[0]["name"]="D"
print(students)
