# region Description
from ways import graph
from ways import info

KILOMETER_TO_METER = 1000
#print("xd")
roads = graph.load_map_from_csv(start=0,count = 100)
junctions = roads.junctions()


class Junction_Node:

    def __init__(self, index, parent=None, newCost=0):
        self.index = index
        self.junction = junctions[index]
        self.parent = parent
        self.cost = newCost

    def step_cost(self, link):
        max_speed = max(info.SPEED_RANGES[link.highway_type])
        time = float(link.distance) / max_speed
        return time / 1000

    def expand(self):
        target_nodes, node_time_distances = [link.target for link in self.junction.links] \
            , [self.step_cost(link) for link in self.junction.links]
        childs = []
        for target, distance in zip(target_nodes, node_time_distances):
            childs.append(self.child_node(target, distance))

        return childs

    def path(self):
        path = []
        current_node = self
        while current_node:
            path.append(current_node.index)
            current_node = current_node.parent
        path.reverse()
        return [s for s in path]

    def child_node(self, junction, time_cost):
        # cost = time.
        next_node = Junction_Node(junction, self, self.cost + time_cost)
        return next_node

    def __repr__(self):
        return f"<{self.cost}>"

    def __lt__(self, node):
        return self.cost < node.cost

    def __eq__(self, other):
        return isinstance(other, Junction_Node) and self.cost == other.cost

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.cost)
# endregion
