class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_length = len(arr)
        last_mod = -1
        for j in range(arr_length):
            if last_mod == j:
                continue
            if arr[j] == 0:
                last_mod = j + 1
                for i in range(arr_length-1, last_mod, -1):
                    arr[i] = arr[i-1]
                if last_mod < arr_length:
                    arr[last_mod] = 0
        return arr
