#interactive python

#unordersequential
#def sequentialSearch(alist, item):
#	    index = 0
#	    found = False
	
#	    while index < len(alist) and not found:
#	        if alist[index] == item:
#	            #found = index
#                found = True
#	        else:
#	            index += 1
	
#	    return found
	
#testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#print(sequentialSearch(testlist, 13))

#ordersequential

#def orderedSequentialSearch(alist, item):
#	    pos = 0
#	    found = False
#	    stop = False
#	    while pos < len(alist) and not found and not stop:
#	        if alist[pos] == item:
#	            found = True
#	        else:
#	            if alist[pos] > item:
#	                stop = True
#	            else:
#	                pos = pos+1
	
#	    return found
	
#testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#print(orderedSequentialSearch(testlist, 3))
#print(orderedSequentialSearch(testlist, 13))

#binary search

#def binarySearch(alist, item):
#	    first = 0
#	    last = len(alist)-1
#	    found = False
#	    while first<=last and not found:
#	        midpoint = (first + last)//2
#	        if alist[midpoint] == item:
#                # for searching index
#                #found = midpoint
#	            found = True
#	        else:
#	            if item < alist[midpoint]:
#	                last = midpoint-1
#	            else:
#	                first = midpoint+1
	
#	    return found
	
#testlist = [4,6,10,34,56,78,99]
#print(binarySearch(testlist, 78))

#biinary search with recursive methode

#def binarsearchingrecursive(listdata,data):
#    if len(listdata) == 0:
#        return False
#    else:
#        midpoint = len(listdata)//2
#        if listdata[midpoint] == data:
#            return midpoint
#        else:
#            if data < listdata[midpoint]:
#                last=midpoint - 1
#                return binarsearchingrecursive(listdata,data,first,last)
#            else:
#                first= midpoint + 1
#                return binarsearchingrecursive(listdata,data,first,last)
#a=[4,6,10]
#binarsearchingrecursive(a,10)

#hasing

#def putdata(data):
#    table=[]
#    hasilremainder= remainder()
#    for i in range(data):
#        table.append(i)
#    return table[data]

#def createhastable(size):
#    hastable=[]
#    for i in range(size-1):
#        hastable.append(None)
#    return hastable

#createhastable(11)
#def remainder(data,n):
#    hasil=data%n
#    return hasil

###########################################################################modul8################################################################

#def modul8seq(daftar,cari):
#    q=[]
#    pos=0
#    found = False
#    jumlah= -1
#    while pos<len(daftar)-1 and not found:
#        jumlah += 1
#        if daftar[pos] == cari:
#            found =True
#            q.append(pos)
#        else:
#            pos += 1
#    print('Posisi Data =',q)
#    print('Jumlah Iterasi =',jumlah)
#a=[1,5,9,8,1,5,10,26,5,12]
#modul8seq(a,26)

#def modul8unorseq(alist, item):
#    q=[]
#    pos = 0
#    found = False
#    stop = False
#    jumlah = -1
#    while pos < len(alist) and not found and not stop:
#        jumlah+=1
#        if alist[pos] == item:
#            found = True
#            q.append(pos)
#        else:
#            if alist[pos] > item:
#                stop = True
#            else:
#                pos += 1
#    print('posisi Data=',q)
#    print('Jumlah Iterasi=',jumlah)
              
#a=[1,2,3,4,5,6,7,9,12]
#modul8unorseq(a,12)

#def modul8bin(alist,item):
#    q=[]
#    jumlah = 0
#    first = 0
#    last = len(alist)-1
#    found = False
#    while first<=last and not found:
#        jumlah +=1
#        midpoint = (first + last)//2
#        if alist[midpoint] == item:
#            q.append(midpoint +1)
#            found = True
#        else:
#            if item < alist[midpoint]:
#                last = midpoint-1
#            else:
#	            first = midpoint+1
#    print("posisi Data=",q)
#    print("Jumlah Iterasi =",jumlah)
#a=[1,2,3,4,5,6,7,9,12]
#modul8bin(a,2)

#########################################################
#hashing
#def remainder():


#def hashfunction(n,mod):
#   n*=n
#   n=str(n)
#   m=(len(n)-1)//2
#   if len(n)%2 != 0:
#       a=n[m]
#       n=a
#   elif len(n)%2 == 0:
#       a=n[m:m+2]
#       n=a
#   n=int(n)
#   n%mod
#   return n
#print(hashfunction(9,2))

#def midsqfunction(data,num):
#    temp*=data
#    if len(stry(temp))<3:
#        return(temp%num)
#    else:
#        a=str(temp)
#        a=a[1:len(a)-1]
#        return(int(a))%num

#def putData2(a,hastable,functionName):
#    for i in range(len(a)):
#        if functionName == 'reminder':
#            ind=remainderFunction(a[i],len(hastable))
#        elif functionName=='midsq':
#            ind=midsqfunction(a[i],len(hastable))
#        hastable[ind]=a[i]
#    return(hastable)

##linear problem
#def linearprobling(ind,hashTable,data):
#    count=ind
#    found=False
#    while (count!=0) and not found:
#        if hashTable[count]=='none':
#            found=True
#            hashTable[count]=data
#        else:
#            count+=1
#            if count==len(hashTable)-1:
#                count=0
#    return(hashTable)
#buat methode channing structure data hashing

#modul9
def remainderFunction(data,mod):
    hasil=data%mod
    return(hasil)
slot=remainderFunction(5,10)
print(slot)

def createHashTable(angka):
    table=[]
    for i in range(angka):
        temp=[]
        temp.append(None)
        table.append(temp)
    return(table)
hashtable=createHashTable(11)
print(hashtable)

def chainning(angka,mod):
    table=hashtable
    ind=angka%mod
    temp=[]
    for i in range(11):
        if i == ind:
            temp.append(angka)
        else:
            table.append(angka)
        table.append(temp)
    return(table)
a=[54,26,93,17,77,31,44,55,20]
chain=chainning(a,11)
print(chain)

def searchHash(angka,data):
    alist=data
    index = 0
	found = False
	while index < len(alist) and not found:
        if alist[index] == angka:
            found = True
            print('data berada di slot ke-,%d, dan index ke -, %d',%(index,angka))
	    elif:
            index += 1
        else:
        return (False)

hashTable = chain
searchHash(20,hashTable)
