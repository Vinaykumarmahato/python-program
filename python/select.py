# selection sort in python



from platform import java_ver


def selectionSort(a):
    for i in range(a):
        mini=i
        
        for j in range(i+1,len(a)):
            if a[j] < a[mini]:
                mini=j
                temp=a[i]
                a[i]=a[mini]
                a[mini]=temp
                print(a)
                a=[4,3,0,2]
                selectionSort(a)