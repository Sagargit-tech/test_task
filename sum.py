
def sum(l):
  s=0
  for i in l :
     s=s+i
  print("sum=",s)
n=int(input("input the lenght of ur list"))
l=[]
for i in range(0,n):
   j= int(input())
   l.append(j)
sum(l)