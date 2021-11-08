from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    '''明确users表的结构'''
    table_name = 'User'  # 定义表名为User_tb
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User %r' % self.nickname


if __name__ == '__main__':
    print("......")
    db.drop_all()
    db.create_all()
    # p1 = User(nickname='leo', email='leo.liu@italki.com')
    # p2 = User(nickname='test', email='test@italki.com')
    p3 = User(username='curry', nickname='curry', email='stephen.curry@italki.com', password = '123123')
    db.session.add_all([p3])  # 向表中添加两条数据
    db.session.commit()
