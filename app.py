from flask import Flask
from db import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        from models import Event
        db.create_all()

    return app

app = create_app()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        from models import Event
        db.create_all()

    return app


if __name__ == '__main__':
    app.run(debug=True)
