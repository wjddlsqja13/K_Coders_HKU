class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}
        
        def initGraph(equations, values):
            def addEdge(f, t, v):
                if f in g:
                    g[f].append((t, v))
                else:
                    g[f] = [(t, v)]
                    
            for vertices, value in zip(equations, values):
                f, t = vertices
                addEdge(f, t, value)
                addEdge(t, f, 1/value)
        
        def dfs(query):
            n, d = query
            
            if n not in g or d not in g:
                return -1.0
            
            visited = set()
            q = deque([(n, 1.0)])
            
            while q:
                front, curVal = q.popleft()
                if front == d:
                    return curVal
                visited.add(front)
                
                for neighbor, value in g[front]:
                    if neighbor not in visited:
                        q.append((neighbor, value * curVal))
            return -1.0
        
        initGraph(equations, values)
        return [dfs(q) for q in queries]