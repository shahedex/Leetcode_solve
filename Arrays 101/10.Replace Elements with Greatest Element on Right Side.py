class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        le = len(arr)
        maxi = 0
        lefi = 0
        while maxi != le-1:
            m = -1
            for i in range(maxi+1, le):
                if arr[i] > m:
                    m = arr[i]
                    maxi = i
            for j in range(lefi, maxi):
                arr[j] = m
                lefi += 1
        arr[le-1] = -1
        return arr

    
# le = len(arr)
# for i in range(le-1):
#     great = -1
#     for j in range(i+1, le):
#         if arr[j] > great:
#             great = arr[j]
#     arr[i] = great
# arr[le-1] = -1
# return arr
