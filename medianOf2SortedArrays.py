def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n = len(nums1)
    m = len(nums2)
    total = n + m
    i = 0
    nCurr = 0
    mCurr = 0
    results = {}

    # fill a new array up with all the sorted elements
    while i < total:
        if nCurr < n and mCurr < m:
            if nums1[nCurr] < nums2[mCurr]:
                results[i] = nums1[nCurr]
                nCurr = nCurr + 1
            else:
                results[i] = nums2[mCurr]
                mCurr = mCurr + 1
        else:
            if nCurr < n:
                results[i] = nums1[nCurr]
                nCurr = nCurr + 1
            else:
                results[i] = nums2[mCurr]
                mCurr = mCurr + 1
        i = i + 1

    # get the median out of the newly sorted array
    if (total) % 2 != 0:
        #array length is odd
        return results[(total//2)]
    else:
        #array length is even
        return (results[total/2-1] + results[total/2]) / float(2)

print(str(findMedianSortedArrays([1,2],[3,4])))
