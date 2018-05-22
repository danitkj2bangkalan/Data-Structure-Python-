#queues(antrian) 
#pointernya menggunakan front dan rear FiFo(first in first out) berbeda dengan stack yang menggunakan 1 pointer yaitu, top of the stack
#operasi pada queues
#   queue(), inisialisasi struktur data queue kosong
#   enqueue (data), penambahan data baru pada queue
#   isEmpty(), pengecekan apakah queue dalam keadaan kosng
#   dequeue(), penghapusan data
#   size(), informasi jumlah data yang terdapat pada queue

def createQueue():
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

'''q=createQueue()
enqueue(q,'matematika')
enqueue(q,'struktur data')
enqueue(q,'bahasa inggris')
enqueue(q,'pemrograman web')
print(q)
dequeue(q)
print(q)
enqueue(q,dequeue(q))
print(q)
a=dequeue(q)
print(a,q)
enqueue(q,'new')
print(q)
isEmpty(q)
print(q)
size(q)
print(q)'''






