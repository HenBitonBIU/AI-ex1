from Problem import Problem
class Node:
    def __init__(self, junction, parent=None, action=None, cost=0):
        self.state = junction.index
        self.father = parent
        self.links = junction.links
        self.cost = cost
        self.h = 0

    def solution(self):
        if self.father!=None:
            return self.father.solution() + ", " + str(self.state[0])
        else:
            return str(self.state[0])

    def total_cost(self):
        return self.g + self.h

    def path(self):
        path = []
        current_node = self
        while current_node:
            path.append(current_node.state)
            current_node = current_node.parent
        path.reverse()
        return [s for s in path]

    def ordered_set(self, coll):
        return dict.fromkeys(coll).keys()

    def child_node(self, problem, action):
        next_state = problem.succ(self.state, action)
        parent = self
        next_node = Node(next_state, None, None,
                         self.cost + problem.step_cost(self.state, action))
        return next_node

    def expand(self, problem):
        nodes = self.links
        send = []
        for l in nodes:
            next_state = problem.roads[l.target]
            time = self.cost + problem.step_cost(self, l)
            next_node = Node(next_state, self, None, time)
            send.append(next_node)
        return send

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