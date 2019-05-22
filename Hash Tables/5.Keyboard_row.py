class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        final_list = []
        key_list = ['qwertyuiop', 'asdfghjkl','zxcvbnm']
        for word in words:
            count1 = count2 = count3 = 0  
            word_to_push = word
            word = list(set(word.lower()))
            for letter in word:
                if letter in key_list[0]:
                    count1 += 1
                elif letter in key_list[1]:
                    count2 += 1
                elif letter in key_list[2]:
                    count3 += 1
            if count1 == len(word) or count2 == len(word) or count3 == len(word):
                final_list.append(word_to_push)
        return final_list
