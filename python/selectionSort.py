# selection sort in python

from array import array


def selectionSort(arr,size):
    for step in range(size):
        mid_ind=step
        
        for i in range(step + 1 , size):
            if array[i] <array[min_idx]:
                min_idx = 1
                (array[step],array[min_idx]) = (array[mid_ind], array[step])
                data = [35,1,58,78,69,54]
                size=len(data)
                selectionSort(data,size)
                print("sorted array in accending order")
                print(data)