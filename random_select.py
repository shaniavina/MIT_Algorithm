import numpy as np
import quicksort 

def random_select(A, p, q, i):
    if p == q:
        return A[p]
    r = random_select_helper(A, p, q)
    k = r + 1
    if i == k:
        return A[r]
    elif i < k:
        return random_select(A, p, r, i)
    else:
        return random_select(A, r + 1, q, i)

def random_select_helper(A, p, q):
    r = quicksort.partition(A, p, q, choose_pivot(A, p, q))
    return r
    

def choose_pivot(A, p, q):
    n = q - p
    if n < 5:
        return p
    k = p
    num_group = n // 5
    l = [[0, 0, 0, 0, 0] for i in range(num_group)]
    median_list = []
    for i in range(p, p + 5 * num_group, 5):
        median = int(np.median(A[i:i+5]))
        index = i
        for j in range(i, i + 5):
            if A[j] == median:
                index = j
                break
        print(A, p, q, i, median, index)
        median_list.append((median, index))
    median_list.sort(key=lambda x:x[0]) 
    print(median_list)
    return int(median_list[(num_group - 1) // 2][1])

def main():
    A = [1,2,5,2,6,3,7,3,8,4,3,7,5,10]
    res = random_select(A, 0, len(A), 7)
    print(res)

if __name__ == '__main__':
    main()
