from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Janis1993@localhost/postgres'

#savienojas ar datubāzi
engine =create_engine(SQLALCHEMY_DATABASE_URL)

#sarunāties ar data bāzi
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()