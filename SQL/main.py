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


# Iegūst šodienas datumu
today = date.today()

# Izveido funkciju, kas apstrādā katru rindu, kas atgriezta no vaicājuma
def process_row(row):
    # Darbības, kas jāveic ar katru rindu
    print(row)

# Izveido vaicājumu
query = "SELECT * FROM jubilejas WHERE dzimsanas_diena = %s"

# Izpilda vaicājumu, izmantojot cursor iteratoru
with conn.cursor() as cur:
    cur.execute(query, (today,))
    for row in cur:
        process_row(row)

# Aizver savienojumu ar datubāzi
conn.close()        