class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(list)
        n = len(beginWord)
        alphabets = [chr(num + ord('a')) for num in range(26)]
        wordList = set(word for word in wordList if len(word) == n)
        no_words = len(wordList)

        matrix_words = defaultdict(list)

        if len(endWord) != n or no_words == 0 or endWord not in wordList:
            return 0

        def get_neighbours(word):
            neighbours = []
            if len(word) != n :
                return []
            for pos in range(n):
                for alphabet in alphabets:
                    curr = word[:pos] + alphabet + word[pos+1:]
                    if curr in wordList and curr != word:
                        neighbours.append(curr)

            return neighbours


        for word in wordList:
            graph[word] = get_neighbours(word)
        

        # the graph is built 
        # now we build the ladder am I right 

        visited = set()
        queue = deque(get_neighbours(beginWord))
        ladder_steps = 1

        while queue:
            q = len(queue)

            for i in range(q):
                word = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        return ladder_steps +1
                    queue.extend(graph[word])

            ladder_steps +=1
            
            
        return 0 
            







