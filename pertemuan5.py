#queues(antrian) 
#pointernya menggunakan front dan rear FiFo(first in first out) berbeda dengan stack yang menggunakan 1 pointer yaitu, top of the stack
#operasi pada queues
#   queue(), inisialisasi struktur data queue kosong
#   enqueue (data), penambahan data baru pada queue
#   isEmpty(), pengecekan apakah queue dalam keadaan kosng
#   dequeue(), penghapusan data
#   size(), informasi jumlah data yang terdapat pada queue

def Queue():
    q=[]
    return(q)

def enqueue(q,data):
    q.insert(0,data)
    return(q)

def dequeue(q):
    data=q.pop()
    return(data)

def isEmpty(q):
    return(q==[])

def size(q):
    return(len(q))

#q=Queue()
#enqueue(q,'matematika')
#enqueue(q,'struktur data')
#enqueue(q,'bahasa inggris')
#enqueue(q,'pemrograman web')
#print(q)
#dequeue(q)
#print(q)
#enqueue(q,dequeue(q))
#print(q)
#a=dequeue(q)
#print(a,q)
#enqueue(q,'new')
#print(q)
#isEmpty(q)
#print(q)
#size(q)
#print(q)

#def penjadwalancpu(a,b):
#    q = Queue ()
#    for i in a:
#        enqueue(q,i)
#    print('waktu proses cpu =',b)
#    print('antrian proses :',q)
#    i=0
#    while not isEmpty(q):
#        print("iterasi ke- %d"%(i+1))
#        c=dequeue(q)
#        c[1]-=b
#        if c[1] > 0:
#            print("      proses",c[0],"sedang diproses, waktu proses",c[0],"=",a[1])
#            enqueue(q,c)
#        elif c[1] < 0:
#            print("      proses",c[0],"telah selesai,")
#        print('         data yang tersisa : ',q)
#        i=i+1
#b=int(input('masukkan jumlah proses di cpu :'))
#temp=[]
#for i in range(b):
#    temp1=[]
#    a=input('nama proses di cpu ke-%d : '%(i)).upper()
#    proses=int(input("waktu prosesnya : "))
#    temp1.append(a)
#    temp1.append(proses)
#    temp.append(temp1)
#f=int(input('lama waktu proses = '))
#penjadwalancpu(temp,f)

#def ularnaga(hitungan):
#    q = Queue()
#    enqueue(q,'c#')
#    enqueue(q,'c++')
#    enqueue(q,'java')
#    waktuproses=int(input('Waktu proses : '))
#    print('Antrian Proses:\n',q)
#    list=True
#    while list:
#        for i in range(waktuproses):
#            enqueue(q,dequeue(q))
#            print('iterasi ke- %d:'%(i))
#            print('Data Proses yang tersisa:',q)
#        eliminasi=dequeue(q)
#        if len(q) == 1:
#            list = False
#            print('yang tereliminasi adalah =',eliminasi)
#            print('isi terakhir di queue',q)
#        else:
#             print('yang tereliminasi adalah =',eliminasi)
#angka=int(input('Jumlah Proses yang akan dijadwalkan di CPU = '))
#ularnaga(angka)









