import pygame
from queue import PriorityQueue
from src.logic.snakebot.models.searchnode import SearchNode
from src.logic.snakebot.models.gridmap import GridMap
from src.logic.point.point import Point


class SnakeBot:
    solution_cost = float('inf')
    solution_path = []
    show_debug = False

    def __init__(self, screen: pygame.display, snake_body, pixel_size, show_debug=False):
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.graph = GridMap(screen_width, screen_height, snake_body[:len(snake_body)-1], pixel_size)
        self.show_debug = show_debug

    def plan_route(self, start_point, finish_point):
        # SETUP: priority queue, starting node, explored nodes
        search_pqueue = PriorityQueue()
        starting_node = SearchNode(start_point, [], 0)

        # enqueue start_node;
        node_priority = starting_node.get_path_cost() + Point.euclidean_distance(start_point, finish_point)

        search_pqueue.put((node_priority, starting_node))
        explored_points = set()

        # SEARCH: do search loop
        while not search_pqueue.empty():
            # dequeue current node to search
            node_priority, current_node = search_pqueue.get()
            current_node.add_self_to_movement_list()

            # show debug messages
            if self.show_debug is True:
                file_path = "log.txt"  # Replace with your desired file path
                file = open(file_path, "a+")

                file.write(str(node_priority) + "---" + current_node.get_search_point().to_string()
                           + str(current_node.get_path_cost()))
                for move in current_node.get_path_list():
                    file.write("   ")
                    file.write(move.to_string() + ",\n")
                file.write("\n")

                # Close the file
                file.close()

            # Goal check: return from function if goal is met
            if current_node.get_search_point() == finish_point:
                self.solution_path = current_node.get_path_list()
                self.solution_cost = current_node.get_path_cost()

                print("Solution found")
                return

            if current_node.get_search_point() in explored_points:
                continue

            # enqueue neighbors
            for neighbor_point in self.graph.get_neighbors(current_node.get_search_point()):
                if neighbor_point not in explored_points:
                    neighbor_cost = current_node.get_path_cost() + \
                                    Point.manhattan_distance(current_node.get_search_point(), neighbor_point)
                    # distance between neighbors in grid is same as manhattan distance

                    new_neighbor_node = SearchNode(neighbor_point, current_node.get_path_list(), neighbor_cost)

                    # enqueue neighbor to search queue
                    node_priority = neighbor_cost + Point.euclidean_distance(neighbor_point, finish_point)

                    search_pqueue.put((node_priority, new_neighbor_node))

            # mark current node as visited
            explored_points.add(current_node.get_search_point())

            if search_pqueue.empty():
                for position in current_node.get_path_list():
                    print(position.to_string())
                self.solution_path = current_node.get_path_list()[0:2]

        # Search failed
        print("Search failed")

    def get_movement_list(self):
        if len(self.solution_path) <= 1:
            return []
        else:
            return [self.solution_path[i] - self.solution_path[i-1] for i in range(1, len(self.solution_path))]
