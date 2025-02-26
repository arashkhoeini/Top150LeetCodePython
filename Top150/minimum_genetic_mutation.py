# https://leetcode.com/problems/minimum-genetic-mutation/description/?envType=study-plan-v2&envId=top-interview-150
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if len(bank) == 0: return -1
        if endGene not in bank: return -1
        graph = self.generate_graph([startGene, endGene]+bank)
        # print(graph)
        # now run bfs starting from startGene. the goal is to see if we can reach endGene

        visited = set()
        q = [startGene]
        path_dist = {startGene:0}
        visited.add(startGene)

        while q:
            # print(path_dist)
            gene = q.pop(0)
            current_dist = path_dist[gene]
            for g in graph[gene]:
                if g not in visited:
                    visited.add(g)
                    q.append(g)
                    path_dist[g] = current_dist + 1
                else:
                    path_dist[g] = min(path_dist[g], current_dist+1)
        
        return -1 if endGene not in path_dist else path_dist[endGene]


    def generate_graph(self, genes):
        graph = {}
        for g1 in genes:
            graph[g1] = []
            for g2 in genes:
                if (g1 != g2) and (self.gene_dist(g1,g2) == 1):
                    graph[g1].append(g2)
        return graph
    
    def gene_dist(self, g1, g2):
        dist = 0
        if len(g1) != len(g2):
            return -1
        for i in range(len(g1)):
            if g1[i] != g2[i]:
                dist +=1

        return dist