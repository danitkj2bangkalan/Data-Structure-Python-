#advanced sorting(Divide and conquer)
#merge sort

def mergesort(a_list):
    print("Splitting", a_list)
    if len(a_list) >1:
        mid = len(a_list)//2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[K] = right_half[j]
                j +=1
            k +=1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i +=1
            k +=1
        while j < len(right_half):
            a_list[k] = right_half[i]
            j +=1
            k +=1
    print("Merging", a_list)

a=[10,11,34,2,4,5,1,78]
mergesort(a)
                

