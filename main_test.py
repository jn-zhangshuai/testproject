
from sqlalchemy import inspect
from routes import app,db


    


if __name__ == '__main__':
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('user'):
            from models.test2 import User
            db.create_all()
            user = User(userid="root", userpwd="123456")
            db.session.add(user)
            db.session.commit()
    app.run(host='0.0.0.0', debug=True, port=8080)