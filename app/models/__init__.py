import os

from sqlmodel import SQLModel, Session, create_engine

from app.models.user import User


current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
db_file = os.path.join(root_dir, 'database.sqlite')

print('DB:', db_file)


engine = create_engine(f'sqlite:///{db_file}')
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

__all__ = ['get_session']
