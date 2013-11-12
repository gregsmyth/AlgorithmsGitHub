# Greg Smyth
# 13th October 2013
# Insertion sort algorithm
# Based on section 2.1 in Algorithms (3rd ed) Cormen et al 2009
# insertion_sort.py


numbers = [2000,1943, 33, 4, 66, 827, 0, 5,2,4,6,1,3]

for j in range(1,len(numbers)):
    print numbers
    currentNumber = numbers[j]

    #insert numbers[j] into the sorted sequence numbers[1... j-1]
    i = j - 1
    while i > -1 and numbers[i] > currentNumber:
        numbers[i + 1] = numbers[i]
        i = i - 1
        numbers[i + 1] = currentNumber

print "This is the sorted array ", numbers
