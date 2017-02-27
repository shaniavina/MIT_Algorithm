def partition(A, p, q, pivot=None):
    if pivot:
        A[p], A[pivot] = A[pivot], A[p]
    i = p
    print(A, p, q, pivot)
    for j in range(p + 1, q):
        if A[j] <= A[p]:
            i += 1
            A[i], A[j] = A[j], A[i]
    print(A, i)
    A[i], A[p] = A[p], A[i]
    return i


def quicksortHelper(A, p, q):
    if q - p <= 1:
        return
    r = partition(A, p, q)
    quicksortHelper(A, p, r)
    quicksortHelper(A, r + 1, q)
            
            
def quicksort(A):
    
    quicksortHelper(A, 0, len(A))
    



def main():
    A = [1,2,5,2,6,3,7,3,8,4,3,7,5,10]
    quicksort(A)
    print(A)

if __name__ == '__main__':
    main()
