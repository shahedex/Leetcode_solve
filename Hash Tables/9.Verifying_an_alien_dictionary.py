class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indexed_order = {c:i for i,c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for c1, c2 in zip(w1, w2):
                if indexed_order[c1] > indexed_order[c2]:
                    return False
                elif indexed_order[c1] < indexed_order[c2]:
                    break
        return True
