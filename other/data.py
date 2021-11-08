from flask import Flask, flash, request, jsonify
# 连接mysql数据库需要导入pymysql模块
import pymysql

app = Flask(__name__)

# # 连接mysql数据库需要导入pymysql模块
# import pymysql

pymysql.install_as_MySQLdb()

# 导入SQLAlchemy扩展：通过python对象操作数据库
from flask_sqlalchemy import SQLAlchemy

# 配置数据库的地址； 协议+用户名:密码@主机IP/数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask?charset=utf8'
# 实时跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化SQLALchemy,实例化需要写在配置数据库之后
db = SQLAlchemy(app)


# 定义数据库模型
class need(db.Model):
    # 定义创建的表名
    __tablename__ = 'needs'
    # 定义字段
    # primary_key=True 声明主键  unique=True 值唯一  nullable=False 非空
    # 默认主键（label_id）auto_increment 自增
    need_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(16))
    applicant_name = db.Column(db.String(16))
    applicant_number = db.Column(db.Integer)
    department = db.Column(db.String(16))
    business = db.Column(db.String(16))
    systemctl_number = db.Column(db.String(16))
    cause = db.Column(db.String(40))


if __name__ == '__main__':
    # 删除所有表
    # db.drop_all()
    # 创建所有表
    db.create_all()
    app.run(host="127.0.0.1:5000", debug=True, )

