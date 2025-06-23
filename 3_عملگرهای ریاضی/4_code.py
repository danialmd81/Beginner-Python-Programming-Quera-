num = int(input())
h=num/3600
h=int(h)
num=num-h*3600
m=num/60
m=int (m)
s=num%60
print (h,end=" : ")
print (m,end=" : ")
print (s)