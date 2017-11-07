mdays = [31,28,31,30,31,30,31,31,30,31,30,31]
wdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

ys = 1900  #1900-1901-2000
ds = 1    #1-28,29,30,31
ms = 1   #1-12
dn = 1   #1-7
day = 1   #counter
ns = 0     #counter

df = 1     #stop
mf = 1    #stop
yf = 1901    #stop

while (ys != yf or ds != df or ms != mf):
  print(str(ms)+'-'+str(ds)+'-'+str(ys)+' Sundays = '+str(ns)) 
  day += 1
  dn += 1
  ds += 1 
  if dn == 7:
    if ds == 1:
      ns += 1   
    dn = 0

  if ds >= mdays[ms-1]:
    if ms == 2 and ys % 4 == 0: 
      if ds == 28:
        if ys % 100 == 0:
          if ys % 400 == 0:
            continue 
          else:
            ds = 0
            ms += 1
      else:
        ds = 0
        ms += 1
        if ms > 12:
          print(ys)
          ms = 1
          ys += 1

print(str(ms)+'-'+str(ds)+'-'+str(ys)+' Sundays = '+str(ns))    
