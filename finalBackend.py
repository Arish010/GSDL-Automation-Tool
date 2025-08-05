import geopandas as gpd
import pandas as pd
import geoalchemy2
import os
import psycopg2
from sqlalchemy import create_engine

shapeFilePath = "D:\\Programming\\Python\\backend\\testing stuff\\karnataka_bagalkote_badami_parcel_boundary.shp"
shapeFile = gpd.read_file(shapeFilePath)
shapeFileName = os.path.splitext(os.path.basename(shapeFilePath))[0]
print(shapeFileName)

excelFilePath = "D:\\Programming\\Python\\backend\\testing stuff\\excel_karnataka_bagalkote_badami.xlsx"
excelFile = pd.read_excel(excelFilePath)
excelFileName = os.path.splitext(os.path.basename(excelFilePath))[0]
print(excelFileName)
# adding a comment just for commitment purposes
# importing shapefile content to postgres
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="gsdlAutomation",
        user="postgres",
        password="root"
    )

    cursor = conn.cursor()
    engine = create_engine("postgresql://postgres:root@localhost:5432/gsdlAutomation")

    shapeFile.to_postgis(shapeFileName, con = engine, schema = 'public', index = False, if_exists = 'replace')
    print("shapefile data written to database")

except:
    print("data not inserted to database")


# importing excelfile content to postgres
try:
    excelFile.to_sql(excelFileName, con = engine, if_exists = 'replace', schema = 'public', index = False)
    print("excel data written to database")

except:
    print("data not inserted to database")

# summarizing the code of village names from shapefile
summarizingQuery = cursor.execute(f"""select "NAME" from {shapeFileName} GROUP BY "NAME";""")
summarizingResult = cursor.fetchall()
# for i in summarizingResult:
#     print(i)

for row in summarizingResult:
    print(row[0])
    cursor.execute(f"""insert into {excelFileName} (village_name_real) values ('{row[0]}');""")
    conn.commit()
    # print("inserted data")

# cursor.execute(f"INSERT INTO {table_name} (name_column) VALUES ('{name[0]}')")