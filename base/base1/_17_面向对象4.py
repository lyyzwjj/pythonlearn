class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        print("装填%d个子弹" % count)
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s抢没子弹了" % self.model)
            return
        self.bullet_count -= 1
        print("%s开枪,剩余子弹%d" % (self.model, self.bullet_count))


class Soldier(object):
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # is类似equals
        if self.gun is None:
            print("%s士兵没有抢" % self.name)
            return
        self.gun.add_bullet(50)
        while self.gun.bullet_count > 0:
            self.gun.shoot()


gun = Gun("AK47")
xu = Soldier("许三多￿")
xu.gun = gun
xu.fire()
# while xu.gun.bullet_count > 0:
#    xu.fire()
