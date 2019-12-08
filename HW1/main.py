'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions
import heapq
from Node import Node
from Problem import Problem
from PriorityQueue import PriorityQueue
from collections import namedtuple
from ways import load_map_from_csv
from collections import defaultdict, Counter
from ways import compute_distance
from ways.info import SPEED_RANGES
import ways
import stats
from ways import info
class my_heap:
    def __init__(self):
        self.heap = []
    def push(self,item):
        heapq.heappush(self.heap,item)


def best_first_graph_search(s1, s2, f):
    node = s1
    frontier = PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    log = []
    closed_list = set()
    while frontier:
        node = frontier.pop()
        log.append(node)
        if node.index == s2.index:
            print(node.path(), node.cost, len(closed_list))
            return node.cost
        closed_list.add(node.index)
        links = node.expand()
        for child in links:
            is_in_Frontier = child not in frontier
            if child.index not in closed_list and is_in_Frontier:
                frontier.append(child)
            elif not is_in_Frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return []
def find_ucs_rout(source, target):
    roads = ways.load_map_from_csv(start=0,count=100)
    problem=Problem(source,target,roads)
    def g(node):
        def g(node):
            return lambda node: node.cost
    return best_first_graph_search(source,target, g)


def find_astar_route(source, target):
    roads = ways.load_map_from_csv(start=0,count=100)
    problem = Problem(source, target, roads)
    def g(node):
        return node.cost
    def h(node):
        node_junction = node.junction
        target_junction = target.junction
        return ways.compute_distance(node_junction.lat, node_junction.lon, target_junction.lat, target_junction.lon)
    return best_first_graph_search(source,target,lambda n: g(n) + h(n))


def find_idastar_route(source, target):
    roads = ways.load_map_from_csv()
    problem = Problem(source, target, roads)
    'call function to find path, and return list of indices'
    raise NotImplementedError


def dispatch(argv):
    # from Problem import Node
    # from Problem import Problem
    # from ways import graph
    from Utils import Junction_Node

    s1 = Junction_Node.Junction_Node(1)
    s2 = Junction_Node.Junction_Node(7)

    # if argv[1] == 'ucs':
    path = print(find_astar_route(s1, s2))
    # elif argv[1] == 'astar':
    #     path = best_first_graph_search(source, target)
    # elif argv[1] == 'idastar':
    #     path = find_idastar_route(source, target)
    # print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
   # roads=ways.load_map_from_csv(start=0, count=10000)
    #print(stats.map_statistics(roads))







