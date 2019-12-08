import Node
from ways import info
from ways import compute_distance
class Problem:
    def __init__(self,source,target,roads):
        self.s_start=source
        self.s_target=target
        self.roads=roads
    def is_goal(self,state):
        return state == self.s_target

    def actions(self, s):
        return self.roads[s.index].links

    def link_cost(self, state, lnk):
        speed = info.SPEED_RANGES[lnk[3]][1]
        return (lnk[2] / 1000) / speed

    def get_link(self, s, a):
        link = [l for l in s.links if l.target == a.index]
        return link[0]

    def heuristic_cost(self, s, a):
        return compute_distance(s.lat, s.lon, a.lat, a.lon)

    def succ(self, s, a):
        nodes = [self.roads[l.target] for l in s.links]
        for n in nodes:
            if a.target == n.index:
                return n

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state)
class Problem1:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.roads = graph

    def actions(self, s):
        return self.roads[s.index].links

    def succ(self, s, a):
        nodes = [self.roads[l.target] for l in s.links]
        for n in nodes:
            if a.target == n.index:
                return n

    def is_goal(self, s):
        return s == self.goal.state

    def get_link(self, s, a):
        link = [l for l in s.links if l.target == a.index]
        return link[0]

    def kph_to_mpm(self, speed):
        return (1000 / 60) * speed

    def step_cost(self, s, a):
        link = a
        max_speed = max(SPEED_RANGES[link.highway_type])
        time = float(link.distance)/max_speed
        return time /1000

    def heuristic_cost(self, s, a):
        return compute_distance(s.lat, s.lon, a.lat, a.lon)