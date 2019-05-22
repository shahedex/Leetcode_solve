class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total_jewel_count = 0
        for j in J:
            total_jewel_count += S.count(j)
        return total_jewel_count
