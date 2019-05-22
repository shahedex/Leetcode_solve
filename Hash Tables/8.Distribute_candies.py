class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candies = list(set(candies))
        if len(unique_candies) < int(len(candies)/2):
            return len(unique_candies)
        else:
            return int(len(candies)/2)
