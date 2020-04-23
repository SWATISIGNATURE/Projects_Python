"""
Insertion Sort:
    For any given array lets say [3,6,2,3,1,0,8]
    the 0th element is considered as a partition to create a sorted array on the left like : [3 | 6,2,3,1,0,8]
    one element is taken at a time : like 6 (1st element)
    6 is compared with 3: if less goes to left or right , result: [3 ,6 | 2,3,1,0,8]
    and so on it conitues:

1. Insertion sort occurs in place.
2. Time Complexity :
    Best case (assume the array is already sorted) => Omega(n)
    Worst Case (fully unsorted) => O(n**2)
    Avaergae case => Theta(n**2)

"""

Arr = [3,6,2,3,1,0,8]

#[6 | 3,2,3,1,0,8] => [3,6 || 2,3,1,0,8]

def quicksort(Arr):
    n = len(Arr)
    for i in range(1, n): # as we have nothing to do with the 0th element so just let it be
        j = i -1 #for i=1, j=0
        curr = Arr[i] #6
        #print(Arr[i],Arr[j]) #6,3
        while j >= 0 and Arr[j] > curr:
            Arr[j+1] = Arr[j]
            Arr[j] = curr
            j -= 1

        Arr[j+1] = curr


quicksort(Arr)
print(*Arr)




