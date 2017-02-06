# 问题转成,是图是否存在环,
# 利用拓扑排序来求解
# 能拓扑排序必定是偏序图
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        node_map = {}

        for i in range(numCourses):
            node_map[i] = Node(i)

        for pairs in prerequisites:
            node_map[pairs[0]].degree += 1
            node_map[pairs[1]].next.append(pairs[0])

        courses = list(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            remove_list = []
            for i in courses:
                if node_map[i].degree == 0:
                    for child in node_map[i].next:
                        node_map[child].degree -= 1
                    remove_list.append(i)
                    flag = True
            for j in remove_list:
                courses.remove(j)
        return len(courses) == 0

class Node:
    def __init__(self, x):
        self.x = x
        self.next = []
        self.degree = 0


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(3,[[0,1],[0,2],[1,2]]))