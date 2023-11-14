from random import random
from typing import List
from math import cos, sin, pi
import pygame as py
from pygame.math import Vector2
from dataclasses import dataclass
import random

class Node():
    def __init__(self):
        self.links: List[Link] = []
        self.isGrab: bool = False

    @staticmethod
    def compute_position(position: Vector2, angle, length):
        newX = position[0] + cos(angle) * length
        newY = position[1] + sin(angle) * length

        return Vector2(newX, newY)

    def add_link(self, angle, length):
        new_node = Node()
        self.links.append(Link(new_node, angle, length))
        return new_node

@dataclass
class Link():
    node: Node
    angle: int
    length: int

class Entity():
    def __init__(self, position: Vector2):
        self.nodes: List[Node] = [Node()]
        self.position: Vector2 = position

    def add_node(self):
        nodes_len = len(self.nodes)
        node_nb = random.randrange(0, nodes_len)
        angle = random.uniform(0, 2 * pi)
        length = random.uniform(60, 100)
        new_node = self.nodes[node_nb].add_link(angle, length)
        self.nodes.append(new_node)


    def draw_enities(self, surface):
        visited: List[Node] = []

        def draw_graph(node: Node, position: Vector2):
            if node not in visited:
                # print(node)
                py.draw.circle(surface, (0, 0, 0), position, 10)
                visited.append(node)
                for neighbour in node.links:
                    newPos = Node.compute_position(position, neighbour.angle, neighbour.length)
                    py.draw.line(surface, (0, 0, 0), position, newPos, 3)
                    draw_graph(neighbour.node, newPos)
        draw_graph(self.nodes[0], self.position)

visited = list() # Set to keep track of visited nodes of graph.

