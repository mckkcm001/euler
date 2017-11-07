import math # just in case
# a is given--I should write a script to import it from a file rather than manually inserting commas and brackets
with open('triangle.txt') as tri:
  b = tri.readlines()

a = [[]]

for i in range(0,len(b)):
  a[i] = b[i].split()

print(a[0])
print(a[1])
#I still don't understand how to build the array one element at a time, so I just made a copy of a. However, I can't just do c = a, because I need a separate set of numbers since c is going to change, but a is not
c = [[]]
c = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]
#The idea is to replace each member in c with the maximum total up to that point. Every path starts at 75. The next two possibilities are 75 + 95 and 75 + 64. The possibilities in each row are calculated from the one or two paths leading to the element in a row. The edge elements only have one path, so test to see if on the edge. If not on the edge, then replace the element with the max of the two possibilities. Then, when you get to the bottom, the maximum in the last row must be the overall maximum. I don't know the path, but I do know the maximum.
for i in range(1,len(a)):# this loops through the rows--after each row is processed, c contains the maximum possibilites for that row
  for j in range(0,len(a[i])):
    if j == 0: # if at left edge, only one possibility, i is this row, i-1 is previous row, j is element in row
      c[i][j] = a[i][j]+c[i-1][j]
    if j == len(a[i])-1: # if at right edge, only one possibility
      c[i][j] = a[i][j]+c[i-1][j-1]
    else: # not at either edge, so only keep the max of two possibilities
      c[i][j] = max(a[i][j]+c[i-1][j],a[i][j]+c[i-1][j-1])
#print out result--max of last row
print(max(c[len(a)-1]))
