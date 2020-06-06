class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for p in sorted(people, key=lambda x: [-x[0], x[1]]):
            _, c = p
            result.insert(c, p)
        return result
