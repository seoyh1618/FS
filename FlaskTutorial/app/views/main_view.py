from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/home')

@bp.route('/')
def main() :
    return "Hello World ! "