# Greg Smyth
# 13th October 2013
# Merge function
# Based on p31 in Algorithms (3rd ed) Cormen et al 2009
# merge.py

def merge(A,p,q,r):

    n1 = q - p + 1
    n2 = r - q

    for i in range(1,n1):
        list1[i]=A[p+i-1]

    for j in range(1,n2):
        list2[j]=A[q+j]

    list1[n1+1]=infinity
    list2[n2+1]=infinity
    i=1
    j=1

    for k in range(p,r):
        if list1[i]<=list2[j]:
            A[k]=list1[i]
            i+=1
        else:
            A[k]=list2[j]
            j+=1

    return A


