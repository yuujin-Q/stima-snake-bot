from src.logic.point.point import Point


class SearchNode:
    def __init__(self, search_point, path_list, path_cost):
        self.search_point = search_point
        self.path_list = [direction for direction in path_list]
        self.path_cost = path_cost

    def add_self_to_movement_list(self):
        self.path_list = self.path_list + [self.search_point]

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def get_search_point(self):
        return self.search_point

    def get_movement_list(self):
        return self.path_list[:]

    def get_path_cost(self):
        return self.path_cost
