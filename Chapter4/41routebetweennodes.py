#directed graph ((1,2),(2,3),(2,4),(3,4),(4,5),(5,6),(6,8),(7,8), there is route 1 to 8, no route 1 to 7)
import collections
def routebetweennodes(edges,node1,node2):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    q = collections.deque()
    q.append(node1)
    visited = set()
    while q:
        node = q.popleft()
        if node == node2:
            return True
        visited.add(node)
        for nextnode in graph[node]:
            if nextnode not in visited:
                q.append(nextnode)
    return False
import unittest
class Test(unittest.TestCase):
    def test(self):
        edges = [(1,2),(2,3),(2,4),(3,4),(4,5),(5,6),(6,8),(7,8)]
        self.assertEqual(routebetweennodes(edges,1,8),True)
        self.assertEqual(routebetweennodes(edges,1,7), False)
if __name__ == "__main__":
  unittest.main()






