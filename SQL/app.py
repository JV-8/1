import datetime
import time
from datetime import date, timedelta

import psycopg2
from psycopg2.extras import RealDictCursor

# savienojas ar PostgreSQL datu bāzi
while True:

    try:
      conn = psycopg2.connect(host= 'localhost',
                              database ='postgres',
                              user= 'postgres',
                              password='Janis1993',
                              cursor_factory= RealDictCursor)
      cursor = conn.cursor()
      print("Databases connection was succesfull!")
      break
    except Exception as error:
        print("Connestiin to database failed")   
        print("Error:", error)
        time.sleep(2)      

# # # izveido tabulu "cilveki"
# with conn.cursor() as cur:
#     cur.execute("CREATE TABLE jubilejas (id SERIAL PRIMARY KEY, vards_uzvards VARCHAR(50) NOT NULL, dzimsanas_diena DATE NOT NULL, vārda_diena DATE NOT NULL)")
#     conn.commit()   



# ievada lietotāja vārdu un dzimšanas datumu
vards = input("Ievadi savu vārdu: ")
dzimsanas_diena = input("Ievadi savu dzimšanas diena formātā dd.mm.yyyy: ")
vārda_diena = input("Ievadi savu vārda dienas datumu formātā dd.mm: ")


# konvertē dzimšanas datumu no teksta formāta uz datetime formātu
dzimsanas_diena = datetime.datetime.strptime(dzimsanas_diena, "%d.%m.%Y").date()
vārda_diena =datetime.datetime.strptime(vārda_diena, "%d.%m").date()


# aprēķina datumu, kad jāatgādina par dzimšanas dienu
atgadinajuma_datums = dzimsanas_diena - datetime.timedelta(days=7)
atgadinajuma_datums = vārda_diena - datetime.timedelta(days=7)

# iegūst pašreizējo datumu
sodienas_datums = datetime.date.today()

# pārbauda, vai cilvēks jau eksistē datu bāzē
with conn.cursor() as cur:
    cur.execute("SELECT * FROM jubilejas WHERE vards_uzvards=%s AND dzimsanas_diena=%s AND vārda_diena=%s", (vards, dzimsanas_diena, vārda_diena))
    jubilejas = cur.fetchall()
    
# ja cilvēks nav atrasts, ievada viņu datu bāzē
if not jubilejas:
    with conn.cursor() as cur:
        jubilars =cur.execute("""INSERT INTO jubilejas (vards_uzvards, dzimsanas_diena, vārda_diena) VALUES (%s, %s, %s) RETURNING * """, (vards, dzimsanas_diena, vārda_diena))
        conn.commit()
        print(jubilars)

conn.cursor() 

# pārbauda, vai ir cilvēks, kam jāatgādina par dzimšanas dienu
with conn.cursor() as cur:
    cur.execute("SELECT * FROM jubilejas WHERE vards_uzvards=%s AND dzimsanas_diena=%s AND vārda_diena=%s", (vards, dzimsanas_diena, vārda_diena))
    cur.fetchall()
    
if not jubilejas:
    print("Sodien svētku nav.")
else:
    # salīdzina pašreizējo datumu ar datumu, kad jāatgādina par dzimšanas dienu
    for jubilejas in jubilejas:
        if sodienas_datums == atgadinajuma_datums:
            print(f"Šonedēļ ir jāsvin {jubilejas[1]} svētku diena!")
        elif sodienas_datums == dzimsanas_diena:
            print(f"Sveicieni {jubilejas[1]} svētku  dienā!")
        else:
            print("Vēl nekas nenotiks.")



# izveido SQL pieprasījumu, kas atgriezīs visus jubilārus, kam šodien ir dzimšanas diena vai vārda diena
sql = "SELECT * FROM jubilejas WHERE dzimsanas_diena::text LIKE %s OR vārda_diena::text LIKE %s"
params = (f"%-{sodienas_datums.month:02d}-{sodienas_datums.day:02d}", f"%-{sodienas_datums.month:02d}-{sodienas_datums.day:02d}")
cursor.execute(sql, params)
jubilejas = cursor.fetchall()

time.sleep(86400)