class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = [(beginWord,1)]
        for word, length in queue :
            if word == endWord : 
                return length
            for i in range(len(word)) :
                for char in 'abcdefghijklmnopqrstuvwxyz' :
                    tmp = word[:i] + char + word[i+1:]
                    if tmp in wordList :
                        wordList.remove(tmp)
                        queue.append([tmp,length+1])
        return 0