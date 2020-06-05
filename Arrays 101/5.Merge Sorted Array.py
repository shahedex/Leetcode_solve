class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        org_n = n
        for ind2, i in enumerate(nums2):
            for ind, val in enumerate(nums1):
                if i <= val:
                    nums1.insert(ind, i)
                    nums1.pop()
                    n -= 1
                    m += 1
                    break
        while n > 0:
            nums1.insert(m, nums2[org_n - n])
            nums1.pop()
            m += 1
            n -= 1
