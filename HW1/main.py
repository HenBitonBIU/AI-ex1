'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions
import heapq
from collections import namedtuple
from ways import load_map_from_csv
from collections import defaultdict, Counter
import ways
import stats
class my_heap:
    def __init__(self):
        self.heap = []
    def push(self,item):
        heapq.heappush(self.heap,item)

def best_first_graph_search(problem, f):
  node = problem.s_start
  frontier = my_heap(f)
  frontier.append(node)
  closed_list = set()
  while frontier:
    node = frontier.pop()
    if problem.is_goal(node.state):
      return node.solution()
    closed_list.add(node.state)
    for child in node.expand(problem):
      if child.state not in closed_list and child not in frontier:
        frontier.append(child)
      elif child in frontier and f(child) < frontier[child]:
        del frontier[child]
        frontier.append(child)
  return None
def find_ucs_rout(source, target):
    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)


def find_astar_route(source, target):
    'call function to find path, and return list of indices'
    raise NotImplementedError


def find_idastar_route(source, target):
    'call function to find path, and return list of indices'
    raise NotImplementedError
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
   # dispatch(argv)
    distMax = 0
    distMin = 10000000
    roads=ways.load_map_from_csv(start=0, count=10000)
    print(stats.map_statistics(roads))







