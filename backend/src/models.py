from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producao(db.Model):
    __tablename__ = 'producao'

    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    produto = db.Column(db.String, nullable=False)
    quantidade = db.Column(db.BigInteger, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('producao.id'), nullable=True)

    subprodutos = db.relationship('Producao', remote_side=[id])

    def __repr__(self):
        return f'<Producao {self.ano} - {self.produto}>'