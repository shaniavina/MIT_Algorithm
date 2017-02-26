def counting_sort(A):
    C = [0 for i in range(max(A) + 1)]
    B = [0 for i in range(len(A))]
    
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, max(A) + 1):
        C[i] += C[i - 1]
    for i in range(len(A) - 1 , -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B




def main():
    A = [1,2,5,2,6,3,7,3,8,4,3,7,5,10]
    print(counting_sort(A))

if __name__ == '__main__':
    main()
