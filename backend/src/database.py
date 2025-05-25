from sqlalchemy.exc import SQLAlchemyError
from .models import db, Producao

def save_to_database(data):
    """Salva dados raspados no PostgreSQL com commit/rollback explícito"""
    try:
        # Remove registros antigos
        db.session.execute(
            db.delete(Producao).where(Producao.ano == data['ano'])
        )

        for categoria in data['dados']:
            parent = Producao(
                ano=data['ano'],
                produto=categoria['produto'],
                quantidade=categoria['quantidade'],
                parent_id=None
            )
            db.session.add(parent)
            db.session.flush()

            for sub in categoria['subprodutos']:
                child = Producao(
                    ano=data['ano'],
                    produto=sub['produto'],
                    quantidade=sub['quantidade'],
                    parent_id=parent.id
                )
                db.session.add(child)

        db.session.commit()
        return True

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"❌ Erro de banco de dados: {str(e)}")
        return False
    except Exception as e:
        db.session.rollback()
        print(f"❌ Erro inesperado: {str(e)}")
        return False

def get_from_database(year):
    """Recupera dados do PostgreSQL"""
    try:
        categorias = Producao.query.filter_by(ano=year, parent_id=None).all()
        
        if not categorias:
            return None
            
        return {
            'ano': year,
            'dados': [{
                'produto': cat.produto,
                'quantidade': cat.quantidade,
                'subprodutos': [{
                    'produto': sub.produto,
                    'quantidade': sub.quantidade
                } for sub in cat.subprodutos]
            } for cat in categorias],
            'total': sum(cat.quantidade for cat in categorias if cat.quantidade)
        }
    except Exception as e:
        print(f"Erro ao buscar no banco: {str(e)}")
        return None