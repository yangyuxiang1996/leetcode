#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start
class Solution(object):
    """
     拓扑排序
     判断图中是否有环
     解法：广度优先搜索/深度优先搜索
    """
    def canFinish0(self, numCourses, prerequisites):
        """DFS版本
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for to_learn, pre in prerequisites:  # 构建邻接矩阵
            graph[pre].append(to_learn)
        
        visited = set() # 判断
        being_visited = set()

        def dfs(pre):
            if pre in being_visited:  # 有环
                return False
            if pre in visited:
                return True
            
            visited.add(pre)
            being_visited.add(pre)
            for to_learn in graph[pre]:
                if not dfs(to_learn):  # 有环返回false
                    return False
            being_visited.remove(pre)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    def canFinish(self, numCourses, prerequisites):
        """BFS版本
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        from collections import defaultdict
        # 邻接矩阵, dp[i]保存以顶点i为起点的顶点
        graph = defaultdict(list)
        # 记录每个顶点的入度（入度：以当前顶点为终点的有向边的数量，出度：以当前顶点为起点的有向边的数量）
        degree = [0] * numCourses
        for x, y in prerequisites:
            degree[x] += 1
            graph[y].append(x)
        # print(degree)
        queue = deque()
        count = 0
        for i in range(numCourses):
            if degree[i] == 0:
                queue.appendleft(i)
                count += 1
        # print(queue)

        while queue:
            course = queue.pop()
            for tmp in graph[course]:
                degree[tmp] -= 1
                if degree[tmp] == 0:
                    queue.appendleft(tmp)
                    count += 1
        return numCourses == count


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(Solution().canFinish(numCourses, prerequisites))
            

# @lc code=end

