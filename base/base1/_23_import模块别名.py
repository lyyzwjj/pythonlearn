#导入模块起别名
import _22_异常 as exce
#导入部分 全局变量函数名类
from _20_静态类 import Tool
exce.raise_exception()
tool = Tool()
tool.static()
#导入同名函数
from _20_静态类 import haha
from _21_单例 import haha as haha_single
from _06_方法 import * #工作不推荐
print_lines()
haha()
haha_single()
import _24_main as main
main.say()
