from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy import Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
import datetime

# create_engine就是去建立连接，相当于我们pymsql建立连接的时候 conn= pymysql.connect(...)
db_args = "mysql+pymysql://root:Wzzst310@163.com@129.204.35.106:3306/test?charset=utf8mb4"
conn = create_engine(
    db_args,
    max_overflow=0,  # 超过连接池大小外最多创建的连接数
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 连接池中没有线程最多等待时间，否则报错
    pool_recycle=-1,  # 多久之后对连接池中的连接进行回收（重置）-1不回收
)


# 原生sql
def test():
    ret = conn.execute("select * from face_date")
    result = ret.fetchall()
    print(result)
    ret.close()


# Base是declarative_base的实例化对象
Base = declarative_base()


# 创建和删除表
# 每个类都要继承Base
class UserInfo(Base):
    # __tablename__是必须要的，它是设置实际存在数据库中的表名
    __tablename__ = "user_info"

    # Column是列的意思，固定写法 Column(字段类型, 参数)
    # primary_key主键、index索引、nullable是否可以为空
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # 此处会给数据库加个名字叫ix_user_info_name  字段name 类型normal 索引方法BTree的索引
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    create_time = Column(DateTime, default=datetime.datetime.now)

    # 相当于Django的ORM的class Meta，是一些元信息
    __table_args__ = (
        UniqueConstraint("id", "name", name="uni_id_name"),  # unique类型的索引  名字叫uni_id_name的索引
        Index("name", "email")  # 类型normal 名字分别叫name和email的两个索引
    )


# 创建一对多的表
# ======一对多示例=======
class MyUserInfo(Base):
    __tablename__ = "t_user_info"

    id = Column(Integer, primary_key=True)
    # index=True,设置索引
    name = Column(String(32), nullable=False)
    email = Column(String(32), unique=True)
    create_time = Column('CREATE_TIME', DateTime, default=datetime.datetime.now)
    # ForeignKey字段的建立,需要指定外键绑定哪个表的哪个字段
    hobby_id = Column(Integer, ForeignKey("hobby.id"))
    # 不生成表结构 方便查询和增加的操作
    # 第一个参数是关联到哪个类(表), backref是给关联的那个类反向查询用的
    hobby = relationship("Hobby", backref="user_info")

    __table_args__ = (
        # UniqueConstraint联合唯一，这个联合唯一的字段名为：uni_id_name
        UniqueConstraint("id", "name", name="uni_id_name"),
        # 联合索引
        # Index("name", "email")
    )


class Hobby(Base):
    __tablename__ = "hobby"

    id = Column(Integer, primary_key=True)
    title = Column(String(32), default="码代码")


# ======多对多示例=======
class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    # 不生成表字段 仅用于查询和增加方便
    # 多对多的relationship还需要设置额外的参数secondary：绑定多对多的中间表
    tags = relationship("Tag", secondary="book2tag", backref="books")


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    title = Column(String(32))


class Book2Tag(Base):
    __tablename__ = "book2tag"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    tag_id = Column(Integer, ForeignKey("tag.id"))


def create_db():
    Base.metadata.create_all(conn)


def drop_db():
    Base.metadata.drop_all(conn)


if __name__ == '__main__':
    # test()
    create_db()
    # drop_db()
