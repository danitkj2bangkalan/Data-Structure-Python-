import Queue
def practice(nama,hitungan):
    q=Queue.createQueue()

    for i in range(hitungan):
        print(nama)
        for j in nama:
            p=Queue.enqueue(q,j)
    print(q)
    return(nama)
    
practice(['d','a','c','e'],5)
