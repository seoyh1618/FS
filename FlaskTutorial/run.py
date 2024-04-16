import os
from app import create_app,db,migrate

MIGRATION_DIRECTROY_PATH = os.path.join(os.path.dirname(__file__),'migrations')

app = create_app('development')

if __name__ == '__main__' :     

    #if not os.path.exists(MIGRATION_DIRECTROY_PATH) : 
    #    with app.app_context():
    #        db.create_all()
    #        migrate.init_app(app, db)    
        
    app.run(port=3001,host='0.0.0.0',debug=app.config['DEBUG'])
