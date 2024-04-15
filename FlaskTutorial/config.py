from dotenv import load_dotenv
import os

load_dotenv()

class Config : 
    #SECRET_KEY = os.getenv('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    pass 

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # 프로덕션 환경에 최적화된 설정을 여기에 넣습니다.
    
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql:///your_prod_db')
    #MAIL_SERVER = 'smtp.example.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    #MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


class TestingConfig(Config) : 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # 테스트 환경에 특화된 설정을 여기에 넣습니다.
    #TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 인 메모리 DB 사용
    # 테스트에 필요한 설정 ...
    #WTF_CSRF_ENABLED = False  # 폼 테스트를 위해 CSRF 토큰을 비활성화


class DevelopmentConfig(Config) : 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # 개발 환경에 적합한 설정을 여기에 넣습니다.
    
    #SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///your_dev_db.sqlite')
    # 일반적으로 개발 중에는 디버그 모드를 활성화하고, 상세한 로그를 출력합니다.
    # 개발용 편의 기능 추가 .

