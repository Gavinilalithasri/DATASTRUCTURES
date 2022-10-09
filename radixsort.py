def countingsort(arr,exp):
  n=len(arr)
  output=[0]*(n)
  count=[0]*10
  for i in range(0,n):
    index=arr[i]/exp
    count[int (index%10)]+=1
  for i in range(1,10):
    count[i]+=count[i-1]
  i=n-1
  while i>=0:
    index=arr[i]/exp
    output[count[int(index%10)]-1]=arr[i]
    count[int (index%10)]-=1
    i-=1
  i=0
  for i in range(0,len(arr)):
    arr[i]=output[i]
def radixsort(arr):
  max1=max(arr)
  exp1=1
  while(max1/exp1)>0:
    countingsort(arr,exp1)
    exp1*=10
arr=[]
n=int(input("enter size of array:"))
for i in range(n):
  ele=int(input("enter element:"))
  arr.append(ele)
radixsort(arr)
print(arr)