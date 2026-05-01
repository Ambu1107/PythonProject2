#1.1.3 Days between Two Dates
from datetime import date
firstdate=list(map(int,input().split('-')))
seconddate=list(map(int,input().split('-')))
date1=date(firstdate[0],firstdate[1],firstdate[2])
date2=date(seconddate[0],seconddate[1],seconddate[2])
daysdiff=abs((date2-date1).days)
print(daysdiff)