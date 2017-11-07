import time
start = time.time()

d = {1:(2,1)}
n = 1
while(d[n][0] < 1000000000):
    n += 1
    d[n] = (d[1][0]*d[n-1][0] + 3*d[1][1]*d[n-1][1],
            d[1][0]*d[n-1][1] + d[1][1]*d[n-1][0])
  
da1 = {i:(2*d[i][0]+1)/3. for i in d if (2*d[i][0]+1)/3. == int((2*d[i][0]+1)/3.) and 2*d[i][0]+2 < 1000000000} 
da2 = {i:(2*d[i][0]-1)/3. for i in d if (2*d[i][0]-1)/3. == int((2*d[i][0]-1)/3.) and 2*d[i][0]-2 < 1000000000}
  
area1 = {i:(d[i][0]+2)*d[i][1]/3. for i in da1 if (d[i][0]+2)*d[i][1]/3. == int((d[i][0]+2)*d[i][1]/3.)}
area2 = {i:(d[i][0]-2)*d[i][1]/3. for i in da2 if (d[i][0]-2)*d[i][1]/3. == int((d[i][0]-2)*d[i][1]/3.)}  

s = sum([da1[i]*3+1 for i in area1 if area1[i] > 0])    
s += sum([da2[i]*3-1 for i in area2 if area2[i] > 0])

print s
print time.time() - start        