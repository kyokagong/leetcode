# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


#DFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    cache = {}
    def cloneGraph(self, node):

        return self._clone(node)

    def _clone(self, node):
        if node is None:
            return None
        if node.label in self.cache:
            return self.cache[node.label]
        cloneNode = UndirectedGraphNode(node.label)
        self.cache[cloneNode.label] = cloneNode
        for neighbor in node.neighbors:
            cloneNode.neighbors.append(self._clone(neighbor))

        return cloneNode

#BFS
class Solution2:
    # @param node, a undirected graph node
    # @return a undirected graph node
    cache = {}
    def cloneGraph(self, node):
        if node is None:
            return None
        root = UndirectedGraphNode(node.label)
        queue = [node]
        self.cache[node] = root
        while queue:
            cur = queue.pop(0)
            clone_cur = self.cache[cur]
            for neighbor in cur.neighbors:
                if neighbor in self.cache:#如果在cache里,代表已经跑过这个node的neighbors了,所以不用再visit多一次
                    clone = self.cache[neighbor]
                else:
                    clone = UndirectedGraphNode(neighbor.label)
                    self.cache[neighbor] = clone
                    queue.append(neighbor)
                clone_cur.neighbors.append(clone)
        return root


if __name__ == '__main__':
    a = UndirectedGraphNode(1)
    a.neighbors.append(a)
    s = Solution2()
    b = s.cloneGraph(a)
    UndirectedGraphNode(None)
    print(id(b)==id(a))
    print()