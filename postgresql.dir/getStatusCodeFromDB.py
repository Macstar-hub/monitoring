import redis
import datetime
import time 
import os 
import psycopg2

def datetimeToEpoch (startTimeDate):
    epoch = (datetime.datetime.strptime(startTimeDate, '%Y, %m, %d, %H, %M, %S, %f').timestamp()) * 1000
    return int(epoch)

def getStatusCodeDatabase (key, host, port, startTimeDate):
    conn = psycopg2.connect(host=dbHost, port=dbPort, database=database)
    cursor = conn.cursor()
    cursor.execute(("select statuscode from statuscount where epochtime >= %s"), [datetimeToEpoch(startTimeDate)])
    records = cursor.fetchall()
    statusCodes = []
    for row in records: 
        statusCodes.append(row[0])
    statusCodeUniq = set(statusCodes)
    for status in statusCodeUniq:
        print ("status count: ", status, statusCodes.count(status))
    conn.commit()
    cursor.close()
    conn.close()
    return statusCodes, cursor.rowcount

if __name__ == "__main__":
    startTimeDate = '2023, 9, 1, 05, 15, 00, 000'
    dbHost = '127.0.0.1'
    dbPort = '5432'
    database = "statuscode"
    statusCode = getStatusCodeDatabase(dbHost, dbPort, database, startTimeDate)
    #print ("All status codes is: ", statusCode[0])
    print ("and total request with status code is: ",statusCode[1])
