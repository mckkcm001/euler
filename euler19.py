monlist = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 1900
day = 1
month = 1
name = 1
count = 0

while year!=2000 or day != 31 or month != 12:
  day += 1
  name += 1
  
  if name > 7:
    name = 1
    
  if day > monlist[month-1]:
    if month == 2:
      if day == 29 and year % 4 == 0 and (not year % 100 == 0):
        day = 29
        
      if day == 29 and not (year % 4 == 0):
        day = 1
        month = 3
        
      if day == 29 and year % 4 == 0 and year % 100 == 0 and (not year % 400 == 0):
        day = 1
        month = 3
        
      if day == 29 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        day = 29   
        
      if day == 30:
        day = 1
        month = 3
        
    else:
      day = 1
      month += 1
      
  if month > 12:
    month = 1
    year += 1
    
  if day ==1 and name == 7:
    count += 1
    
print(str(month)+'-'+str(day)+'-'+str(year)+'-'+str(name))
print(count)
