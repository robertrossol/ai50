class Node():
    def __init__(self, actor, parent, movie):
        self.actor = actor
        self.parent = parent
        self.movie = movie

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_actor(self, actor):
        return any(node.actor == actor for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def len(self):
        return len(self.frontier)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
