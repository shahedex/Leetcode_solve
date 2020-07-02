class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        return " ".join(c[::-1] for c in ss)
       
# for c in ss:
#     ret += c[::-1]
#     ret += ' '
# return ret.strip()
