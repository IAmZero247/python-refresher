import time as t
import datetime as dt
import pytz
## In python the date is not a data type, but date object


#1) time module -> Seconds after 12 am  1st Jan 1970
print("Seconds after 12 AM 1st Jan 1970 ->" ,t.time())

#2) datetime -> Current date and time
dto = dt.datetime.now()
print("Current date and time ->" , dto )

print( "Day: {} ,  Month: {} ,  Year {} ".format(dto.day, dto.month, dto.year))
print( "Hr: {} ,  Min: {} ,  Sec {} ".format(dto.time().hour, dto.time().minute, dto.time().second))


#3) Datetime object represent a date

dto_date = dt.date(2021,6,22)
print("dto_date ->", dto_date)



#4) Get date from timestamp (UTC , Universal time cordinated)
utc_time = 1624779290.7954447
date_from_utc = dt.date.fromtimestamp(utc_time)
print ("Date converted from UTC ->" , date_from_utc )



#5) Get today
today = dt.date.today()
print("Today ->", today)
print(today.year)
print(today.month)
print(today.day)

#6) Timedelta:

t1 = dt.date(2021, 6, 21)
t2 = dt.timedelta(15)
print("TimeDelta Sample",t1 - t2)

#7)StringFormatTime strftime()
#**** strftime() method is defined under classes date, datetime & time.
#**** The method creates a formatted string from a given date.

curr_time = dt.datetime.now()
print(curr_time)
format_time1 = curr_time.strftime("%Y/%m/%d")
format_time2 = curr_time.strftime("%H:%M:%S")
print("format_time1 -> ",format_time1)
print("format_time2 -> ",format_time2)
format_IST = curr_time.strftime("%d-%m-%Y")
print("IST Date Format: ", format_IST)


#8)StringParseTime strptime() -> string to datetime.
#**** strptime() method creates a datetime object from a given string.

dt_str = "26 June 2021"
print("String Date Received -> ", dt_str)

dt = dt.datetime.strptime(dt_str, "%d %B %Y")
print("DateTime Object -> " , dt)


#9) TimeZone
#**** Third party module: pytz
#**** validate installation -> pip freeze grep pytz

UTC = pytz.utc
format ='%Y:%m:%d %H:%M:%S %Z %z'
AS_KO = pytz.timezone('Asia/Kolkata')
AM_NY = pytz.timezone('America/New_York')
AF_MA = pytz.timezone('Africa/Maseru')
US_CE = pytz.timezone('US/Central')
EU_AT = pytz.timezone('Europe/Athens')

from datetime import datetime

dt_Kl = datetime.now(AS_KO) # not sure why dt.datetime.now(AS_KO) throws error
dt_Ny = datetime.now(AM_NY)
dt_Ma = datetime.now(AF_MA)
dt_Ce = datetime.now(US_CE)
dt_At = datetime.now(EU_AT)
dt_Ln = datetime.now(pytz.timezone("Europe/London"))

utc_Kl = dt_Kl.astimezone(UTC)
utc_Ny = dt_Ny.astimezone(UTC)
utc_Ma = dt_Ma.astimezone(UTC)
utc_Ce = dt_Ce.astimezone(UTC)
utc_At = dt_At.astimezone(UTC)
utc_Ln = dt_Ln.astimezone(UTC)


header = ["ZoneFormat", "Date & Time Formatted" , "Date & Time Formatted wrt UTC" ,"IST"]
print("{0:^32s}   | {1:^30s}  |  {2:^30s} |  {3:^30s}".format(header[0], header[1], header[2] , header[3] ))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_Kl.__str__(), dt_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_Ny.__str__(), dt_Ny.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Ny.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_Ma.__str__(), dt_Ma.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Ma.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_Ce.__str__(), dt_Ce.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Ce.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_At.__str__(), dt_At.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_At.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))
print("{0:<30s}   | {1:<30s}  | {2:<30s}  |  {3:^30s}".format(dt_Ln.__str__(), dt_Ln.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Ln.strftime('%Y:%m:%d %H:%M:%S %Z %z'), utc_Kl.strftime('%Y:%m:%d %H:%M:%S %Z %z')))





