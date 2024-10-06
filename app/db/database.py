from sqlmodel import create_engine, SQLModel, Session


#TODO: Maybe I need to move it somewhere else with all other configs
DATABASE_URL = "postgresql://moesalari:123456@localhost:5433/task1"


engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session