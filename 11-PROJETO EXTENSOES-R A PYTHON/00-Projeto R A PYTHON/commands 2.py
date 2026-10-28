from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seu_usuario:senha@localhost/nome_do_banco'
db = SQLAlchemy(app)

class Morador(db.Model):
    __tablename__ = 'moradores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    cep = db.Column(db.String(8), nullable=False)
    data_nascimento = db.Column(db.Date)
    contato = db.Column(db.String(255))

class Necessidade(db.Model):
    __tablename__ = 'necessidades'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    morador_id = db.Column(db.Integer, db.ForeignKey('moradores.id', ondelete='SET NULL'))
    data_submissao = db.Column(db.Date)

    morador = db.relationship('Morador', backref=db.backref('necessidades', lazy=True))

class Sugestao(db.Model):
    __tablename__ = 'sugestoes'

    id = db.Column(db.Integer, primary_key=True)
    sugestao = db.Column(db.Text, nullable=False)
    morador_id = db.Column(db.Integer, db.ForeignKey('moradores.id', ondelete='SET NULL'))
    data_submissao = db.Column(db.Date)

    morador = db.relationship('Morador', backref=db.backref('sugestoes', lazy=True))

from flask_migrate import Migrate

migrate = Migrate(app, db)

Flask db init
flask db migrate -m "Initial migration";
flask db upgrade
from flask import jsonify
from models import Morador  # Certifique-se de que você está importando corretamente seus modelos

@app.route('/moradores', methods=['GET'])
def get_moradores():
    moradores = Morador.query.all()
    return jsonify([morador.serialize() for morador in moradores])

if __name__ == '__main__':
    app.run(debug=True)
    
