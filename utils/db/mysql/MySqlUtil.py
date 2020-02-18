from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy import Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
import datetime

# create_engine就是去建立连接，相当于我们pymsql建立连接的时候 conn= pymysql.connect(...)
db_args = "mysql+pymysql://root:Wzzst310@163.com@129.204.35.106:3306/user?charset=utf8mb4"
conn = create_engine(
    db_args,
    max_overflow=0,  # 超过连接池大小外最多创建的连接数
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 连接池中没有线程最多等待时间，否则报错
    pool_recycle=-1,  # 多久之后对连接池中的连接进行回收（重置）-1不回收
)

Session = sessionmaker(bind=conn)
db_session = Session()

# Base是declarative_base的实例化对象
Base = declarative_base()


# 创建和删除表
# 每个类都要继承Base
class FaceIdentificationResult(Base):
    # __tablename__是必须要的，它是设置实际存在数据库中的表名
    __tablename__ = "t_face_identification_result"

    # Column是列的意思，固定写法 Column(字段类型, 参数)
    # primary_key主键、index索引、nullable是否可以为空
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 此处会给数据库加个名字叫ix_user_info_name  字段name 类型normal 索引方法BTree的索引
    res_code = Column(String(255))
    res_msg = Column(String(255))
    compare_source = Column(String(255))
    result_gmsfhm = Column(String(255))
    result_xm = Column(String(255))
    result_fx = Column(String(255))
    hint = Column(String(255))

    def __init__(self, result_dict):
        self.res_code = result_dict.get("RES_CODE")
        self.res_msg = result_dict.get("RES_MSG")
        self.compare_source = result_dict.get("COMPARE_SOURCE")
        self.result_gmsfhm = result_dict.get("RESULT_GMSFHM")
        self.result_xm = result_dict.get("RESULT_XM")
        self.result_fx = result_dict.get("RESULT_FX")
        self.hint = result_dict.get("HINT")
