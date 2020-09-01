import collections
def buildorder(points,edges):
    graph = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        indegree[edge[1]]+=1
    q = collections.deque()
    visited = set()
    res = []
    for point in points:
        if indegree[point]==0:
            q.append(point) 
    while q:
        node = q.popleft()
        visited.add(node)
        res.append(node)
        for newnode in graph[node]:
            if newnode not in visited:
                indegree[newnode]-=1
                if indegree[newnode]==0:
                    q.append(newnode)
    if len(res)< len(points):
        return -1
    return res
import unittest
class Test(unittest.TestCase):
    def test(self):
        points = (1,2,3,4,5,6,7,8)
        edges = [(1,2),(2,3),(3,4),(5,4),(6,3),(6,4),(7,8)]
        edges2 = [(1,2),(2,3),(3,4),(5,4),(6,3),(6,4),(7,8),(8,7)]
        print(buildorder(points,edges), buildorder(points,edges2))
if __name__=="__main__":
    unittest.main()
