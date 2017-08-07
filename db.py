import pyodbc
import json
import collections
import requests

server = 'bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com'
database = 'bentexmssql'
username = '****'
password = '****'
#driver= '{ODBC Driver 11 for SQL Server}'
cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com,1433;DATABASE=tempdb;UID=dreamwave1234;PWD=****")

url = "https://prod-ua.deposco.com/integration/RBY/items/"

headers = {
    'authorization': "Basic YmVudGV4OmJlbnRleHRlc3Q=",
    'cache-control': "no-cache",
    'Content-Type': 'application/xml',
    'Accept-Encoding': "gzip,deflate",
    'Host': 'prod-ua.deposco.com',
    'Content-Length': '3200',
    'Accept-Encoding': 'gzip,deflate'
    }

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM dbo.items')
rows = cursor.fetchall()

field_names = [i[0] for i in cursor.description]

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d[ field_names[0] ] = row[0]
    d[ field_names[1] ] = row[1]
    d[ field_names[2] ] = row[2]
    d[field_names[3]] = row[3]
    d[field_names[4]] = row[4]
    d[field_names[5]] = row[5]
    d[field_names[6]] = row[6]
    objects_list.append(d)

#Generate JSON data for POST
json_string = json.dumps( objects_list )

print json_string

#Sent API POST request
response = requests.request("POST", url, headers=headers,data=data)
print(response)


