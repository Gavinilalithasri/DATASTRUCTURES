def Insertion(a):
     
   for i in range(1,len(a)):
        
         j=i-1
        
         nxtele=a[i]
        
         while(a[j]>nxtele and j>=0):
            
              a[j+1]=a[j]
            
              j=j-1
        
         a[j+1]=nxtele
    
   print(a)  

n=int(input("enter size of array:")) 

arr=[]
for i in range(n):
    
    ele=int(input("enter element:"))
    
    arr.append(ele)
Insertion(arr)