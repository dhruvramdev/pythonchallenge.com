import calendar
import datetime


i= 1999

while i > 999 :
    if calendar.isleap(i):
        if datetime.date(i , 2 , 29).weekday() == 6:
            if i % 10 == 6 :
                print i

        

    i -= 1

##WE GET
##    1976
##    1756
##    1576
##    1356
##    1176
##
##Second YOungest is 1756

##Search for 27th January 1756
