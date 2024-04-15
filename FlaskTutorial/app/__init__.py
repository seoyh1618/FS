from flask import Flask,Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sys, os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DevelopmentConfig,ProductionConfig,TestingConfig

db = SQLAlchemy()
migrate = Migrate()

# Blueprint 동적 등록 
# 단점 : import_module() 을 통해 load 하기 때문에 초기 module 에 모든 라이브러리를 가져와야 한다. 
# -> Python GC를 통해 어느정도 문제는 발생하지 않으나 오버헤드가 발생 
# 장점 : 추가시 일일히 Register에 등록하지 않아도 된다. views __init__.py 포함
def register_blueprints(app) :
    views_dir = os.path.join(os.path.dirname(__file__),'views')
    for filename in os.listdir(views_dir) : 
        if filename.endswith('.py') and filename != '__init__.py' : 
            module_name = f"app.views.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr_name in dir(module) : 
                attr = getattr(module,attr_name)
                if isinstance(attr,Blueprint) : 
                    app.register_blueprint(attr)

def create_app(config_name=None)  :
    app = Flask(__name__)
    
    # Config 설정이 None 일 경우 Development 설정 참조 
    if not config_name : 
        app.config.from_object(DevelopmentConfig)
    else : 
        if config_name == 'development' : 
            app.config.from_object(DevelopmentConfig)
        elif config_name == 'production' :
            app.config.from_object(ProductionConfig)
        else :
            app.config.from_object(TestingConfig) 
    
    #BluePrint Setup 
    register_blueprints(app)

    #ORM Part 
    db.init_app(app)
    migrate.init_app(app, db)

    return app
