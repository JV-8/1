import datetime
import time

import psycopg2
from fastapi import Depends
from psycopg2.extras import RealDictCursor
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# engine =create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# savienojas ar PostgreSQL datu bāzi
  

def test_user(db: Session = Depends(get_db)):
    print("tests")
    
           

# ievada lietotāja vārdu un dzimšanas datumu
vards = input("Ievadi savu vārdu: ")
dzimsanas_diena = input("Ievadi savu dzimšanas diena formātā dd-mm-yyyy: ")
vārda_diena = input("Ievadi savu vārda dienas datumu formātā dd-mm: ")
# konvertē dzimšanas datumu no teksta formāta uz datetime formātu
dzimsanas_diena = datetime.datetime.strptime(dzimsanas_diena, "%d-%m-%Y").date()
vārda_diena =datetime.datetime.strptime(vārda_diena, "%d-%m").date()
# aprēķina datumu, kad jāatgādina par dzimšanas dienu
atgadinajuma_datums = dzimsanas_diena - datetime.timedelta(days=7)
atgadinajuma_datums = vārda_diena - datetime.timedelta(days=7)

# iegūst pašreizējo datumu
sodienas_datums = datetime.date.today()

# pārbauda, vai cilvēks jau eksistē datu bāzē
# with conn.cursor() as cur:
#     cur.execute("SELECT * FROM jubilejas WHERE vards_uzvards=%s AND dzimsanas_diena=%s AND vārda_diena=%s", (vards, dzimsanas_diena, vārda_diena))
#     jubilejas = cur.fetchall()
    
# ja cilvēks nav atrasts, ievada viņu datu bāzē
# if not jubilejas:
#     with conn.cursor() as cur:
#         jubilars =cur.execute("""INSERT INTO jubilejas (vards_uzvards, dzimsanas_diena, vārda_diena) VALUES (%s, %s, %s) RETURNING * """, (vards, dzimsanas_diena, vārda_diena))
#         conn.commit()
#         print(jubilars)
# pārbauda, vai ir cilvēks, kam jāatgādina par dzimšanas dienu
# with conn.cursor() as cur:
#     cur.execute("SELECT * FROM jubilejas WHERE vards_uzvards=%s AND dzimsanas_diena=%s AND vārda_diena=%s", (vards, dzimsanas_diena, vārda_diena))
#     cur.fetchall()
    
# if not jubilejas:
#     print("Sodien svētku nav.")
# else:
#     # salīdzina pašreizējo datumu ar datumu, kad jāatgādina par dzimšanas dienu
#     for jubilejas in jubilejas:
#         if sodienas_datums == atgadinajuma_datums:
#             print(f"Šonedēļ ir jāsvin {jubilejas[1]} svētku diena!")
#         elif sodienas_datums == dzimsanas_diena:
#             print(f"Sveicieni {jubilejas[1]} svētku  dienā!")
#         else:
#             print("Vēl nekas nenotiks.")
 