class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        n = len(beginWord)

        if len(beginWord) != len(endWord):
            return 0
        
        wordList = set(word for word in wordList if len(word) == n)
        
        queue = deque()
        visited = set()
        visited.add(beginWord)
        queue.append((beginWord,1))


        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(n):
                for j in range(26):
                    letter = chr(ord('a') + j )
                    if letter == word[i]:
                        continue
                    curr_word = word[:i] + letter + word[i+1:]

                    if curr_word in wordList and curr_word not in visited:
                        visited.add(curr_word)
                        queue.append((curr_word, step+1))


        return 0 



            


