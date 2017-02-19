import math
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    nums1 = merge_sort(nums[:len(nums) // 2]) #####python 3
    nums2 = merge_sort(nums[len(nums) // 2:])
    return merge(nums1, nums2)
def merge(nums1, nums2):
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i < len(nums1):
        res.extend(nums1[i:])
    if j < len(nums2):
        res.extend(nums2[j:])
    return res
        


def main():
    A = [1,2,5,2,6,3,7,3,8,4,3,7,5,10]
    print(merge_sort(A))

if __name__ == '__main__':
    main()
