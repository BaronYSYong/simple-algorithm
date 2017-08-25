"""
Reference: 
    http://www.geeksforgeeks.org/quick-sort/
    http://www.geeksforgeeks.org/heap-sort/
"""

import random
import time

class Sorting(object): 
    def partition(self, arr,low,high):
        """
        This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot)
        to left of pivot and all greater elements to right
        of pivot
        """        
        i = ( low-1 )         # index of smaller element
        pivot = arr[high]     # pivot     
        for j in range(low , high):     
            # If current element is smaller than or
            # equal to pivot
            if   arr[j] <= pivot:             
                # increment index of smaller element
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]     
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )
     
    def quickSort(self, arr,low,high):
        """
        The main function that implements QuickSort
        arr[]: Array to be sorted,
        low: Starting index,
        high: Ending index    
        """
        if low < high:     
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr,low,high)     
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

    def bubbleSort(self, arr):
        n = len(arr)     
        # Traverse through all array elements
        for i in range(n):     
            # Last i elements are already in place
            for j in range(0, n-i-1):     
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def heapify(self, arr, n, i):
        """
        To heapify subtree rooted at index i.
        n is size of heap        
        """
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l     
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r     
        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]  # swap     
            # Heapify the root.
            self.heapify(arr, n, largest)
     
    def heapSort(self, arr):
        n = len(arr)     
        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)     
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # swap
            self.heapify(arr, i, 0)
 
if __name__ == '__main__':
    arr1 = arr2 = arr3 = [random.randint(0,999999) for r in range(100000)]
    sorting = Sorting()
    
    start = time.time()
    sorting.quickSort(arr1,0,len(arr1)-1)
    quick_time = time.time() - start
    
    start = time.time()
    sorting.bubbleSort(arr2)
    bubble_time = time.time() - start
    
    start = time.time()
    sorting.heapSort(arr3)
    heap_time = time.time() - start
    
    #~ print ("Sorted array is:")
    #~ for i in range(len(arr1)):
        #~ print ("%d" %arr1[i]),

    print ("quickSort: %f seconds" %quick_time)
    print ("bubbleSort: %f seconds" %bubble_time)
    print ("heapSort: %f seconds" %heap_time)
