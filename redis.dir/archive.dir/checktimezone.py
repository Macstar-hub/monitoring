def currentHourEpoch (currentDateTime):
    import datetime 
    currentHourEpoch = datetime.datetime(currentDateTime.year, currentDateTime.month, currentDateTime.day, currentDateTime.hour, 00, 00).timestamp()
    return currentHourEpoch

def tsChecker (epoch):
    from datetime import datetime
    currentDateTime = datetime.now()
    currentTime = currentDateTime.time()
    epochDateTime = datetime.fromtimestamp(epoch/1000)
    if epochDateTime.hour == currentTime.hour:
        print ("getTimeSpan()")
    else:
        currentHourEpoch2 = currentHourEpoch(currentDateTime)
        print (epochDateTime.hour, "current epoch time hour", currentHourEpoch2)
    return currentTime.hour

if __name__ == "__main__":
    #epoch = 1693604054934
    epoch = 1693600800000 
    now = tsChecker(epoch)
    print (now)
