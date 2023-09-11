import datetime

def dateTimeToEpoch (timeDate):
    epoch = (datetime.datetime.strptime(timeDate, '%Y, %m, %d, %H, %M, %S, %f').timestamp()) * 1000
    return int(epoch)

if __name__ == '__main__':
    startTimeDate = '2023, 1, 1, 0, 0, 2, 714'
    endTimeDate   = '2023, 1, 1, 0, 0, 2, 714'
    startEpoch = dateTimeToEpoch(startTimeDate)
    endEpoch = dateTimeToEpoch(endTimeDate)
    print ("startEpoch: " + str(startEpoch), "endEpoch: " + str(endEpoch))
