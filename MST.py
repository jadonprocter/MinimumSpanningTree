"""
Author: Jadon Procter (procteja)
Description: Implementation of prims algorithm given an adjacency matrix.
Class: OSU CS325 - Summer 2022
"""


def min_unvisited(G, visited):
    node = float("inf")
    minimum_next_node = float("inf")
    minimum_node_weight = float("inf")
    for i in visited:
        for j in range(len(G[i])):
            if G[i][j] < minimum_node_weight and G[i][j] != 0 and j not in visited:
                node = i
                minimum_next_node = j
                minimum_node_weight = G[i][j]
    return node, minimum_next_node, minimum_node_weight


def Prims(G):
    result = []
    visited = [0]
    while len(visited) < len(G):
        node_tuple = min_unvisited(G, visited)
        result.append(node_tuple)
        visited.append(node_tuple[1])

    return result

