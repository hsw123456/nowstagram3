
# -*-encoding=UTF-8-*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
app = Flask(__name__)
app.config.from_pyfile('app.conf')

app.secret_key = 'nowcoder'#在session中传递错误消息的时候必须要添加
db = SQLAlchemy(app)#we should put this line after load app.conf

login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/' # 如果没有登录自动跳转到该页面

from nowstagram import  models,views