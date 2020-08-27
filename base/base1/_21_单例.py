##python单例写法##
class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("创建对象,分配空间")
        if MusicPlayer.instance is None:
            # 分配空间  调用父类new 方法并切纪录结果返回给python解释器
            cls.instance = super().__new__(cls)
            print("父类创建对象")
            # 返回对象的引用
        # 返回单例对象
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return

        print("播放器初始化")

        MusicPlayer.init_flag = True


m = MusicPlayer()
m = MusicPlayer()


def haha():
    print("单例haha")
