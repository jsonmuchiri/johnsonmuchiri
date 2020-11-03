from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes import index


app = Flask(__name__)
app.register_blueprint(index)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
