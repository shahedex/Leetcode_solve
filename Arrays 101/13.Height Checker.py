class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr_sorted = sorted(heights)
        counter = 0
        for i in range(len(arr_sorted)):
            if arr_sorted[i] != heights[i]:
                counter += 1
        return counter
