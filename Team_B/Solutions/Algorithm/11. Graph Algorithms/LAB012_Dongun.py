class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(word):
            if word in cache:
                return cache[word]
            cache[word] = False
            for i in range(1, len(word)):
                s, e = word[:i], word[i:]
                if s in d and e in d:
                    cache[word] = True
                    break
                if dfs(s) and e in d:
                    cache[word] = True
                    break
            return cache[word]
    
        d = set(words)
        cache = {}
        
        return [word for word in words if dfs(word)]
            
            
        
