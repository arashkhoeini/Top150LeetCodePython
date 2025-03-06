# https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.graph = self.generate_graph(numCourses, prerequisites)

        if numCourses == 0: return True
        # if numCourses != len(actual): return False

        self.visited = [0 for _ in range(numCourses)]
        for k in range(numCourses):
            if self.visited[k] == 0:
                if not self.dfs(k):
                    return False
        return True
                        
        
        return True
    def dfs(self, start):
        if self.visited[start] == 1: return False
        if self.visited[start] == 2: return True

        self.visited[start] = 1
        for n in self.graph[start]:
            if not self.dfs(n):
                return False
        self.visited[start] = 2
        return True

    def generate_graph(self, num_courses, pres):
        graph = {i:[] for i in range(num_courses)}
        for i,j in pres:
            graph[j].append(i)
        
        return graph

            