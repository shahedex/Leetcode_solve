class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        total_list = collections.Counter((A + " " + B).split())
        return [word for word in total_list if total_list[word] == 1]
