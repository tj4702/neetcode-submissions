class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        all_letters = set()

        for word in words:
            for c in word:
                all_letters.add(c)

        graph = defaultdict(list)
        n = len(words)
        indegree = defaultdict(int)
        res = ''

        for letter in all_letters:
            indegree[letter] = 0 


        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ''

            for c1, c2 in zip(words[i], words[i+1]):
                if c1!= c2:
                    graph[c1].append(c2)
                    indegree[c2] +=1
                    break

        queue = deque()

        for k,v in indegree.items():
            if v == 0 :
                queue.append(k)

        while queue:
            letter = queue.popleft()
            res += letter
            for nei in graph[letter]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
            
        if len(res) < len(all_letters):
            return ''

        return res

            



        