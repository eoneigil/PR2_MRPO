from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SQLRepository:
    def __init__(self, model_class, connection_string):
        self.model_class = model_class
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_all(self):
        return self.session.query(self.model_class).all()

    def get_by_id(self, id):
        return self.session.query(self.model_class).filter_by(id=id).first()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity):
        db_entity = self.get_by_id(entity.id)
        for key, value in vars(entity).items():
            setattr(db_entity, key, value)
        self.session.commit()

    def delete_by_id(self, id):
        entity = self.get_by_id(id)
        self.session.delete(entity)
        self.session.commit()
