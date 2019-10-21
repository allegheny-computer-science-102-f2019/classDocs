#!/usr/bin/env python3

# Algorithm Code referenced for modification: https://www.python.org/doc/essays/graphs/


DATE = "21 Oct 2019"
VERSION = "i"
AUTHOR = "NAME"

'''
Program to find the path between two vertices in a graph. The beginning and end nodes of a path hardcoded in the program.
'''

# Starting and ending nodes:
node1_str = "A"
node2_str = "C"

#00
graph00 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
#01 TODO: fill in the graph
graph01 = {}

#02 TODO
graph02 = {}


# change the number of the graph in the next line to change graphs
graph = graph00
#graph = graph01
#graph = graph02


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        #if not graph.has_key(start):
        if not start in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
# end of find_all_paths()


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
    if not start in graph:
        return None
    for node in graph[start]:
         if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None
#end of find_path


print("\t A simple function to determine a path between two nodes.",node1_str,"and", node2_str)

l_list = find_path(graph, node1_str, node2_str)
print("\t Graph: ",graph, type(graph)) # graph is in a dictionary


print("\n\t + Finding a path from",node1_str,"to",node2_str)
if l_list != None:
    print("\t   Path: ",l_list)
else:
    print("\t   There was no path. :-( ")





print("\n\t + Finding all paths from",node1_str,"to",node2_str)
p_list = find_all_paths(graph, node1_str, node2_str)
if p_list != None:
    print("\t   Path(s): ",p_list)
else:
    print("\t   There was no path. :-( ")
