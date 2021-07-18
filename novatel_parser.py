#! /usr/bin/env python3
"""

"""

import os
import time
from os.path import expanduser
# from datetime import datetime
import csv
import datetime, calendar   

def weeksecondstoutc(gpsweek,gpsseconds,leapseconds):
    datetimeformat = "%Y-%m-%d %H:%M:%S"
    epoch = datetime.datetime.strptime("1980-01-06 00:00:00",datetimeformat)
    elapsed = datetime.timedelta(days=(gpsweek*7),seconds=(gpsseconds+leapseconds))
    raw_time = epoch + elapsed
    return [raw_time.timestamp(),datetime.datetime.strftime(raw_time,datetimeformat)]

log_filename = '/home/user1/Projects/USAR_GPS_Study/20210714_DataR1/DMMU20040148C_14-07-2021_17-35-40.gps'

with open(log_filename, 'r') as log_file:            
    for line in log_file:
        if line.startswith('#BESTPOSA'):
            header = line.split(';')[0].split(',')
            message = line.split(';')[1].split(',')
            #message_time = timeconvert24(float(header.split(',')[6]))
            message_epoch,message_time = weeksecondstoutc(int(header[5]),float(header[6]),0)
            print(message_epoch,message_time,header)
            print(message)

'''

header: Message_type, Port,    Seq#, Idle_time, Time_Status,  Week, Seconds,    Rcvr_Status  Reserved  S/W Version
        BESTPOSA,     ICOM1_1, 0,    61.0,      FINESTEERING, 2166, 337014.000, 02000000,    b1f6,     15990
        
message: SolStat,     Pos Type,      Lat,            Lon,            Hgt,       Undulat, Datum  LatDev, LonDev  HgtDev, BaseID, diffAge, SolAge, #SV, #SVSol l1, Ms, Rs, Stat, OthrUsed, GpsMask, crc
        SOL_COMPUTED, INS_RTKFIXED, 41.38021433223, -73.97238983324, 227.8666, -32.3000, WGS84, 0.0083, 0.0076, 0.0104, "0",    1.000,   0.000,  11,  8,     8,  8,  00, 20,00,03*16dc6888
        
TimeStamp,HumanTime,PosType,Lat,Lon,Hgt,
'''                


#if __name__ == "__main__":

#    log_dir = '/home/user1/PC21_Collect/Archive/HarveyLogs/APM/LOGS/'
#    filename = log_dir + "00000010.BIN"
#    convert_gps_bin(filename)


'''
#BESTPOSA,ICOM1_1,0,61.0,FINESTEERING,2166,337014.000,02000000,b1f6,15990;SOL_COMPUTED,INS_RTKFIXED,41.38021443130,-73.97238982565,227.8822,-32.3000,WGS84,0.0082,0.0073,0.0103,"0",1.000,0.000,13,8,8,8,00,21,00,03*6ecd68a1

'''
