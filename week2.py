#a=[[1,2,3],[4,5,6]]
#b=[[2,3,7],[0,8,1]]
#def penjumlahan_matrik(a,b):
#    lis=[]
#    for i in range(2):
#        lis1=[]
#        for j in range(3):
#            hasil[i][j]=a[i][j]+b[i][j]
#            lis1.append(hasil)
#        lis.append(lis1)

#studentData={}
#studentData['001']:"sadad"
#studentData['002']:"qfrf"
#studentData['003']:"ewrh"
#studentData['003']:"rewr"

#a={(0,0):1,(0,1):2,(0,2):3,(1,0):4,(1,1):5,(1,2):6}
#b={(0,0):2,(0,1):3,(0,2):7,(1,0):0,(1,1):8,(1,2):1}

#hasil={}
#for i in range(2): #baris
#    for j in range(3): #kolom
#        hasil[i,j]=a[i,j]+b[i,j]
#print(hasil)

a={(0,3):1,(2,1):2,(3,3):3}
b={(0,1):3,(2,1):5}
hasil={}
for i in range(4):
    for j in range(4):
        if a.get((i,j),0)!=0 and b.get((i,j),0)!=0:
            hasil[i,j]=a[i,j]+b[i,j]
        if a.get((i,j),0)!=0 and b.get((i,j),0)==0:
            hasil[i,j]=a[i,j]
        if a.get((i,j),0)==0 and b.get((i,j),0)!=0:
            hasil[i,j]=b[i,j]
        
print(hasil)



        
