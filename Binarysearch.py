print("Binary search")
print("1 non-recursive")
print("2 recursive")
y=int(input("enter your choice:"))
if y==1:
  def binsearch(l,low,high,key):
    while low<=high:
       mid=(low+high)//2
       if l[mid]==key:
         return mid
       elif l[mid]>key:
         high=mid-1
       else:
         low=mid+1
    return -1
else:
  def binsearch(l,low,high,key):
    if low<=high:
       mid=(low+high)//2
       if l[mid]==key:
         return mid
       elif l[mid]>key:
         return binsearch(l,low,mid-1,key)
       else:
         return binsearch(l,mid+1,high,key)
    else:
       return -1
l=[]
n=int(input("enter size of list:"))
low=0
high=n-1
for i in range(n):
   ele=int(input("enter element:"))
   l.append(ele)
print(l)
key=int(input("enter key:"))
res=binsearch(l,low,high,key)
if res==-1:
  print("element not found")
else:
  print("element found at",res)