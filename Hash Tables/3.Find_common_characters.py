class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        one_word = list(set(A[0]))
        output_array = []
        for s in one_word:
            lowest_count = 10000
            for words in A:
                letter_count = words.count(s)
                if letter_count < lowest_count:
                    lowest_count = letter_count
            for i in range(lowest_count):
                output_array.append(s)
        return output_array
