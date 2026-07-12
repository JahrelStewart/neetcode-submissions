class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for wrd in words:
            for c in wrd:
                dic[c] = dic.get(c, 0) + 1
        
        for c in dic:
            if dic[c] % len(words):
                return False
        
        return True