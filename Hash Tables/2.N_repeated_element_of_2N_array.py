class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        unique_elements = list(set(A))
        number_of_unique_elements = len(A)/2
        
        for e in unique_elements:
            if A.count(e) == number_of_unique_elements:
                return e
