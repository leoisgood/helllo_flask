# -*- coding: utf-8 -*-
from flask import Flask, redirect
from flask import request
from flask.templating import render_template
from flask.helpers import url_for
# from Ansible_platform1 import info
import pymysql
from flask_sqlalchemy import SQLAlchemy
import psutil
import datetime
import urllib
import json
import os
import sys

import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))

sys.path.append(curPath)

print(sys.path)

db = pymysql.connect(host="127.0.0.1", user="root", password='italki123', db='test')
cur = db.cursor()
app = Flask(__name__)

'''
登录界面的路由设置，包括页面内的登录，注册，以及忘记密码的页面跳转
'''


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/static/<path:path>', methods=['POST'])
def login_post(path):
    print(path)
    if path == "login":
        username = request.form['username']
        password = request.form['password']
        sql = """ select username,password from user where username='%s' and password='%s' """ % (username, password)
        cur.execute(sql)
        results = cur.fetchone()
        if results:
            return render_template('index.html')
            db.close()
        else:
            return render_template('registration.html')
            db.close()
    if path == "reset-password":
        return render_template('reset-password.html')
    elif path == "registration":
        return render_template('registration.html')
    else:
        return render_template('error-500.html')


@app.route('/register', methods=['Get'])
def register():
    return render_template('registration.html')


@app.route('/register', methods=['POST'])
def register_post():
    id = 4
    nickname = request.form['name1']
    username = request.form['name1']
    email = request.form['email']
    password = request.form['password1']
    role = 0
    rename = """
        select * from user where username='%s'
        """
    n = cur.execute(rename % username)
    db.commit()
    if n <= 0:
        sql_insert = """
             insert into user values('%s', '%s','%s','%s','%s','%s')
                                           """
        cur.execute(sql_insert % (id, nickname, username, email, password, role))
        db.commit()
        return render_template('login.html')
    else:
        return render_template('login.html')
    db.close()


app.run('127.0.0.1', port=6789, debug=True)
