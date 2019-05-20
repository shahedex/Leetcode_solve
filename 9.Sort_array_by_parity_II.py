class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list = [i for i in A if i%2 != 0]
        even_list = [i for i in A if i%2 == 0]
        
        final_sorted_list = []
        
        for i in range(len(odd_list)):
            final_sorted_list.append(even_list[i])
            final_sorted_list.append(odd_list[i])
        return final_sorted_list
