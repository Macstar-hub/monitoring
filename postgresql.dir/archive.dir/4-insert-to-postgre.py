import redis
import datetime
import time 
import os 
import psycopg2

def datetimeToEpoch (timedate):
    epoch = (datetime.datetime.strptime(timedate, '%Y, %m, %d, %H, %M, %S, %f').timestamp()) * 1000
    return int(epoch)

def getStatusCodeDatabase (key, host, port):
    conn = psycopg2.connect(host=dbHost, port=dbPort, database=database)
    cursor = conn.cursor()
    cursor.execute(("select statuscode from statuscount where epochtime >= %s"), [1693603383383])
    records = cursor.fetchall()
    statusCodes = []
    for row in records: 
        statusCodes.append(row[0])
    conn.commit()
    cursor.close()
    conn.close()
    return statusCodes, cursor.rowcount

if __name__ == "__main__":
    dbHost = '127.0.0.1'
    dbPort = '5432'
    database = "statuscode"
    statusCode = getStatusCodeDatabase(dbHost, dbPort, database)
    print ("All status codes is: ", statusCode[0])
    print ("and total request with status code is: ",statusCode[1])
