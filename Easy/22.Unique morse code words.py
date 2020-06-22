class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = list('abcdefghijklmnopqrstuvwxyz')
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphas = {}
        for i,c in enumerate(chars):
            alphas[c] = morse[i]
        lst = []
        for word in words:
            st = ''
            for char in word:
                st += alphas[char]
            lst.append(st)
        return len(set(lst))
