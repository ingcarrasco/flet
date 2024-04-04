import pyodbc
import os

from datetime import datetime

SERVER = os.getenv('SQLSERVER')
DATABASE = 'SS'
USERNAME = os.getenv('DBUSER')
PASSWORD = os.getenv('DBPASS')

# Asesor GMA
# Tecnico EEJ

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

# Select
SQL_QUERY = """
SELECT PAR_TIPOPARA, PAR_IDENPARA, PAR_IDMODULO, PAR_DESCRIP1, PAR_DESCRIP2, 
CASE 
    WHEN RIGHT(PAR_DESCRIP2, 1) = ','
        THEN 'Ok' 
    ELSE 'No' 
END, 
PAR_DESCRIP3, PAR_DESCRIP4, PAR_DESCRIP5, PAR_STATUS, PAR_IMPORTE1, PAR_IMPORTE2, 
PAR_IMPORTE3, PAR_IMPORTE4, PAR_IMPORTE5, PAR_FECHA1, PAR_FECHA2, PAR_FECHA3, 
PAR_HORA1, PAR_HORA2, PAR_HORA3, PAR_CVEUSU, PAR_FECHOPE, PAR_HORAOPE
FROM GSH_KOA_HER.dbo.PNC_PARAMETR
WHERE PAR_TIPOPARA=N'ACTPANSE' AND PAR_IDENPARA=N'EVIDENSE' AND PAR_DESCRIP2 LIKE '%GMA%';
"""
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.PAR_TIPOPARA}\t{r.PAR_IDENPARA}\t{r.PAR_DESCRIP1}\t{r.PAR_DESCRIP2}")

current_dateTime = datetime.now()

user_new1='MRF'
user_new2='MRF'
user_new3='%MRF%'
user_old='%MMM%'
user_name='Nombre'
date_now = str(current_dateTime.day) + """/""" + str(current_dateTime.month) + """/""" + str(current_dateTime.year)
time_now = str(current_dateTime.hour) + """:""" + str(current_dateTime.minute)
# Update
# SQL_QUERY = """
# UPDATE GSH_KOA_OBR.dbo.PNC_PARAMETR
# SET  
#     PAR_DESCRIP2=(
#         CASE 
#             WHEN RIGHT(PAR_DESCRIP2, 1) = ','
#                 THEN CONCAT(PAR_DESCRIP2, '?,')
#             ELSE CONCAT(PAR_DESCRIP2, ',?,') 
#         END),
#     PAR_CVEUSU=N'GMI',
#     PAR_FECHOPE=N'?', 
#     PAR_HORAOPE=N'?'
# WHERE PAR_TIPOPARA=N'ACTPANSE' AND PAR_DESCRIP2 LIKE '?' AND PAR_DESCRIP2 NOT LIKE '?';
# """
# cursor.execute(SQL_QUERY, user_new1, user_new2, date_now, time_now, user_old, user_new3)

################        OK          ################ 
################        ASCOM       ################ 

SQL_QUERY="""
SELECT PAR_TIPOPARA FROM pnc_parametr
    WHERE PAR_TIPOPARA = 'ASCOM' AND PAR_IDENPARA = ?
"""

cursor.execute(SQL_QUERY, (user_new1))

records = cursor.rowcount
if records == 0:
    SQL_QUERY = """INSERT INTO pnc_parametr 
        (PAR_TIPOPARA,PAR_IDENPARA,PAR_IDMODULO,PAR_DESCRIP1,PAR_DESCRIP2,
        PAR_DESCRIP3,PAR_DESCRIP4,PAR_DESCRIP5,PAR_STATUS,PAR_IMPORTE1,
        PAR_IMPORTE2,PAR_IMPORTE3,PAR_IMPORTE4,PAR_IMPORTE5,PAR_FECHA1,
        PAR_FECHA2,PAR_FECHA3,PAR_HORA1,PAR_HORA2,PAR_HORA3,PAR_CVEUSU,
        PAR_FECHOPE,PAR_HORAOPE) 
    VALUES (N'ASCOM',?,N'SER',?,N'(644) 128 7550',N'EXT',N'',N'',N'A',
    0.00000,0.00000,0.00000,0.00000,0.00000,N'          ',N'          ',
    N'          ',N'     ',N'     ',N'     ',N'GMI',?,?);"""

    cursor.execute(SQL_QUERY,(user_new1,user_name,date_now,time_now))

    conn.commit()

################                  ################ 
################        ASAUTO       ################ 

SQL_QUERY="""
SELECT PAR_TIPOPARA FROM pnc_parametr
    WHERE PAR_TIPOPARA = 'ASAUTO' AND PAR_IDENPARA = ?
"""

cursor.execute(SQL_QUERY, (user_new1))

records = cursor.rowcount
if records == 0:
    print(records)
conn.commit()


cursor.close()
conn.close()