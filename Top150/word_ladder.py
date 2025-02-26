# https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # self.dists = {}
        if len(wordList) == 0: return 0
        if endWord not in wordList: return 0
        
        graph = self.generate_graph([beginWord, endWord] + wordList)

        q = [beginWord]
        visited = {beginWord:1}

        while q:
            word = q.pop(0)
            current_dist = visited[word]
            for w in graph[word]:
                if w not in visited:
                    visited[w] = current_dist + 1
                    q.append(w)
                else:
                    visited[w] = min(visited[w], current_dist+1)
        
        return 0 if endWord not in visited else visited[endWord]


    def generate_graph(self, words):
        graph = {}
        for w1 in words:
            graph[w1] = []
            for w2 in words:
                # dist = self.dists[(w1,w2)] if (w1,w2) in self.dists else self.gene_dist(w1,w2)
                if self.word_dist(w1,w2) == 1:
                    graph[w1].append(w2)
        return graph
    
    def word_dist(self, w1, w2):
        flag = False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                if flag: 
                    return -1
                flag = True
        # self.dists[(w1,w2)] = dist
        # self.dists[(w2,w1)] = dist
        return 1