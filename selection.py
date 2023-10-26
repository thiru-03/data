def sort(alist):
    for i in range (0,len(alist)-1):
        minpos= i
        for j in range (i,len(alist)):
            if alist[j]<alist[minpos]:
              minpos= j
        temp=alist[i]
        alist[i]=alist[minpos]
        alist[minpos]=temp
alist =[5,7,2,1,3,4]
sort(alist)
print("sorted result :",alist)