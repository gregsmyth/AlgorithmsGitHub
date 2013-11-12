# Greg Smyth
# 13th October 2013
# Merge sort algorithm
# Based on section 2.3 in Algorithms (3rd ed) Cormen et al 2009
# merge_sort.py
#
# random_ints used for testing
# written by bvdet and posted on
# http://bytes.com/topic/python/answers/829129-generate-random-list-integers
# last accessed 13th Oct 2013



import random
def random_ints(num, lower=0, upper=9999):
    ints = []
    for i in range(num):
        ints.append(random.randrange(lower,upper+1))
    return ints

# Main code starts
# Written by GS
# Use while loops instead of for(range) as produced indexing errors

def merge(numbers, start, middle, end):

    size1 = middle - start + 1
    size2 = end - middle
    numbersFirstHalf = []
    numbersSecondHalf = []

    i=1
    while i <= size1:
        numbersFirstHalf.append(numbers[start + i - 2])
        i+=1
        

    j=1
    while j <=size2:
        numbersSecondHalf.append(numbers[middle + j -1])
        j+=1

    numbersFirstHalf.append(float("inf"))
    numbersSecondHalf.append(float("inf"))
    
    i = 0
    j = 0


    k=start

    while k <= end:
        if numbersFirstHalf[i] <= numbersSecondHalf[j]:
            numbers[k-1] = numbersFirstHalf[i]
            i += 1
        else:
            numbers[k-1] = numbersSecondHalf[j]
            j += 1
        k+=1


    return numbers

def mergeSort(numbers, start, end):
    if start < end:
        middle = (start + end) / 2
        mergeSort(numbers, start, middle)
        mergeSort(numbers, middle + 1, end)
        merge(numbers, start, middle, end)

    return numbers
        
numbers = random_ints(10)
print "Unsorted numbers: ", numbers
mergeSort(numbers, 1, len(numbers))
print "Sorted numbers:   ", numbers
