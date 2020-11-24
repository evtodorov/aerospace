# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:15:35 2014

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author: etodorov
"""
from copy import deepcopy
year = []
for i in xrange(1,13):
    if(i==4 or i==6 or i==9 or i==11):
        year.append([i]+range(1,31))
    elif(i==2):
        year.append([i]+range(1,29))
    else:
        year.append([i]+range(1,32))
century = []
lyear = deepcopy(year)
lyear[1].append(29)
for j in xrange(1900,2001):
    if(j%100==0 and j%400!=0):
        century.append([j]+year)
    elif(j%4==0):
        century.append([j]+lyear)
    else:
        century.append([j]+year)
calendar = []
sundays = 0
day = 1
yearN = 1900
for yr in century:
    y = [yearN]
    yearN += 1
    monthN = 0
    for month in yr[1:]:
        monthN +=1
        m = [monthN]
        for date in month[1:]:
            if(day==8): day = 1
            #date, day of week
            m.append((date,day))
            if(yr[0]>=1901 and date==1 and day==7): sundays += 1
            day +=1
        y.append(m)
    calendar.append(y)
print sundays