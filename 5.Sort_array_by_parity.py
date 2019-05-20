class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_list = [i for i in A if i%2 != 0]
        even_list = [i for i in A if i%2 == 0]
        
        return even_list + odd_list
