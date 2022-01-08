class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        
        res = []
        leng = min(len(word1), len(word2))
        leng1 = leng - 1
        i = 0
        while i < leng:
            res.append(list1[i])
            res.append(list2[i])
            leng -= 1
            list1.remove(list1[i])
            list2.remove(list2[i])
        
        if list1:
            res.extend(list1[::])
        if list2:
            res.extend(list2[::])
        
        
        return ("".join(res))