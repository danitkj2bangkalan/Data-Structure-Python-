
#def bubblesort(listdata):
#    for outiter in range(len(listdata)-1,-1,-1):
#        for i in range(outiter):
#            if listdata[i]>listdata[i+1]:
#                #old school version
#                temp=listdata[i]
#                listdata[i]=listdata[i+1]
#                listdata[i+1]=temp
#                #old school version
#                #python version#listdata[i],lisdata[i+1]=listdata[i+1],listdata[i]
#            print(listdata)
#        print('iterasi ke- %d'%(i),'\ndata urut',listdata)
#a=[23,4,5,6,7,8,9,11,12,34,12]
#bubblesort(a)

#soal 
#ubahlah modifikasi  agar tidak ada iterasi mubazir dalam ite=rasi di buble sort
#ubahlah modifikasi mengguanakan dua pointer kiri dan kanan

#selection sort
#def alsort(listdata):
#    for outIter in range(len(listdata)-1):
#        minIndex=outIter
#        for i in range(outIter+1,len(listdata)):
#            if listdata[i]<listdata[minIndex]:
#                minIndex=i
#        temp=listdata[outIter]
#        listdata[outIter]=listdata[minIndex]
#        listdata[minIndex]=temp
#        print(listdata)
#    print('Data Urut=',listdata)

#a=[24,5,7,8,9,7,3]
#alsort(a)

#500 data random bandingkan waktu pengurutan antara buble dan selection

#def modul6(listdata):
#    urutan=0
#    for outIter in range(len(listdata)-1,-1,-1):
#        for i in range(outIter):
#            if listdata[i]>listdata[i+1]:
#                #old school version
#                temp=listdata[i]
#                listdata[i]=listdata[i+1]
#                listdata[i+1]=temp
#            else:
#                break
#                #old school version
#                #python version#listdata[i],lisdata[i+1]=listdata[i+1],listdata[i]
#            print(listdata)
#        urutan +=1
#        print('Iterasi ke -%d'%(urutan),'\nData urut',listdata)
#a=[10,2,4,5,8,1,20,2,2,4]
#modul6(a)



#dari yang terbesar selection sort


#buat dengan dua pointer kiri dan kanan
#def selection(listdata):
#    for outIter in range(len(listdata)-1,-1,-1):
#        maxIndex=outIter
#        for i in range(outIter):
#            if listdata[i]>listdata[maxIndex]:
#                maxIndex=i
#            elif listdata[i]<listdata[maxIndex]:
#                maxIndex=outIter
#            temp=listdata[outIter]
#            listdata[outIter]=listdata[maxIndex]
#            listdata[maxIndex]=temp
#            print('min='listdata)
#a=[10,2,0,9,3]
#alsort(a)


#def seq(x,s):
#    found=False
#    i=0
#    while not (found) and i <=len(x):
#        if x[i] == s:
#            found=True
#        else:
#            found=False
#        i+=1
#a=int(input('Masukkan bilangan yang  ingin dicari!='))
#seq(a,[54,26,93,17,77,31,44,55,20,65])

#def insertionSort(alist):
#   for index in range(1,len(alist)):

#     currentvalue = alist[index]
#     position = index

#     while position>0 and alist[position-1]>currentvalue:
#         alist[position]=alist[position-1]
#         position = position-1

#         print(alist)
#     alist[position]=currentvalue
#     print("Data sementara",alist)
#alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)

#def alsort(listdata):
#    for outIter in range(len(listdata)-1,-1,-1):
#        maxIndex=outIter
#        for i in range(outIter):
#            if listdata[i]>listdata[maxIndex]:
#                maxIndex=i
#        temp=listdata[outIter]
#        listdata[outIter]=listdata[maxIndex]
#        listdata[maxIndex]=temp
#        print(listdata)
#    print('Data Urut=',listdata)


###################################################################
#def modul6(alist):
#    urutan=0
#    bertukar = True
#    passnum = len(alist)-1
#    while passnum > 0 and bertukar:
#       urutan+=1
#       bertukar = False
#       print('Iterasi ke-%d'%(urutan))
#       for i in range(passnum):
#           if alist[i]>alist[i+1]:
#               bertukar = True
#               temp = alist[i]
#               alist[i] = alist[i+1]
#               alist[i+1] = temp
#               print(alist)
#       print("Data urut",alist) 
#       passnum = passnum-1

#alist=[10,1,3,11,12]
#modul6(alist)
#print(alist)

def modul7(alist):
    #print("No 1")
    #print("Data Awal=",alist)
    #urutan = 0
    #for outIter in range(len(alist)-1):
    #    minIndex=outIter
    #    urutan+=1
    #    for i in range(outIter+1,len(alist)):
    #        if alist[i]<alist[minIndex]:
    #            minIndex=i
    #    temp=alist[outIter]
    #    alist[outIter]=alist[minIndex]
    #    alist[minIndex]=temp
    #    print("Iterasi ke -%d :"%(urutan),alist)
    #print('Data Urut=',alist)
    #print('no 2')
    #produk gagal
    #print("Data Awal=",alist)
    #urutan = 0
    #perulangan = True
    #while perulangan:
    #    urutan+=1
    #    for j in range(len(alist)-1):
    #        minIndex=j
    #    for y in range(len(alist)-1,-1,-1):
    #        maxIndex=y
    #    for i in range(len(alist)-1):
    #        if alist[i]<alist[minIndex]:
    #            minIndex=i
    #        elif alist[i]>alist[maxIndex]:
    #            maxIndex=i
    #    print("Iterasi ke-%d:"%(urutan))
    #    tempj=alist[j]
    #    alist[j]=alist[minIndex]
    #    alist[minIndex]=tempj
    #    print("Urutan Data Minimal",alist)
    #    tempy=alist[y]
    #    alist[y]=alist[maxIndex]
    #    alist[maxIndex]=tempy
    #    print("Urutan Data Maxsimal",alist)

    #    if alist[1]>alist[0]:
    #        perulangan = False
    print("")
    for i in range(len(alist)//2):
        print("Iterasi ke -%d"%(i+1))
        Max=i
        Min=i
        for j in range(1,(len(alist)-1)-i):
            if alist[j]<alist[Min]:
                Min=j
            if alist[j]>alist[Max]:
                Max=j
        alist[i],alist[Min]=alist[Min],alist[i]
        print("Nilai Data Minimal = ",alist)
        alist[(len(alist)-1)-i],alist[Max]=alist[Max],alist[(len(alist)-1)-i]
        print("Nilai Data Maksimum = ",alist)
    print("Data Urut=",alist)
alist=[10,2,5,8,1,20,7,12,4]
modul7(alist)
