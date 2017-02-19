def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        for j in range(i - 1, 0, -1):
            if key <= nums[j]:
                nums[j + 1] = nums[j]
                nums[j] = key
            else:
                break
      
def main():
    A = [1,2,5,2,6,3,7,3,8,4,3,7,5,10]
    insertion_sort(A)
    print(A)

if __name__ == '__main__':
    main()
