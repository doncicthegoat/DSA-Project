
def merge_lists(lst1, lst2):
    i, j = 0, 0
    new_lst = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            new_lst.append(lst1[i])
            i += 1
        else:
            new_lst.append(lst2[j])
            j += 1

    new_lst.extend(lst1[i:])
    new_lst.extend(lst2[j:])

    return new_lst


def merge_sort(lista):
    m=len(lista)//2
    list1 = lista[:m]
    list2 = lista[m:]


    if len(lista) <= 1:

        return lista

    temp2=merge_sort(list1)
    temp3=merge_sort(list2)

    return merge_lists(temp2,temp3)


def heapify(lst, i, max_index = None):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if max_index is None:
        max_index = len(lst)

    if left < max_index and lst[left] > lst[largest]:
        largest = left
    if right < max_index and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, largest,max_index)

    return lst


def heap_sort(lst):
    #Building Max Heap

    for i in range((len(lst)-1)//2,-1,-1):
        heapify(lst,i)


    for j in range(len(lst) - 1, -1, -1):
        lst[0],lst[j] = lst[j],lst[0]
        heapify(lst,0, j)

    return lst




def search(lst,num,index = 0):
    m = len(lst)//2
    right=lst[m:]
    left=lst[:m]


    if lst[0] >= num:
        return index
    elif lst[-1] <= num:
        return len(lst)+index
    elif right[0] <= num:
        return search(right,num,index+len(left))
    elif left[-1] >= num:
        return search(left,num,index)
    else:
        return index + len(left)


def binary_insertion_sort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        pos = search(lst[:i],key)
        j = i
        while j != pos and j-1>=0:
            lst[j] = lst[j-1]
            j -=1
        lst[pos] = key
    return lst

def quick_sort(lst):

   # Base case: lists with 0 or 1 element are already sorted
   if len(lst) <= 1:
       return lst


   # Choose pivot (here we choose the middle element to avoid worst-case with already sorted arrays)
   pivot_idx = len(lst) // 2
   pivot = lst[pivot_idx]


   # Partition the array
   left = [x for x in lst if x < pivot]  # Elements less than pivot
   middle = [x for x in lst if x == pivot]  # Elements equal to pivot
   right = [x for x in lst if x > pivot]  # Elements greater than pivot


   # Recursively sort the partitions and combine them
   return quick_sort(left) + middle + quick_sort(right)
