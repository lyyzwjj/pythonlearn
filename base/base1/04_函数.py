def print_line(i, j):
    """

    :param i:
    :param j:
    :return:
    """
    print('i=%d,j=%d' % (i, j))
    return i * j


c = print_line(1, 2)
print(c)


def print_flower(char, count):
    """

    :param char:
    :param count:
    """
    print(char * count)


print_flower("/*", 50)


def print_lines(char, count):
    """
    打印多行字符
    :param char: 需要打印的字符
    :param count: 打印次数和行数
    """
    i = 0
    while (i < count):
        print(char * count)
        i += 1


print_lines("#", 5)
