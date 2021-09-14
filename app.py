from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:////mnt/c/Users/pragati/Documents/post.db"
app.config['SQLALCHEMY_BINDS'] = {'mysql':"sqlite:////mnt/c/Users/pragati/Documents/post.db"}

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class PostgresData(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class MysqlData(db.Model):
    __bind_key__ = 'mysql'
    id = db.Column(db.Integer, primary_key=True)


@app.route('/PostgreSQL')
def postgresDB():
    data = PostgresData.query.all()
    return render_template('postgres.html',data=data)

@app.route('/MySQL')
def postgresDB():
    data = MysqlData.query.all()
    return render_template('mysql.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)