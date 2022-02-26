class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or beginWord == endWord:
            return []
        L = len(beginWord)
        
        combDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                combDict[word[:i] + "*" + word[i+1:]].append(word)
                
        ans = []
        q = deque()
        q.append([beginWord])
        visited = set([beginWord])
        
        while q and not ans:
            qLen = len(q)
            localVisited = set()
            
            for _ in range(qLen):
                print(visited)
                node = q.popleft()
                for i in range(L):
                    for nextWord in combDict[node[-1][:i] + "*" + node[-1][i+1:]]:
                        if nextWord == endWord:
                            ans.append(node+[nextWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            q.append(node+[nextWord])
                
            visited = visited.union(localVisited)
        return ans